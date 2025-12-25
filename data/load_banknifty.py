import pandas as pd

def load_iv_snapshot(path, spot):
    df = pd.read_csv(path)

    K = df["strike"].values / spot
    T = df["expiry_days"].values
    IV = df["iv"].values

    return K, T, IV
