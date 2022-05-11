from activities.numbers import is_prime

def test_is_prime():
    """
    This function will test if the number is prime or not
    """
    assert is_prime(7) == True
    assert is_prime(8) == False


