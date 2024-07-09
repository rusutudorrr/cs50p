from bank import value

def test_zero_dollars():
    assert value("Hello") == 0
    assert value(" Hello ") == 0
    assert value("Hello, Newman") == 0

def test_20_dollars():
    assert value("How you doing?") == 20

def test_100_dollars():
    assert value("What's happening?") == 100
c