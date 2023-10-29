import math

def is_prime(n):
    """
    Check if a number is prime.

    This function takes an integer `n` as input and returns True if it's a prime number, or False if it's not.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the input is a prime number, False otherwise.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True