"""File to define Fish class."""

__author__ = "730702700"


class Fish:
    """Class to define Fish"""

    age: int

    def __init__(self) -> None:
        """New fish with age 0"""
        self.age = 0

    def one_day(self) -> None:
        """Fish ages"""
        self.age += 1
