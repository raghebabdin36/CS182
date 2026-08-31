def print_hosoya_triangle(rows: list[list[int]]):
    """
    Prints a Hosoya Triangle in a readable format.

    Parameters:
        `rows`: A Hosoya Triangle as a two-dimensional list.
    """
    largest_length = len(str(rows[-1]))
    for row_idx, row in enumerate(rows):
        current_row_length = len(str(row))
        print(f"[{row_idx}]{' ' * ((largest_length - current_row_length) // 2)}{row}")


def hosoya_triangle(n: int) -> list[list[int]]:
    """
    Generates the first `n + 1` rows of Hosoya's Triangle.

    Parameters:
        `n`: The depth of the triangle (0-indexed). Must be non-negative.

    Returns:
        A two-dimensional list with the first `n + 1` rows of Hosoya's
        Triangle.

    Example:
        hosoya_triangle(0) -> [[1]]
        hosoya_triangle(3) -> [[1], [1, 1], [2, 1, 2], [3, 2, 2, 3]]
    """
    raise NotImplementedError
