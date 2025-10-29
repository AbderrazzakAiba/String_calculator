from src.String_calculator import Add


def test_function_is_callable():
 Add("numbers")

def test_empty_string_returns_zero():
    assert Add("") == 0