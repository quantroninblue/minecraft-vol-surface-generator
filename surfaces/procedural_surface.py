from noise.fbm import fbm
from surfaces.crash_injector import inject_crash_caves

def procedural_surface(K, T, template, seed=0, noise_scale=3.0, noise_amp=0.04):
    x = K * noise_scale
    y = T * noise_scale

    noise = fbm(x, y, octaves=5, seed=seed)
    IV = template(K, T) + noise_amp * noise

    return inject_crash_caves(IV, K, T, seed=seed)
