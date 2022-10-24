#  code also runs in the virtual environment called "jupyter_in_class"
#  this code teaches you how to effectively use pytest
import pytest


@pytest.mark.parametrize("input_one,expected",
                         [(80, "Normal"),
                          (45, "Borderline Low"),
                          (30, "Low")])
def test_check(input_one, expected):
    from blood_calculator import check
    answer = check(input_one)
    assert answer == expected


@pytest.mark.parametrize("input_one,expected",
                         [(129, "Normal"),
                          (145, "Borderline High"),
                          (180, "High"),
                          (200, "Very High")])
def test_checkLDL(input_one, expected):
    from blood_calculator import checkLDL
    answer = checkLDL(input_one)
    assert answer == expected


@pytest.mark.parametrize("input_one,expected",
                         [(129, 'Normal'),
                          (205, 'Borderline High'),
                          (300, 'High')])
def test_check_TC(input_one, expected):
    from blood_calculator import check_TC
    answer = check_TC(input_one)
    assert answer == expected
