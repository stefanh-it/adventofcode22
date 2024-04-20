def process_rows(lines: list) -> int:
    score: int = 0
    for row in lines:
        for i, _ in enumerate(row, 4):
            set_4 = set(row[i-4:i])
            if len(set_4) == 4:
                score += i
                break
    return score


def main(data):
    """Main Entry."""
    rows = data.splitlines()
    score = process_rows(rows)
    return score


if __name__ == "__main__":
    main('**kwargs')
