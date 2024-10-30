import pytest

def multiple_of_two(num):
    if num == 0:
        raise(ValueError)
    return num % 2 == 0


def get_lenght(string):
    return len(string)


def gen_sequence(n):
    return list(range(1, n+1))


def test_numbers():
    assert multiple_of_two(4) is True
    assert multiple_of_two(5) is False
    assert multiple_of_two(8) is True


def test_zero():
    with pytest.raises(ValueError):
        multiple_of_two(0)


@pytest.mark.skip
def test_get_len():
    assert get_lenght("123") == 3


@pytest.mark.skipif('2 * 2 == 4')
def test_get_lenght2():
    assert get_lenght("") == 0


@pytest.mark.xfail
def test_gen_sequence():
    assert gen_sequence(-1)
