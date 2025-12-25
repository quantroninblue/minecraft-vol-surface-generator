import numpy as np

def base_surface(K, T):
    """
    Smooth baseline implied vol surface.
    K : moneyness (K / S)
    T : maturity in years
    """

    # ATM term structure
    atm = 0.18 + 0.07 * np.sqrt(T)

    # Equity-style skew
    skew = -0.25 * (K - 1.0)

    # Smile curvature
    smile = 0.35 * (K - 1.0) ** 2

    return atm + skew + smile
