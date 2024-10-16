import sys
from pathlib import Path
from colorama import Fore, Style

def print_directory_structure(path: Path, indent: str = "") -> None:
    if not path.exists() or not path.is_dir():
        print(f"{Fore.RED}Error: {path} does not exist or is not a directory.{Style.RESET_ALL}")
        return 

    # We display the directories
    for item in path.iterdir():
        if item.is_dir():
            print(f"{Fore.BLUE}{indent}{item.name}{Style.RESET_ALL}")  # Blue color for directories
            print_directory_structure(item, indent + "    ")  # Recursive browsing of folders
        else:
            print(f"{Fore.GREEN}{indent}{item.name}{Style.RESET_ALL}")  # Green color for files

if __name__ == "__main__":
    # Checking for command line arguments
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Correct command to run: python <start file path> <directory path>{Style.RESET_ALL}")
        sys.exit(1)

    # Getting the directory path from the arguments
    directory_path = Path(sys.argv[1])
    print_directory_structure(directory_path)
