from Week5.twttr import shorten
import pytest


def test_removed_vowels():
    assert shorten("cat") == "ct"
    assert shorten("mammal") == "mmml"


def test_capitalized_vowels():
    assert shorten("ENIGMA") == "NGM"


def test_punctuation():
    assert shorten("Great Scott!") == "Grt Sctt!"


def test_numbers_string():
    assert shorten("123456") == "123456"


def test_consonant_words():
    assert shorten("rhythms") == "rhythms"
    assert shorten("flyby") == "flyby"


def test_multiple_words():
    assert shorten("cat and dog") == "ct nd dg"
