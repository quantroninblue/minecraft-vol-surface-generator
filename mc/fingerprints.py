import numpy as np

def extract_fingerprints(worlds, pnls):
    feats = []
    labels = []

    for w, pnl in zip(worlds, pnls):
        IV = w["IV"]
        K = w["K"]
        T = w["T"]

        # ATM columns
        k_mid = IV.shape[1] // 2
        t_short = 1

        # Geometry metrics
        skew = np.gradient(IV[t_short, :], K[0, :])[k_mid]
        convex = np.mean(np.gradient(np.gradient(IV[t_short, :], K[0, :]), K[0, :]))
        tail_density = np.mean(IV > np.percentile(IV, 92))

        feats.append([skew, convex, tail_density])
        labels.append(pnl)

    return np.array(feats), np.array(labels)
