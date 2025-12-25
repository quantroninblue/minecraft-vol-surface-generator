import numpy as np
from noise.fbm import fbm
from surfaces.crash_injector import inject_crash_caves

def procedural_surface_batch(K, T, template, seeds, noise_scale=6.0, noise_amp=0.10):
    base = template(K, T)   # compute ONCE
    worlds = []
    for s in seeds:
        x = K * noise_scale
        y = T * noise_scale
        noise = fbm(x, y, octaves=5, seed=int(s))
        IV = base + noise_amp * noise
        IV = inject_crash_caves(IV, K, T, seed=int(s))
        worlds.append(IV.astype(np.float32))
    return np.stack(worlds, axis=0)
