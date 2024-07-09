import pytest
from seasons import seasons_of_love, is_leap_year


def test_is_leap_year():
    assert is_leap_year(2020) == True
    assert is_leap_year(2021) == False


def test_seasons_of_love_correct_input(monkeypatch, capfd):
    # monkeypatch correct user input
    monkeypatch.setattr('builtins.input', lambda x:"2020-01-01")

    seasons_of_love()

    # capture printed output
    out, error = capfd.readouterr()

    # update expected output to match actual output
    assert "Two million, seventy-two thousand, one hundred sixty minutes" in out


def test_seasons_of_love_incorrect_input(monkeypatch):
    # monkeypatch incorrect user input
    monkeypatch.setattr('builtins.input', lambda x:"incorrect-date-format")

    with pytest.raises(SystemExit):
        seasons_of_love()
