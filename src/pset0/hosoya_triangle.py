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
    triangle: list[list[int]] = []

    for i in range(n + 1):
        row: list[int] = []
        for k in range(i + 1):
            if i <= 1:
                row.append(1)
            elif k < i:
                above = triangle[i - 1][k]
                above2 = triangle[i - 2][k] if k <= i - 2 else 0
                row.append(above + above2)
            else:
                above = triangle[i - 1][k - 1]
                above2 = triangle[i - 2][k - 2] if k - 2 >= 0 else 0
                row.append(above + above2)
        triangle.append(row)

    return triangle
