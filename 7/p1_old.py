"Advent of Code Day 7 - p1."


class TreeNode:
    "Represents a Node in the Tree"

    def __init__(self, name, size=0, children=None, parent=None):
        self.name: str = name
        self.size: int = size
        self.children: list = children if children is not None else []
        self.parent = parent

#     def __repr__(self):
#         return f"""name={self.name},
# size={self.size},
# children{self.children},
# parent={self.parent})"""
    def __repr__(self):
        parent_name = self.parent.name if self.parent else "None"
        return f"TreeNode(name={self.name}, parent={parent_name})"

    def add_node(self, node_name, parent):
        "Adds a node to the children and sets a parent."
        new_node = TreeNode(name=node_name, parent=parent)
        self.children.append(new_node)
        print(f"Added node: {new_node.name} \n With Parent: {new_node.parent}")

    def locate_nodes(self, ls):
        "Locate all nodes in the ls output."
        for entry in ls:
            if entry[:3] == "dir":
                node_name = entry[4:]
                self.add_node(node_name, self)

    def recursive_size(self) -> int:
        total_size = self.size
        if self.children == []:
            return self.size
        for child in self.children:
            total_size += child.recursive_size()
            # print(self.name, total_size)
        return total_size


def process(rows):
    i = 0
    ls: list = []
    dir_name: str = ""
    node = TreeNode(name="/", parent=None)
    current_node = node
    while i < len(rows):
        # print(rows[i])
        if rows[i] == "$ ls":
            i, ls = list_dir(i, [], rows)
            # print(ls)
            current_node.size += calc_dirsize(ls)
            current_node.locate_nodes(ls)
            current_node.size += node.recursive_size()

        elif rows[i][:4] == "$ cd":
            dir_name = get_dirname(rows[i])
            if dir_name == "..":
                if current_node.parent:
                    current_node = current_node.parent
            else:
                for child in current_node.children:
                    if child.name == dir_name:
                        current_node = child
                        child.parent = current_node
                        break


        # if node:
        #     print(node)
            # print(node.children)
            # print(node.parent)
        # if node:
        #     traverse_tree(node)
        i += 1

    # print(node)
    return node


def traverse_tree(node):
    if node:
        print(f"Node Name: {node.name}")
        print(f"Node Size: {node.size}")
        print(f"Node Chil: {node.children}")
        print(f"Node Pare: {node.parent}")
        for child in node.children:
            traverse_tree(child)


def get_dirname(command: str,) -> str:
    "Change directory name."
    # print(i)
    command_line = command.split(" ")
    # print(command_line)
    dir_name = command_line[2]
    return dir_name


def calc_dirsize(content_list: list) -> int:
    "Calc the size of a given dir."
    i: int = 0
    size: int = 0
    splitted: str = ""
    while i < len(content_list):
        if content_list[i][0].isdigit():
            splitted = content_list[i].split(" ")
            size += int(splitted[0])
        i += 1
    return size


def list_dir(i: int, ls_out: list, rows: list) -> tuple[int, list]:
    "List directory content."
    ls_out: list = []
    while i < len(rows):
        # Last value of the list
        if i == len(rows) - 1:
            return i, ls_out
        i += 1
        row = rows[i]
        # Early return
        if row[0] == "$":
            return i, ls_out
        ls_out.append(row)
        # print(f"Dir Lists at {i} = {ls_out}")
    return i, ls_out


def main(data):
    """Main Entry."""
    rows = data.splitlines()
    node = process(rows)
    # print(node)
    # traverse_tree(node)
    return 0

if __name__ == "__main__":
    main('**kwargs')
