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

def main(data):
    """Main Entry."""
    score = 0
    rows = data.splitlines()
    clock = process(rows)
    score = get_strength(clock)
    return score


if __name__ == "__main__":
    main('**kwargs')
