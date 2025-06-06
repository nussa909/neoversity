import sys
import pathlib
from colored_output import show_directory, show_file

def show_directory_tree(path, count = 0):
    if path.is_file():
        return
    
    spaces = (count+1) * 4 * " "
    for item in path.iterdir():
        show_directory(item, spaces) if item.is_dir() else show_file(item,spaces)
        show_directory_tree(item,count+1)


def main():
    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        print("Error: Path does not exist")
        return

    show_directory(path)
    show_directory_tree(path)


if __name__ == "__main__":
    main()