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

def precompute_hostile_worlds(template, K, T, n_worlds=1000):
    worlds = []
    for i in range(n_worlds):
        worlds.append(generate_hostile_world(K, T, template, seed=i))
    return worlds
