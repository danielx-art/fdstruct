import os
import sys

def print_structure(startpath, ignore, max_depth=None, prefix=''):
    if max_depth is not None and max_depth < 1:
        return
    next_max_depth = None if max_depth is None else max_depth - 1
    try:
        for entry in os.scandir(startpath):
            if entry.name in ignore:
                continue
            if entry.is_dir():
                print(f"{prefix}└── {entry.name}/")
                print_structure(entry.path, ignore, next_max_depth, prefix + "    ")
            else:
                print(f"{prefix}└── {entry.name}")
    except PermissionError:
        pass  # Ignore directories for which the user has no access permission.

def main():
    if len(sys.argv) < 2:
        print("Usage: fdstruct <path> [-m <depth>] [-i <ignore_folders>]")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"Path {path} does not exist.")
        sys.exit(1)

    max_depth = None
    if "-m" in sys.argv:
        try:
            max_depth_index = sys.argv.index("-m") + 1
            max_depth = int(sys.argv[max_depth_index])
        except (ValueError, IndexError):
            print("Invalid depth value. Please provide an integer.")
            sys.exit(1)

    ignore_folders = []
    if "-i" in sys.argv:
        try:
            i_index = sys.argv.index("-i") + 1
            while i_index < len(sys.argv) and not sys.argv[i_index].startswith("-"):
                ignore_folders.append(sys.argv[i_index])
                i_index += 1
        except IndexError:
            print("Invalid ignore folders list. Please provide folder names after -i.")
            sys.exit(1)

    if path == ".":
        path = os.getcwd()

    print_structure(path, ignore_folders, max_depth)

if __name__ == "__main__":
    main()
