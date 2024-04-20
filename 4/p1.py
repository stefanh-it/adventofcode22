def create_ranges(pairs) -> int:
    score: int = 0
    for pair in pairs:
        p1, p2 = pair.split(",")
        p1s, p1e = map(int, p1.split("-"))
        p2s, p2e = map(int, p2.split("-"))
        if (p1s <= p2s and p1e >= p2e) \
                or p2s <= p1s and p2e >= p1e:
            score += 1
    return score


def main(data):
    """Main Entry."""
    score: int = 0
    pairs = data.splitlines()
    score = create_ranges(pairs)
    return score


if __name__ == "__main__":
    main('**kwargs')
