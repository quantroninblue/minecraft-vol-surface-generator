from strategies.delta_hedge import simulate_delta_hedge_batch
import numpy as np

def hostile_hedge_test_cached(worlds):
    seeds = [w["seed"] for w in worlds]
    return simulate_delta_hedge_batch(seeds)

