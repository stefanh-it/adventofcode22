"Advent of Code Day 18 - p1."


def count_outside(rows):
    for row in rows:
        x,y,z = row.split(",")
        print(f"x = {x}, y = {y}, z = {z}")

def main(data):
    """Main Entry."""
    total_sum = 0
    rows = data.splitlines()
    count_outside(rows)
    return total_sum



if __name__ == "__main__":
    main('**kwargs')


