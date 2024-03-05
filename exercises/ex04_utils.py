"""Ex04 Utils."""


__author__ = "730476889"


def all(numbers_one: list[int], numbers_two: int) -> bool:
    """Checking if all the ints in the list are the same."""
    i: int = 0
    if len(numbers_one) == 0:
        return False
    while i < len(numbers_one):
        if numbers_two != numbers_one[i]:
            return False
        i += 1
    return True


def max(numbers_one: list[int]) -> int:
    """Finding the max in a list of ints."""
    if len(numbers_one) == 0:
        raise ValueError("numbers_One() arg is an empty List")
    i: int = 0
    value_of_max: int = numbers_one[0]
    while i < len(numbers_one):
        if numbers_one[i] > value_of_max:
            value_of_max = numbers_one[i]
        i += 1
    return value_of_max
    
    
def is_equal(numbers_one: list[int], numbers_two: list[int]) -> bool:
    """Checking if two seperate lists of ints are equal."""
    if len(numbers_one) != len(numbers_two):
        return False
    i: int = 0
    while i < len(numbers_one):
        if numbers_one[i] != numbers_two[i]:
            return False
        i += 1
    return True


def extend(numbers_one: list[int], numbers_two: list[int]) -> None:
    """Adds/Extends to seperate lists of ints together."""
    for number in numbers_two:
        numbers_one.append(number)