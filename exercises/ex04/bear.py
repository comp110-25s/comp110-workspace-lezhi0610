"""File to define Bear class."""

__author__ = "730702700"


class Bear:
    """Class to define Bear."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """New bear with age 0 and hunger score 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Bear ages and gets hungrier."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Bear eats fish."""
        self.hunger_score += num_fish
