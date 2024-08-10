"Advent of Code Day 9 - p1."


def run_instructions(instructions):
    visited: set[tuple] = set([(0, 0)])
    head = [0, 0]
    tail = [0, 0]
    for instruction in instructions:
        direction, y = instruction.split(" ")
        y = int(y)

        # Split steps into single instructions
        for _ in range(y):
            if direction == 'R':
                dx = 1
            elif direction == 'L':
                dx = -1
            else:
                dx = 0

            if direction == 'U':
                dy = 1
            elif direction == 'D':
                dy = -1
            else:
                dy = 0

            # Update the value of the head

            head[0] += dx
            head[1] += dy

            # Calculate the difference head and tail ( maximum value is 2 )
            delta_x = head[0] - tail[0]
            delta_y = head[1] - tail[1]

            # Move the tail
            if abs(delta_x) > 1 or abs(delta_y) > 1:
                if delta_x == 0:  # They are in the same column
                    # Move tail vertically
                    # Either -1, 0 or 1 depending on the delta
                    tail[1] += delta_y // 2
                elif delta_y == 0:  # They are in the same row
                    # Move tail horizontally
                    tail[0] += delta_x // 2
                else:
                    # Move to the right if delta x is greater than 0
                    if delta_x > 0:
                        tail[0] += 1
                    # Move to the left if delta x is below 0
                    else:
                        tail[0] += -1
                    if delta_y > 0:
                        tail[1] += 1
                    else:
                        tail[1] += -1
            visited.add(tuple(tail))
    print(visited)
    return len(visited)


def main(data):
    """Main Entry."""
    total_sum = 0
    instructions = data.splitlines()
    total_sum = run_instructions(instructions)
    return total_sum


if __name__ == "__main__":
    main('**kwargs')
