
def compute_factorial(n: int):
    """
    Compute the n!
    """
    if n in [0, 1]:
        return 1
    return n*compute_factorial(n-1)


def compute_fibonnaci(n: int):
    """
    Compute the nth term in the fibonacci sequence.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return compute_fibonnaci(n-2) + compute_fibonnaci(n-1)


def reverse_string(string: str):
    """
    Recursive implementation of reversing a string.
    """
    if string is None:
        return
    if len(string) == 1:
        return string[0]
    return reverse_string(string[1:]) + string[0]


def print_array(array: list):
    """
    Print elements of an array using recursion.
    """
    if array == []:
        return

    print(array[0])
    print_array(array[1:])


def raise_to_power(a: int, b: int):
    """
    Raise a to the power of b.
    """
    if b == 0:
        return 1
    b -= 1
    return a*raise_to_power(a, b)


def is_palindrome(string: str):
    """
    Determine if a string is a palindrome using recursion.
    """
    if string == '':
        return True
    first, last = string[0], string[-1]
    return (first == last) and is_palindrome(string[1:-1])


def pascal_triangle(n: int):
    """
    Print pascal's triangle for n rows
    """
    def moving_sum(arr: list):
        """moving sum sub-routine"""
        n = len(arr)
        if n <= 1:
            return arr
        out = []
        for i in range(0, n-1):
            out.append(arr[i]+arr[i+1])
        return out

    if n == 0:
        row = [1]
    if n == 1:
        row = [1, 1]
    else:
        row = [1] + moving_sum(pascal_triangle(n-1)) + [1]
    print(row)
    return row
