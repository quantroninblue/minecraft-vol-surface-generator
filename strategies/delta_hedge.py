import numpy as np
from surfaces.procedural_surface import procedural_surface
from scipy.stats import norm

def bs_price(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)

def bs_delta(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
    return norm.cdf(d1)

def simulate_delta_hedge(S0=100, K=100, T=0.5, r=0.0, steps=120, seed=0):
    dt = T / steps
    S = S0
    cash = 0.0
    shares = 0.0

    for t in range(steps):
        tau = T - t*dt
        moneyness = K / S

        sigma = procedural_surface(np.array([[moneyness]]), np.array([[tau]]), seed=seed)[0,0]

        price = bs_price(S, K, tau, r, sigma)
        delta = bs_delta(S, K, tau, r, sigma)

        target_shares = delta
        cash -= (target_shares - shares) * S
        shares = target_shares

        dW = np.random.randn() * np.sqrt(dt)
        S *= np.exp(-0.5*sigma**2*dt + sigma*dW)

    payoff = max(S - K, 0)
    pnl = cash + shares*S - payoff
    return pnl
