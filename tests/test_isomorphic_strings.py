import pytest
from isomorphicstrings.solution import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s, t, expected",
    [("egg", "add", True), ("foo", "bar", False), ("paper", "title", True)],
)
def test_solution(solution, s, t, expected):
    assert solution.isIsomorphic(s, t) == expected


def test_reestablish_same_mapping(solution):
    solution.mapping = {"a": "b"}
    assert solution.establish_mapping("a", "b") == True


def test_map_already_exsistent_letter(solution):
    solution.mapping = {"a": "b"}
    assert solution.establish_mapping("a", "c") == False


def test_no_two_characters_map_the_same_character(solution):
    solution.mapping = {"a": "b"}
    assert solution.establish_mapping("c", "b") == False
