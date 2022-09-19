#code also runs in the virtual environment called "jupyter_in_class"
#this code teaches you how to effectively use pytest
import pytest
@pytest.mark.parametrize("input_one,expected",
    [(80,"Normal"),
    (45,"Borderline Low"),
    (30,"Low")])

def test_check(input_one,expected):
    from blood_calculator import check
    answer = check(input_one)
    assert answer == expected

  



"""
def test_check_BorderlineLow():
    from blood_calculator import check
    answer = check(45)
    expected = "Borderline Low"
    assert answer == expected

def test_check_Low():
    from blood_calculator import check
    answer = check(30)
    expected = "Low"
    assert answer == expected

"""