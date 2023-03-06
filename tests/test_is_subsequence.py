import pytest
from issubsequence.solution import Solution

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("s, t, expected", [("abc", "ahbgdc", True), ("axc", "ahbgdc", False), ("bb", "ahbgdc", False)])
def test_solution(solution, s, t, expected):
    assert solution.is_subsequence(s, t) == expected


def test_simple_case(solution):
    assert solution.is_subsequence("abc", "abc") == True


def test_substring_longer_than_string(solution):
    assert solution.is_subsequence("abcdef", "abc") == False


def test_empty_string(solution):
    assert solution.is_subsequence("abc", "") == False


def test_both_strings_empty(solution):
    assert solution.is_subsequence("", "") == True
