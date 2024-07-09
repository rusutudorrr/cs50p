from plates import is_valid


def test_valid_plate_length():
    assert is_valid("AB123")  # Expected to be valid
    assert not is_valid("A")  # Too short, expected to be invalid
    assert not is_valid("ABCDEFGHI")  # Too long, expected to be invalid


def test_plate_starts_with_two_letters():
    assert is_valid("AB123")
    assert not is_valid("1AB23C")
    assert not is_valid("123ABC")


def test_no_leading_zero():
    assert is_valid("AB123")
    assert not is_valid("AB0123")


def test_no_non_alphanumeric_characters():
    assert is_valid("AB123")
    assert not is_valid("AB123!")
    assert not is_valid("AB 123")


def test_last_character_constraints():
    assert is_valid("AB123")
    assert not is_valid("AB123A")
    assert not is_valid("AB12B3")
