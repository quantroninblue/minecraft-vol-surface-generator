import numpy as np

def lerp(a, b, t):
    return a + t * (b - a)

def fade(t):
    return 6*t**5 - 15*t**4 + 10*t**3

def gradient(h, x, y):
    vectors = np.array([[0,1],[0,-1],[1,0],[-1,0]])
    g = vectors[h % 4]
    return g[:, :, 0] * x + g[:, :, 1] * y

def perlin(x, y, seed=0):
    np.random.seed(seed)

    xi = x.astype(int)
    yi = y.astype(int)

    xf = x - xi
    yf = y - yi

    u = fade(xf)
    v = fade(yf)

    perm = np.arange(256)
    np.random.shuffle(perm)
    perm = np.stack([perm, perm]).flatten()

    aa = perm[perm[xi % 256] + yi % 256]
    ab = perm[perm[xi % 256] + (yi + 1) % 256]
    ba = perm[perm[(xi + 1) % 256] + yi % 256]
    bb = perm[perm[(xi + 1) % 256] + (yi + 1) % 256]

    x1 = lerp(gradient(aa, xf, yf), gradient(ba, xf - 1, yf), u)
    x2 = lerp(gradient(ab, xf, yf - 1), gradient(bb, xf - 1, yf - 1), u)

    return lerp(x1, x2, v)
