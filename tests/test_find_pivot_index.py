import pytest
from findpivotindex.solution import Solution


@pytest.mark.parametrize("test_input, expected", [([1,7,3,6,5,6], 3), ([1,2,3], -1), ([2,1,-1], 0)])
def test_solution(test_input, expected):
    solution = Solution()
    assert solution.pivot_index(test_input) == expected