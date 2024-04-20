def ranges_overlap(range1, range2):
    return range1[0] <= range2[1] and range2[0] <= range1[1]


def find_overlap(range1, range2):
    if ranges_overlap(range1, range2):
        return range(max(range1[0], range2[0]), min(range1[1], range2[1])+1)
    else:
        return None

def create_ranges(pairs) -> int:
    score: int = 0
    for pair in pairs:
        p1, p2 = pair.split(",")
        p1s, p1e = map(int, p1.split("-"))
        p2s, p2e = map(int, p2.split("-"))
        p1range = [p1s, p1e]
        p2range = [p2s, p2e]
        overlap = find_overlap(p1range, p2range)
        if overlap:
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
