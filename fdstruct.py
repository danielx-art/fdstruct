import os
import sys

def should_ignore(entry_name, ignore_list, all_files):
    if entry_name.startswith('.') and not all_files:
        return True
    for pattern in ignore_list:
        if pattern.startswith('/') and pattern[1:] == entry_name:
            return True
        elif pattern.startswith('*.') and entry_name.endswith(pattern[1:]):
            return True
        elif entry_name == pattern:
            return True
    return False

def print_structure(startpath, ignore, max_depth=None, prefix='', all_files=False, output_file=None):
    if max_depth is not None and max_depth < 1:
        return
    next_max_depth = None if max_depth is None else max_depth - 1
    try:
        with os.scandir(startpath) as it:
            for entry in it:
                if should_ignore(entry.name, ignore, all_files):
                    continue
                if entry.is_dir():
                    line = f"{prefix}└── {entry.name}/\n"
                else:
                    line = f"{prefix}└── {entry.name}\n"
                if output_file:
                    output_file.write(line)
                else:
                    print(line, end='')
                if entry.is_dir():
                    print_structure(entry.path, ignore, next_max_depth, prefix + "    ", all_files, output_file)
    except PermissionError:
        pass 

def main():
    if len(sys.argv) < 2:
        print("Usage: fdstruct <path> [-m <depth>] [-i <ignore_patterns>] [-a] [-o <output_file>]")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"Path {path} does not exist.")
        sys.exit(1)

    max_depth = None
    ignore_patterns = []
    all_files = False
    output_filename = None

    if "-m" in sys.argv:
        try:
            max_depth_index = sys.argv.index("-m") + 1
            max_depth = int(sys.argv[max_depth_index])
        except (ValueError, IndexError):
            print("Invalid depth value. Please provide an integer.")
            sys.exit(1)

    if "-i" in sys.argv:
        i_index = sys.argv.index("-i") + 1
        while i_index < len(sys.argv) and not sys.argv[i_index].startswith("-"):
            ignore_patterns.append(sys.argv[i_index])
            i_index += 1

    if "-a" in sys.argv:
        all_files = True

    if "-o" in sys.argv:
        try:
            o_index = sys.argv.index("-o") + 1
            output_filename = sys.argv[o_index]
        except IndexError:
            print("Invalid or missing output file name. Please specify a file name after -o.")
            sys.exit(1)

    if path == ".":
        path = os.getcwd()

    output_file = open(output_filename, 'w') if output_filename else None

    try:
        print_structure(path, ignore_patterns, max_depth, all_files=all_files, output_file=output_file)
    finally:
        if output_file:
            output_file.close()

if __name__ == "__main__":
    main()
