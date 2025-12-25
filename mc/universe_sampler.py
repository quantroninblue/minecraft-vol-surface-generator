import numpy as np
from surfaces.procedural_surface import procedural_surface
from mc.regime_mutators import spike_faults, skew_flip, convexity_trap, liquidity_collapse

def generate_world(K, T, template, seed):
    IV = procedural_surface(K, T, template, seed=seed)
    return {"IV": IV, "K": K, "T": T, "seed": seed}

def generate_hostile_world(K, T, template, seed):
    IV = procedural_surface(K, T, template, seed=seed)
    IV = spike_faults(IV, K)
    IV = skew_flip(IV, K)
    IV = convexity_trap(IV, T)
    IV = liquidity_collapse(IV)
    return {"IV": IV, "K": K, "T": T, "seed": seed}

def sample_universe(template, K, T, n_worlds=1000, hostile=False):
    worlds = []
    for i in range(n_worlds):
        if hostile:
            worlds.append(generate_hostile_world(K, T, template, i))
        else:
            worlds.append(generate_world(K, T, template, i))
    return worlds
