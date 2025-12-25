import numpy as np
from noise.fbm import fbm
from surfaces.base_surface import base_surface

def procedural_surface(K, T, seed=0, noise_scale=3.0, noise_amp=0.04):
    x = K * noise_scale
    y = T * noise_scale

    noise = fbm(x, y, octaves=5, seed=seed)
    return base_surface(K, T) + noise_amp * noise
