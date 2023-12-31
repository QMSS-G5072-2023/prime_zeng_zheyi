from src.prime_zz3155.is_prime import is_prime

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(17) == True
    assert is_prime(18) == False