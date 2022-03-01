import numpy as np

def am(x):
    """ Arithmetic mean """
    n = len(x)
    xam = 1/n*(np.sum(x))
    return xam
def gm(x):
    """ Geometric mean """
    n = len(x)
    xgm = np.prod(x)**(1/n)
    return xgm
def hm(x):
    """ Harmonic mean """
    n = len(x)
    xhm = n/(np.sum(1/x))
    return xhm