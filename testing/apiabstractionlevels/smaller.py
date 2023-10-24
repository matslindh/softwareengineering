def is_valid_username(username: str):
    if not username:
        return False

    if not isinstance(username, str):
        return False

    if len(username) < 5:
        return False

    return True


def test_empty_usernames_are_not_valid():
    assert not is_valid_username("")


def test_non_string_usernames_are_not_valid():
    assert not is_valid_username(123)


def test_usernames_must_have_a_minimum_length():
    assert not is_valid_username("foo")
    assert not is_valid_username("spam")  # grenseverdi


def test_valid_usernames_are_accepted():
    assert is_valid_username("foobar")
    assert is_valid_username("fooba")  # grenseverdi


