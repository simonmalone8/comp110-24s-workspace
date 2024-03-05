"""Splitting a dictionary into two lists."""


__author__ = "730476889"


def get_keys(para: dict[str, int]) -> list[str]:
    """Writing a function that will return keys."""
    keys = list(para.keys())
    return keys


args = {"comp": 110, "march": 2024, "junior": 3}
keys = get_keys(args)
print(keys)


def get_values(para: dict[str, int]) -> list[int]:
    """Writing a function that will return values."""
    values = list(para.values())
    return values


args = {"comp": 110, "march": 2024, "junior": 3}
values = get_values(args)
print(values)