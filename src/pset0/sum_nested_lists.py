type NestedIntList = list[int | NestedIntList]


def sum_nested_lists(input_list: NestedIntList) -> int:
    """
    Recursively sums integers within a nested structure of lists.

    Parameters:
        `input_list`: A list containing integers and other nested lists.

    Returns:
        The sum of all integers within the nested integer list.

    Example:
        sum_nested_lists([1, 2, [3, 4], [[5], 6, 7]]) -> 28
        sum_nested_lists([[1, 2], [[3]], 5, 6]) -> 17
    """
    total = 0
    for item in input_list:
        if isinstance(item, list):
            total += sum_nested_lists(item)
        else:
            total += item
    return total
