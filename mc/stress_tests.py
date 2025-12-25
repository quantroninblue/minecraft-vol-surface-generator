import numpy as np
from mc.universe_sampler import sample_universe
from strategies.delta_hedge import simulate_delta_hedge

def hostile_hedge_test(template, K, T, n_worlds=1000):
    """
    Runs delta hedging inside adversarial volatility universes.
    Returns array of PnLs.
    """
    worlds = sample_universe(template, K, T, n_worlds=n_worlds, hostile=True)
    pnls = []

    for w in worlds:
        pnl = simulate_delta_hedge(seed=w["seed"])
        pnls.append(pnl)

    return np.array(pnls)
