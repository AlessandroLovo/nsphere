import numpy as np


def i_d(x: float, d: int) -> float:
    '''
    Computes the integral between 0 and `x` of (sin(x))^d

    Parameters
    ----------
    x : float
    d : int
    '''
    # print(d)
    if d == 0:
        return x
    elif d == 1:
        return 1. - np.cos(x)
    else:
        return ((d - 1)*i_d(x, d - 2) - np.cos(x)*np.sin(x)**(d - 1))/d

class Handler(object):
    def __init__(self, d: int):
        self.d = d

        self.i_max = i_d(np.pi, self.d)

    def i(self, x: float) -> float:
        return i_d(x, self.d)/self.i_max

    @np.vectorize
    def get_theta(self, h: float) -> float:
        if h <= 0:
            return 0.
        if h >= 1:
            return np.pi

        guess = np.pi/2
        jump = np.pi/2

        

        




def sphere_from_angles(angles):
    '''
    Computes the cartesian coordinates of a point on the surface of an N-dimensional unit sphere from N-1 angles.

    Parameters
    ----------
    angles : array-like of length N - 1
        Array of angles: the last one has to be in [0, 2*pi], while all the others in [0, pi]

    Returns
    -------
    np.ndarray of length N
        Cartesian coordinates
    '''
    n = len(angles)
    x = np.zeros(n + 1)
    c = 1.
    for i in range(n):
        x[i] = c*np.cos(angles[i])
        c *= np.sin(angles[i])
    x[-1] = c

    return x
