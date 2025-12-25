import numpy as np
from surfaces.procedural_batch import procedural_surface_batch
from mc.regime_mutators import spike_faults, skew_flip, convexity_trap, liquidity_collapse

def precompute_hostile_worlds(template, K, T, n_worlds=1000):
    seeds = np.arange(n_worlds)
    IVs = procedural_surface_batch(K, T, template, seeds)

    worlds = []
    for i in range(n_worlds):
        IV = IVs[i]
        IV = spike_faults(IV, K)
        IV = skew_flip(IV, K)
        IV = convexity_trap(IV, T)
        IV = liquidity_collapse(IV)
        worlds.append({"IV": IV, "K": K, "T": T, "seed": int(i)})
    return worlds
