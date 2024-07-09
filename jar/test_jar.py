from jar import Jar
import pytest

def test_init():
    # test initialization with valid capacity
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    # test initialization with invalid capacity
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("5")

def test_str():
    jar = Jar(12)
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪" * 12

def test_deposit():
    jar = Jar(5)
    jar.deposit(1)
    assert jar.size == 1

    # test deposit exceeds capacity
    with pytest.raises(ValueError):
        jar.deposit(5)

    # test deposit negative number
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size == 4

    # test withdraw more cookies than are in the jar
    with pytest.raises(ValueError):
        jar.withdraw(5)

    # test withdraw negative number
    with pytest.raises(ValueError):
        jar.withdraw(-1)
