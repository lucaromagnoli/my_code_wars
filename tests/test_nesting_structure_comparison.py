import pytest
from code_wars.nesting_structure_comparison import same_structure_as


@pytest.mark.parametrize(
    "original, other, expected",
    [
        ([1, 1, 1], [2, 2, 2], True),
        ([1, [1, 1]], [2, [2, 2]], True),
        ([[[], []]], [[[], []]], True),
        ([1, [1, 1]], [[2, 2], 2], False),
        ([1, [1, 1]], [[2], 2], False),
        ([[[], []]], [[1, 1]], False),
        ([], [], True),
        ([], [1], False),
        ([1], [], False),
        ([[], []], [[], []], True),
        ([[], []], [[], [1]], False),
        ([1, "a", []], [2, "b", []], True),
        ([1, "a", []], [2, ["b"], []], False),
    ],
)
def test_same_structure_as(original, other, expected):
    assert same_structure_as(original, other) == expected
