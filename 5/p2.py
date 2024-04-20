import re


def get_0_string(stack_list: list) -> str:
    result: str = ""
    charlist: list = []
    for stack in stack_list:
        if stack != []:
            charlist.append(stack[0])
    result = "".join(charlist)
    return result


def apply_instructions(stack_list: list, instruction_list) -> list:
    for instruction in instruction_list:
        amount, source, dest = instruction[0], instruction[1], instruction[2]
        storage = []
        # Remove from Source
        source_stack = stack_list[source]
        storage = source_stack[:amount]
        # Slice off
        source_stack = source_stack[amount:]
        stack_list[source] = source_stack
        # Apply to destination
        dest_stack = stack_list[dest]
        storage = storage[::-1]
        for item in storage:
            dest_stack.insert(0, item)
        stack_list[dest] = dest_stack
    return stack_list


def get_instructions(instruction_data: str) -> list:
    "Get a list of instructions."
    lines = instruction_data.splitlines()
    instruction_list: list = []
    for line in lines:
        ints = re.findall(r"\d+", line)
        amount, source, dest = int(ints[0]), int(ints[1])-1, int(ints[2])-1
        instruction_list.append((amount, source, dest))
    return instruction_list


def get_initial_stack(crates):
    "Build a the initial stack from the input."
    crates = crates.splitlines()[:-1]
    stackdict: dict[int, list] = {}

    for row in crates:
        for i, char in enumerate(row):
            if i not in stackdict:
                stackdict.update({i: []})
            if char not in ['', '[', ']', ' ']:
                stackdict[i].append(char)
    stack_list: list = []

    for k in stackdict:
        if stackdict[k] != []:
            stack_list.append(stackdict[k])
    return stack_list


def main(data):
    """Main Entry."""
    crates, instructions = data.split("\n\n")
    stack_list = get_initial_stack(crates)
    instruction_list = get_instructions(instructions)
    stack_list = apply_instructions(stack_list, instruction_list)
    result = get_0_string(stack_list)
    return result


if __name__ == "__main__":
    main('**kwargs')
