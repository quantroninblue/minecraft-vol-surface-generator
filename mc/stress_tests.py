import numpy as np
from strategies.failure_kernel import hostile_failure_pnl

def hostile_failure_test_cached(worlds, exposure_scale=1.0, shock_scale=1.0):
    pnls = np.empty(len(worlds), dtype=np.float32)
    for i, w in enumerate(worlds):
        pnls[i] = hostile_failure_pnl(w, exposure_scale, shock_scale)
    return pnls

