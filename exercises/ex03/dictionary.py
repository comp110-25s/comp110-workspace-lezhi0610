"""Dictionary functions for EX03."""

__author__: str = "730702700"


def invert(input1: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary."""
    output1 = {}
    for key, value in input1.items():
        if value in output1:
            raise KeyError(f"Duplicate key: {value}")
        else:
            output1[value] = key
    return output1


def count(input2: list[str]) -> dict[str, int]:
    """Count the occurrences of each element in a list."""
    output2 = {}
    for item in input2:
        if item in output2:
            output2[item] += 1
        else:
            output2[item] = 1
    return output2


def favorite_color(input3: dict[str, str]) -> str:
    """Returns the most frequent color in a dictionary."""
    color_counts = count(list(input3.values()))
    max_count = max(color_counts.values())
    for color in input3.values():
        if color_counts[color] == max_count:
            return color
    return ""


def bin_len(input4: list[str]) -> dict[int, set[str]]:
    """Group strings by length."""
    output4 = {}
    for item in input4:
        if len(item) in output4:
            output4[len(item)].add(item)
        else:
            output4[len(item)] = {item}
    return output4
