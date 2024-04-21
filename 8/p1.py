"Advent of Code Day 8 - p1."


def get_visible(rows: list, cols: list) -> int:
    score: int = 0
    y = 1
    while y < len(rows) - 1:
        row = list(rows[y])
        x = 1
        while x < len(row) - 1:
            print(row[x])

            # Main Logic

            height = int(row[x])
            # print(f"Row val left to check {row[:x]}")
            # print(f"Row val right to check {row[x+1:]}")
            # print(f"Col val up to check {cols[x][:y]}")
            # print(f"Col val down to check {cols[x][y+1:]}")
            left, right = row[:x], row[x+1:]
            up, down = cols[x][:y], cols[x][y+1:]
            to_check = [left, right, up, down]
            max_values = list(map(max, to_check))
            # print(max_values)
            if int(min(max_values)) < height:
                score += 1
            x += 1
        y += 1
    return score


def create_columns(rows):
    "Create a list of columns"
    num_cols = len(rows[0])
    columns = []
    for _ in range(num_cols):
        columns.append([])
    for row in rows:
        for col_index, height in enumerate(row):
            columns[col_index].append(height)

    return columns


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
