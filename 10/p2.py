"Advent of Code Day 10 - p1."


def process(data) -> list:
    """Creates a list of clock states."""
    clock = []
    x = 1
    for instr in data:
        if instr == "noop":
            clock.append(x)
        if instr.startswith("addx"):
            val = instr.split()[-1]
            for _ in range(2):
                clock.append(x)
            x += int(val)
    clock.append(x)
    return clock

def get_strength(clock: list) -> int:
    total: int = 0
    clock = clock[19::40]
    multiplier = list(range(221))
    multiplier = multiplier[20::40]
    for x, y in zip(clock, multiplier):
        total += x * y
    return total

def draw_row(clock):
    ans = [["."] * 40 for _ in range(6)]
    for y, row in enumerate(ans):
        for x, _ in enumerate(row):
            idx = y * 40 + x
            # print(idx)
            # print(f" current sprite {clock[idx]}")
            if x == clock[idx] - 1 or x == clock[idx] \
                    or x == clock[idx] + 1:
                row[x] = "\033[92m#"
            else:
                row[x] = " "
        x = 0
    for row in ans:
        row = "".join(row)
        print(f"{row}")

def main(data):
    """Main Entry."""
    rows = data.splitlines()
    clock = process(rows)
    draw_row(clock)


if __name__ == "__main__":
    main('**kwargs')

