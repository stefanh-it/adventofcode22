"Advent of Code Day 8 - p1."

def main(data):
    """Main Entry."""
    total_sum = 0
    rows = data.splitlines()
    columns = create_columns(rows)
    score = get_visible(rows, columns)
    width = (len(rows[0]) - 1) * 2
    height = (len(columns[0]) - 1) * 2
    score += width + height
    return score


if __name__ == "__main__":
    main('**kwargs')
