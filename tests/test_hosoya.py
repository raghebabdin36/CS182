from pset0.hosoya import hosoya_triangle


def test_hosoya():
    assert hosoya_triangle(0) == [[1]]  # Remember, you must return a list of lists!
    assert hosoya_triangle(3) == [[1], [1, 1], [2, 1, 2], [3, 2, 2, 3]]
    assert hosoya_triangle(10) == [
        [1],
        [1, 1],
        [2, 1, 2],
        [3, 2, 2, 3],
        [5, 3, 4, 3, 5],
        [8, 5, 6, 6, 5, 8],
        [13, 8, 10, 9, 10, 8, 13],
        [21, 13, 16, 15, 15, 16, 13, 21],
        [34, 21, 26, 24, 25, 24, 26, 21, 34],
        [55, 34, 42, 39, 40, 40, 39, 42, 34, 55],
        [89, 55, 68, 63, 65, 64, 65, 63, 68, 55, 89],
    ]
