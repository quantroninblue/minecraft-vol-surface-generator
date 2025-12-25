import numpy as np
from noise.fbm import fbm

def inject_crash_caves(IV, K, T, seed=0, cave_amp=0.12, threshold=-0.35):
    """
    Carves negative-noise tunnels into the volatility surface to represent crash regimes.
    """

    x = K * 4.0
    y = T * 4.0

    caves = fbm(x, y, octaves=3, seed=seed + 100)

    mask = caves < threshold
    IV_crash = IV.copy()
    IV_crash[mask] += cave_amp * np.abs(caves[mask])

    return IV_crash
