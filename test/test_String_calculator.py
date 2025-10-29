import pytest

from src.String_calculator import Add
@pytest.mark.parametrize("string, expected_result", [
    ("", 0),
    ("0", 0),
    ("1", 1),
    ("2", 2),
    ("3", 3),
    ("9", 9),
    ("1,2", 3),
    ("2,3", 5),
    ("5,5", 10),
    ("10,20", 30),
    ("7,8", 15),
    ("100,200", 300),
    ("99,1", 100),
])
def test_number_return_itself(string, expected_result):
    assert Add(string) == expected_result

