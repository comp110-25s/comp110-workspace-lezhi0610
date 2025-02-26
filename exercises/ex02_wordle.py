"""A Wordle game containing loops."""

__author__: str = "730702700"


def contains_char(search: str, character: str) -> bool:
    """Check if a character is in a string."""
    assert len(character) == 1, f"len('{character}') is not 1"
    i: int = 0
    while i < len(search):
        if search[i] == character:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emojify the guess."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    result = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def input_guess(length: int) -> str:
    """Guess the word of expected length."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        print(f"That wasn't {length} chars! Try again:")
        guess = input(f"Enter a {length} character word: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    max_turns: int = 6
    while turn <= max_turns:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        result: str = emojified(guess, secret)
        print(result)
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        else:
            turn += 1
    if turn > max_turns:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
