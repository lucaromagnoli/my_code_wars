import pytest
from kata.eval_expression import calc

@pytest.mark.parametrize("expression, expected", [
    ("1 + 1", 2),
    ("8/16", 0.5),
    ("3 -(-1)", 4),
    ("2 + -2", 0),
    ("10- 2- -5", 13),
    ("(((10)))", 10),
    ("3 * 5", 15),
    ("-7 * -(6 / 3)", 14)
])
def test_calc(expression, expected):
    assert calc(expression) == expected