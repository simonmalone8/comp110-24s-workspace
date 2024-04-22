"""CQ07."""


__author__ = "730476889"


def f(n: int, k: int) -> int:
    """This function will return n x k."""
    if n == 0:
        return 0
    else:
        return f(n - 1, k) + k
