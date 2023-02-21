import pytest
from romantointeger.solution import Solution

@pytest.mark.parametrize("test_input, expected", [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)])
def test_solution(test_input, expected):
    solution = Solution()
    assert solution.roman_to_int(test_input) == expected