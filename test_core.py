from core import calculator
from core import is_prime
from core import add_frac

def test_calculator():
	assert calculator(2,2) == [4,0,1,4]


def test_is_prime():
    
    primes = [2,3,5,13,7,59,97]
    for prime in primes:
        assert is_prime(prime) == True
    assert is_prime(8) == False
    
def test_add_frac():
    result = [6,8]
    assert add_frac(1,2,1,4) == result