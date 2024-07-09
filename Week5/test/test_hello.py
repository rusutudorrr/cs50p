from Week5.hello import hello


def test_default():
    assert hello() == "hello, world"


def test_argument():
    for name in ["Tudor", "Dan", "Teo"]:
        assert hello(name) == f"hello, {name}"