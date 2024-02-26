"""Summing the elements of a list using different loops."""

__author__ = "730476889"


def w_sum(vals: list[float]) -> float:
    """Sums up all of the values in the list."""
    total_number = 0.0
    i = 0
    while i < len(vals):
        total_number += vals[i]
        i += 1
    return total_number


answer = w_sum([3.2, 5.6, 8.2])
print(answer)


def f_sum(vals: list[float]) -> float:
    """Sums up all of the values in the list."""
    total_number = 0.0
    for value in vals:
        total_number += value
    return total_number


answer2 = f_sum([8.2, 4.3, 6.1])
print(answer2)


def f_range_sum(vals: list[float]) -> float:
    """Sums up all of the values in the list."""
    total_number = 0.0
    for value in range(len(vals)):
        total_number += vals[value]
    return total_number


result3 = f_range_sum([9.0, 4.2, 6.2])
print(result3)