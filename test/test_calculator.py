from calculator import square
import pytest

def main():
    test_square()


def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_string():
    with pytest.raises(TypeError):
        square("cat")


if __name__ == "__main__":
    main()