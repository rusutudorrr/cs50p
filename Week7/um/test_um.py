from um import count


def test_valid_input():
    im = 'um this is fine, Um..'
    assert count(im) == 2


def test_no_um():
    im = 'umbrella, UMbrella, Umbrella, uMbrella'
    assert count(im) == 0
