import numpy as np

def surface_metrics(IV, K, T):
    # Central slices
    k_mid = IV.shape[1] // 2
    t_short = np.argmin(T[:,0]) + 1

    # Skew steepness near ATM
    skew_grad = np.gradient(IV[:, k_mid], K[0, :])[t_short]

    # Short-term convexity
    short_slice = IV[t_short, :]
    convex = np.mean(np.gradient(np.gradient(short_slice, K[0, :]), K[0, :]))

    # Tail corridor density (how many extreme-vol pockets)
    high_tail = np.percentile(IV, 92)
    corridor_density = np.mean(IV > high_tail)

    return float(skew_grad), float(convex), float(corridor_density)

def hostile_failure_pnl(world, exposure_scale=1.0, shock_scale=1.0):
    IV = world["IV"]
    K = world["K"]
    T = world["T"]

    skew, convex, corridor = surface_metrics(IV, K, T)

    # Geometry-driven terminal shock (fatter tails when corridors are dense)
    tail_fat = 1.0 + 6.0 * corridor
    shock = np.random.standard_t(df=3) * shock_scale * tail_fat

    # Structural loss model: skew & convexity amplify damage
    pnl = - exposure_scale * (abs(skew)*1.5 + abs(convex)*2.5) * abs(shock)

    # Liquidity cliff kicker
    pnl *= (1.0 + 4.0 * corridor)

    return pnl
