import numpy as np
import pickle
import os

def save_worlds(worlds, name="worldlib.pkl"):
    os.makedirs("worldlibs", exist_ok=True)
    path = os.path.join("worldlibs", name)
    with open(path, "wb") as f:
        pickle.dump(worlds, f, protocol=pickle.HIGHEST_PROTOCOL)
    return path

def load_worlds(name="worldlib.pkl"):
    path = os.path.join("worldlibs", name)
    with open(path, "rb") as f:
        return pickle.load(f)
