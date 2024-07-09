import pytest
from fuel import convert, gauge


def test_convert_valid_fraction():
    assert convert("1/2") == 50


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_full_denominator():
    assert convert("100/100") == 100


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"


def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("3/2")
