import math
import numpy as np


def LinEx(y: int, est: int):
    """
    A function that return the error for a given estimation of the number of calls
    :param y: truth
    :param est: estimation (ŷ in the folowing formula)
    :return: LinEx(y, ŷ) = exp[α(y − ŷ)] − α(y − ŷ) − 1
    """
    alpha = 0.1
    prod = alpha * (y - est)
    return math.exp(prod) - prod - 1


def get_error(ys: np.array, ests: np.array):
    """
    A function that calculates the average error over a set of estimations
    :param ys: a numpy array with shape (n,1)
    :param ests: a numpy array with shape (n,1)
    :return: the average error
    """
    n = ests.shape[0]
    assert n == ys.shape[0]

    sum_errors = 0.
    i = 0
    while i < n:
        error = LinEx(ys[i], int(3*ests[i]))
        # print(error)
        sum_errors += error
        i += 1

    #print(sum_errors/n)

    return sum_errors / n


def test():
    y = np.array([[2], [0], [1], [2], [1]])
    est = np.array([[3], [0], [1], [1], [1]])

    print(y.shape)

    print(get_error(y, est))
    L


if __name__ == "__main__":
    test()
