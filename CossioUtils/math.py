from math import isclose


def approx(*x, abs_tol=1e-10, rel_tol=1e-3):
    """
    Tests whether the values given are approximately equal.
    """
    if x == None:
        return True
    for xx in x:
        for yy in x:
            if not isclose(xx, yy, abs_tol=abs_tol, rel_tol=rel_tol):
                return False
    return True
