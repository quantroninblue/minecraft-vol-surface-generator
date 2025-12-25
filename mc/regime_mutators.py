import numpy as np

def spike_faults(IV, K):
    return IV + 0.15 * (K < 0.9)

def skew_flip(IV, K):
    return IV * (1 + 0.4 * (K - 1))

def convexity_trap(IV, T):
    return IV * (1 + 0.6 * (T < 0.25))

def liquidity_collapse(IV):
    return IV * (1 + 0.5 * (IV > np.percentile(IV, 90)))

