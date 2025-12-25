import numpy as np
from noise.perlin import perlin

def fbm(x, y, octaves=5, persistence=0.5, lacunarity=2.0, seed=0):
    value = np.zeros_like(x)
    amplitude = 1.0
    frequency = 1.0

    for i in range(octaves):
        value += amplitude * perlin(x * frequency, y * frequency, seed + i)
        amplitude *= persistence
        frequency *= lacunarity

    return value
