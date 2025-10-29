import pytest

from src.String_calculator import Add
@pytest.mark.parametrize("string, expected_result", [
    ("", 0),
    ("1", 1),
    ("2", 2),
    ("1,2", 3),
    ("2,3", 5),
    ("5,5", 10),
    ("3", 3)
])
def test_number_return_itself(string, expected_result):
    assert Add(string) == expected_result

