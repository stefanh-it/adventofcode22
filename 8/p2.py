"Advent of Code Day 8 - p1."


def get_scenic_score(height, left, right, up, down) -> int:

    mult_score: int = 1
    left = left[::-1]
    up = up[::-1]
    # breakpoint()
    up_score: int = 0

    def count_visible(trees):
        score = 0
        for tree in trees:
            if int(tree) < height:
                score += 1
            else:
                score += 1
                break
        return score
    # breakpoint()
    # print(f"Current Height = {height}")
    # print(f"Up = {up}")
    up_score: int = count_visible(up)
    # print(f"Score after looking up: {up_score}")

    # print(f"Left = {left}")
    left_score: int = count_visible(left)
    # print(f"Score after looking left: {left_score}")

    # print(f"right = {right}")
    right_score: int = count_visible(right)
    # print(f"Score after looking right: {right_score}")

    # print(f"down = {down}")
    down_score: int = count_visible(down)
    # print(f"Score after looking down: {down_score}")

    mult_score = up_score * left_score * right_score * down_score

    return mult_score


def get_visible(rows: list, cols: list) -> int:
    score: int = 0
    scores = []
    y = 1
    while y < len(rows) - 1:
        row = list(rows[y])
        x = 1
        while x < len(row) - 1:
            # print(row[x])

            # Main Logic

            height = int(row[x])
            # print(f"Row val left to check {row[:x]}")
            # print(f"Row val right to check {row[x+1:]}")
            # print(f"Col val up to check {cols[x][:y]}")
            # print(f"Col val down to check {cols[x][y+1:]}")
            left, right = row[:x], row[x+1:]
            up, down = cols[x][:y], cols[x][y+1:]

            # Calculate scenic score

            scores.append(get_scenic_score(height, left, right, up, down))
            x += 1
        y += 1
        score = max(scores)
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
    rows = data.splitlines()
    columns = create_columns(rows)
    score = get_visible(rows, columns)
    return score


if __name__ == "__main__":
    main('**kwargs')

