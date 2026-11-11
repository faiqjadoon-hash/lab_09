from lab09 import two_sum, max_profit, max_subarray, is_balanced


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([]) == 0
    assert max_profit([1, 2]) == 1


def test_max_subarray():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1, -2, -3]) == -1


# STRETCH (optional) - skipping this still passes the three problems above.
def test_is_balanced():
    assert is_balanced("()")
    assert is_balanced("()[]{}")
    assert is_balanced("{[]}")
    assert is_balanced("")
    assert not is_balanced("(]")
    assert not is_balanced("([)]")
    assert not is_balanced("(")
    assert not is_balanced("]")
