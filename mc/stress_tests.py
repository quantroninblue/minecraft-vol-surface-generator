from strategies.delta_hedge import fast_delta_hedge

def hostile_hedge_test_cached(worlds):
    seeds = [w["seed"] for w in worlds]
    return fast_delta_hedge(seeds)

