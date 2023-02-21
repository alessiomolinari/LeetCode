from runningsum1darray.solution import Solution
import pytest


@pytest.mark.parametrize("test_input, expected", [([1,2,3,4], [1,3,6,10]), ([1,1,1,1], [1,2,3,4]), ([3,1,2,10,1], [3,4,6,16,17])])
def test_solution(test_input, expected):
    solution = Solution()
    assert solution.runningSum(test_input) == expected