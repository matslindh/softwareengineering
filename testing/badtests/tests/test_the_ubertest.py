from ..ourproject.twoer import is_two


def test_ubertest():
    assert is_two(2)
    assert not is_two(1)
    assert not is_two(4)
    assert not is_two(6)