from src.String_calculator import Add


def test_function_is_callable():
 Add("0")

def test_empty_string_returns_zero():
    assert Add("") == 0
def test_1_returns_1():
    assert Add("1") == 1