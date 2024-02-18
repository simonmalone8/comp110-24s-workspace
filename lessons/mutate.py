"""Mutating functions."""

__author__ = "730476889"


def manual_append(list: list[int], num: int) -> None:
    """Append the int to the end of the list."""
    list.append(num)


def double(list: list[int]) -> None:
    """Multiple all the values by 2."""
    i = 0
    while i <= len(list) - 1:
        list[i] *= 2
        i += 1

        
a: list[int] = [1, 2, 3, 4]


double(a)
print(a)