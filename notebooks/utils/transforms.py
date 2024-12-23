import numpy as np

def deg2grad(degree: int | float) -> float:
    """
    Converts degree to radians.

    Parameters
    ----------
        degree : float

    Returns
    -------
        Degree converted to radians
    """
    return np.multiply(degree, np.pi / 180.)