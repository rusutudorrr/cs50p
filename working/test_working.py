import pytest
from working import convert

@pytest.mark.parametrize("hour, expected_output", [
    ('9 AM to 5 PM', '09:00 to 17:00'),
    ('8:00 AM to 3:00 PM', '08:00 to 15:00'),
    ('10 AM to 6:30 PM', '10:00 to 18:30')
])
def test_valid_input(hour, expected_output):
    assert convert(hour) == expected_output

@pytest.mark.parametrize("hour", [
    '9AM to 5PM',
    ' to '
    '13 AM to 5 PM'
])
def test_invalid_input(hour):
    with pytest.raises(ValueError):
        convert(hour)
