"""Comparison of the recursive and dynamic programming approaches."""
from typing import Optional

def climb_stairs_recursive(n: int) -> int:
    """Recursive approach"""
    if n <= 2:
        return n  # Base cases: 1 way for 1 step, 2 ways for 2 steps
    # To reach step n, we can come from step (n-1) or step (n-2)
    return climb_stairs_recursive(n-1) + climb_stairs_recursive(n-2)


def climb_stairs_memo(n: int, memo: Optional[dict[int, int]] = None) -> int:
    """Dynamic programming with memoization"""
    if memo is None:
        memo = {}

    # Check if we've already calculated this value
    if n in memo:
        return memo[n]  # Return cached result - O(1) lookup!

    # Base cases
    if n <= 2:
        return n

    # Calculate once and store in memo for future use
    memo[n] = climb_stairs_memo(n-1, memo) + climb_stairs_memo(n-2, memo)
    return memo[n]
# Try them out.
print(climb_stairs_recursive(5))
print(climb_stairs_recursive(5))
