from typing import List

def compute_squares(nums: List[int]) -> List[int]:
    """
    Given a list of integers, returns a new list containing the square of each number.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        List[int]: A list containing the squares of the input integers.
    """
    squares = []
    for n in nums:
        squares.append(n * n)
    return squares


#Func call:
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print("Squares of list1:", compute_squares(list1))
print("Squares of list2:", compute_squares(list2))
