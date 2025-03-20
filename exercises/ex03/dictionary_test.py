"""Unit tests for dictionary functions."""

__author__: str = "730702700"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest


# test for invert
def test_invert1() -> None:
    """Use case"""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert2() -> None:
    """Use case"""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert3() -> None:
    """Edge case"""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


# test for count
def test_count1() -> None:
    """Use case"""
    assert count(["apple", "banana", "apple", "milk", "banana", "banana"]) == {
        "apple": 2,
        "banana": 3,
        "milk": 1,
    }


def test_count2() -> None:
    """Edge case"""
    assert count([]) == {}


def test_count3() -> None:
    """Use case"""
    assert count(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}


# test for favorite_color
def test_favorite_color1() -> None:
    """Use case"""
    assert favorite_color({"Stella": "pink", "Kevin": "red", "Coco": "pink"}) == "pink"


def test_favorite_color2() -> None:
    """Use case"""
    assert favorite_color({"Stella": "green"}) == "green"


def test_favorite_color3() -> None:
    """Edge case"""
    assert (
        favorite_color({"A": "red", "B": "blue", "C": "red", "D": "blue", "E": "pink"})
        == "red"
    )


# test for bin_len
def test_bin_len1() -> None:
    """Use case"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len2() -> None:
    """Use case"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len3() -> None:
    """Edge case"""
    assert bin_len([]) == {}
