"""Functions that implement sorting algorithms."""

__author__ = "730476889"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm."""
    for i in range(1, len(x)):
        value = x[i]
        unsorted = i
        while unsorted > 0 and x[unsorted - 1] > value:
            x[unsorted] = x[unsorted - 1]
            unsorted -= 1
        x[unsorted] = value
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm.""" 
    i = 0  
    while i < len(x):
        minimum_num = i
        smallest_num = False
        j = i + 1  
        while j < len(x):
            if x[j] < x[minimum_num]:
                minimum_num = j
                smallest_num = True
            j += 1
        if smallest_num:
            temporary = x[i]
            x[i] = x[minimum_num]
            x[minimum_num] = temporary
        i += 1 
    return None
    