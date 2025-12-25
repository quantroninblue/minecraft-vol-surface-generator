import numpy as np
from strategies.delta_hedge import simulate_delta_hedge

def sample_universe(n_worlds=1000):
    pnls = [simulate_delta_hedge(seed=i) for i in range(n_worlds)]
    return np.array(pnls)
