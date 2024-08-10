"Advent of Code Day 7 - p2."
from typing import Optional, Required


class Dir:
    """Represent a Directory."""

    def __init__(self, name, parent, childs=None, size=0,):
        self.name: str = name
        self.childs: list = childs if childs is not None else []
        self.size: int = size
        self.parent: Optional[Dir] = parent

    def __repr__(self):
        return f"Dir(name={self.name}, size={self.size})"

    def add_child(self, child):
        self.childs.append(child)

    def add_size(self, filesize):
        self.size += filesize


def process(rows):
    i = 0
    directory = Dir(name="root", parent=None)
    current_dir = directory
    large_bois: list = []
    while i < len(rows):
        # print(rows[i])
        if rows[i] == "$ cd /":
            i += 1
            continue
        elif rows[i] == "$ ls":
            i += 1
            continue
        elif rows[i][0].isdigit():
            # file found
            filesize = int(rows[i].split(" ")[0])
            # print(filesize)
            current_dir.add_size(filesize)
        elif rows[i][:3] == "dir":
            # print(rows[i])
            dirname = rows[i][4:]
            current_dir.add_child(Dir(name=dirname, parent=current_dir))
        elif rows[i] == "$ cd ..":
            if current_dir.parent is not None:
                current_dir.parent.add_size(current_dir.size)
            large_bois.append(current_dir)
            current_dir = current_dir.parent
        else:
            # Case $ cd irgendwas
            dirname = rows[i][5:]
            for child in current_dir.childs:
                if child.name == dirname:
                    current_dir = child
        # print(current_dir)
        i += 1
    # Add current to parent for the last
    if current_dir.parent is not None:
        current_dir.parent.add_size(current_dir.size)
    large_bois.append(current_dir)
    large_bois.append(current_dir.parent)
    return large_bois


def main(data):
    """Main Entry."""
    sizelist = []
    rows = data.splitlines()
    large_bois = process(rows)
    for large in large_bois:
        sizelist.append(int(large.size))
    sizelist = sorted(sizelist)
    print(sizelist)
    leftover = 70_000_000 - sizelist[-1]
    print(leftover)
    for size in sizelist:
        if size >= (30_000_000 - leftover):
            return size
    # print(node)
    # traverse_tree(node)


if __name__ == "__main__":
    main('**kwargs')

