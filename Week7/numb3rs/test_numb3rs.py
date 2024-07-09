from numb3rs import validate


def test_validate_true():

    ip = '255.124.127.255'
    assert validate(ip) == True


def test_validate_false():
    ip = '512.412.814.512'
    assert validate(ip) == False


def test_valid_range():
    ip = '127.0.0.1'
    values = ip.split(".")
    if 0 <= all([int(i) for i in values]) <= 255:
        assert validate(ip) == True
