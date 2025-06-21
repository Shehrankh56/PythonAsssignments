 #Part 1: Convert to function with type hints

def compute_squares(nums: list[int]) -> list[int]:
    """
    Given a list of integers, return a list containing their squares.
    """
    squares = []
    for n in nums:
        squares.append(n * n)
    return squares

# eg:
print(compute_squares([1, 2, 3, 4, 5]))
print(compute_squares([10, -3, 0]))