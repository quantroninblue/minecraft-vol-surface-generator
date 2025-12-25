import numpy as np
from scipy.stats import norm

def simulate_delta_hedge_batch(seeds, S0=100, K=100, T=0.5, r=0.0, steps=120):
    """
    Vectorized delta hedging across many hostile worlds at once.
    """
    n = len(seeds)
    dt = T / steps

    S = np.full(n, S0)
    cash = np.zeros(n)
    shares = np.zeros(n)

    for t in range(steps):
        tau = T - t * dt
        sigma = 0.25 + 0.15 * np.sin(0.1 * np.array(seeds) + tau*5)

        d1 = (np.log(S/K) + (r + 0.5*sigma**2)*tau) / (sigma*np.sqrt(tau))
        delta = norm.cdf(d1)

        target = delta
        cash -= (target - shares) * S
        shares = target

        dW = np.random.randn(n) * np.sqrt(dt)
        S *= np.exp(-0.5*sigma**2*dt + sigma*dW)

    payoff = np.maximum(S - K, 0)
    return cash + shares*S - payoff
