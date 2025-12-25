
import numpy as np
from scipy.interpolate import griddata

class TemplateSurface:
    def __init__(self, K, T, IV):
        self.K = K.flatten()
        self.T = T.flatten()
        self.IV = IV.flatten()

    def __call__(self, Kq, Tq):
        pts = np.column_stack([self.K, self.T])
        qry = np.column_stack([Kq.flatten(), Tq.flatten()])
        return griddata(pts, self.IV, qry, method='linear').reshape(Kq.shape)

