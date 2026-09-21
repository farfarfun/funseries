import pytest

from funseries.experiment.prime import is_prime, is_prime2, prime_generate


def test_prime_functions():
    assert is_prime(2)
    assert is_prime(97)
    assert not is_prime(1)
    assert is_prime2(97)
    assert not is_prime2(91)


def test_prime_generate_boundaries():
    assert prime_generate(5, 20) == [2, 3, 5, 7, 11]
    with pytest.raises(ValueError):
        prime_generate(-1)
