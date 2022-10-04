from ..ourproject.twoer import is_two


def test_1():
    assert is_two(2)


def test_2():
    assert not is_two(1)
    assert not is_two(3)
    assert not is_two(4)


def test_3():
    pass