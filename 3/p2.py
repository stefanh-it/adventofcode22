def calculate_score(overlaps) -> int:
    """Get the score from the hashmap"""
    score: int = 0
    score_dict = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52
    }
    for overlap in overlaps:
        for char in overlap:
            score += score_dict[char]
    return score


def chunks(lst: list, n: int):
    """Yield even chunks of n."""
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


def get_overlap(games) -> list:
    """Get char to compare against."""
    overlaps: list = []
    overlap: set
    groups: list = []
    groups = list(chunks(games, 3))
    for group in groups:
        p1, p2, p3 = set(group[0]), set(group[1]), set(group[2])
        overlap = p1 & p2 & p3
        overlaps.append(overlap)
    return overlaps


def main(data):
    """Main Entry."""
    score: int = 0
    overlaps: list = []
    games = data.splitlines()
    overlaps = get_overlap(games)
    score = calculate_score(overlaps)
    return score


if __name__ == "__main__":
    main('**kwargs')

