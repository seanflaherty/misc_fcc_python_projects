import pytest
import sys
from src.count_up import countup

@pytest.mark.parametrize(
    "input_val, expected",
    [
        # Standard positive cases
        (5, [1, 2, 3, 4, 5]),
        (3, [1, 2, 3]),
        (1, [1]),

        # Base case & boundary conditions (< 1)
        (0, []),
        (-1, []),
        (-100, []),

        # Float support (decrements until < 1)
        (3.5, [1.5, 2.5, 3.5]),
    ],
    ids=[
        "standard-5",
        "standard-3",
        "single-element",
        "zero-base-case",
        "negative-one",
        "large-negative",
        "float-input",
    ]
)
def test_countup_valid_inputs(input_val, expected):
    """Verify countup produces correct ascending lists for valid inputs."""
    assert countup(input_val) == expected


def test_countup_type_error():
    """Verify TypeError is raised when passing non-numeric types."""
    with pytest.raises(TypeError):
        countup("5")  # String comparison fails on `number < 1`


def test_countup_recursion_limit():
    """Verify RecursionError occurs when exceeding Python's call stack depth."""
    limit = sys.getrecursionlimit() + 100
    with pytest.raises(RecursionError):
        countup(limit)