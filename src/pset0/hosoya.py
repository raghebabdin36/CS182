def print_hosoya_triangle(triangle_rows: list[list[int]]):
    """
    Prints out a Hosoya Triangle to the console in a readable format

    Parameters:
        triangle_rows (list[list[int]]): The Hosoya Triangle to print
    """
    largest_length = len(str(triangle_rows[-1]))
    for row_idx, row in enumerate(triangle_rows):
        current_row_length = len(str(triangle_rows[row_idx]))
        print(f"[{row_idx}]{' ' * ((largest_length - current_row_length) // 2)}{row}")


def hosoya_triangle(n: int) -> list[int]:
    """
    Generates the first `n + 1` rows of Hosoya's Triangle.
    Each number is the sum of the two numbers above in either the left or right diagonal.
    https://en.wikipedia.org/wiki/Hosoya%27s_triangle

    Parameters:
        n (int): The depth of the triangle (0-indexed). Must be >= 0.

    Returns:
        list[list[int]]: A list of lists representing the first `n` rows of Hosoya's Triangle.

    Example:
        hosoya_triangle(0) -> [[1]]
        hosoya_triangle(3) -> [[1], [1, 1], [2, 1, 2], [3, 2, 2, 3]]
    """

    raise NotImplementedError
