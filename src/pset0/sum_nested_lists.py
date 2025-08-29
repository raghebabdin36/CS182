from __future__ import annotations
from typing import Protocol, runtime_checkable, Self


@runtime_checkable
class SupportsAdd(Protocol):
    def __add__(self, other, /) -> Self: ...


def sum_nested_lists(input_list: list[SupportsAdd]) -> int:
    """
    Recursively sums items within a nested structure of lists.

    Parameters:
        input_list (list[SupportsAdd]): A nested list structure containing integers and/or other lists.

    Returns:
        int: The sum of all integers within the nested lists.

    Example:
        sum_nested_lists([1, 2, [3, 4], [[5], 6, 7]]) -> 28
        sum_nested_lists([[1, 2], [[3]], 5, 6]) -> 17
    """
    #### YOUR CODE HERE ####
    raise NotImplementedError
