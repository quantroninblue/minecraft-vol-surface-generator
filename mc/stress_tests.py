import numpy as np
from surfaces.procedural_surface import procedural_surface

def calibrate_to_surface(K, T, IV_market, seeds=50):
    best_seed = 0
    best_error = np.inf

    for s in range(seeds):
        IV_model = procedural_surface(K, T, seed=s)
        err = np.mean((IV_market - IV_model)**2)

        if err < best_error:
            best_error = err
            best_seed = s

    return best_seed, best_error
