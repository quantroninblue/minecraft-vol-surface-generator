import numpy as np

def fast_delta_hedge(seeds, S0=100, K=100, T=0.5, r=0.0, steps=120):
    n = len(seeds)
    dt = T / steps

    S = np.full(n, S0, dtype=np.float32)
    cash = np.zeros(n, dtype=np.float32)
    shares = np.zeros(n, dtype=np.float32)

    for t in range(steps):
        tau = T - t * dt

        # Synthetic hostile vol dynamics (no expensive surface calls)
        sigma = 0.25 + 0.12 * np.sin(0.3 * np.array(seeds, dtype=np.float32) + tau*6)

        d1 = (np.log(S/K) + (r + 0.5*sigma*sigma)*tau) / (sigma*np.sqrt(tau))
        delta = 0.5 * (1 + np.tanh(0.7978845608 * d1))  # erf approx

        target = delta
        cash -= (target - shares) * S
        shares = target

        dW = np.random.randn(n).astype(np.float32) * np.sqrt(dt)
        S *= np.exp(-0.5*sigma*sigma*dt + sigma*dW)

    payoff = np.maximum(S - K, 0)
    return cash + shares*S - payoff

