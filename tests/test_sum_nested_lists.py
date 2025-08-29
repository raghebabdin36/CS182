from pset0.sum_nested_lists import sum_nested_lists


def test_sum_nested():
    assert sum_nested_lists([1, 2, [3, 4], [[5], 6, 7]]) == 28
    assert sum_nested_lists([[1, 2], [[3]], 5, 6]) == 17
    assert sum_nested_lists([2, 4, 6]) == 12
    assert sum_nested_lists([]) == 0
    assert sum_nested_lists([[[[[[[[4]]]]]]]]) == 4
