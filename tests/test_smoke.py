import pytest

from funseries.experiment.prime import is_prime, is_prime2, prime_generate


def test_prime_functions():
    assert is_prime(2)
    assert is_prime(97)
    assert not is_prime(1)
    assert is_prime2(97)
    assert not is_prime2(91)


@pytest.mark.parametrize(("n", "trials"), [(1, 10), (0, 10), (-1, 10), (3, 0)])
def test_is_prime2_rejects_invalid_arguments(n, trials):
    with pytest.raises(ValueError):
        is_prime2(n, trials)


def test_prime_generate_boundaries():
    assert prime_generate(5, 20) == [2, 3, 5, 7, 11]
    assert prime_generate() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert prime_generate(0) == []
    assert prime_generate(10, 2) == [2]
    assert prime_generate(10, 10) == [2, 3, 5, 7]
    with pytest.raises(ValueError):
        prime_generate(-1)
    with pytest.raises(ValueError):
        prime_generate(max_value=1)
