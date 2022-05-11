"""
This file will contain the reusable functions of numbers

docstring: https://google.github.io/styleguide/pyguide.html
"""

def is_prime(number:int) -> bool:
    """
    This method will check if the number is prime or not

    Args:
      number: A positive integer.

    Returns:
      True if the number is prime false otherwise.

    Raises:
      ValueError: If the number is invalid.
    """
    for index in range(2, number//2 + 1):
        if number%index == 0:
            break
    else:
        return True
    return False

