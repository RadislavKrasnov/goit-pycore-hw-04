"""Directory printer"""

from pathlib import Path
from colorama import Fore

def print_directory(path: str, indentation: str='') -> None:
    """Print directory by path
    
    path:
        path to the directory
    """
    path_object = Path(path)

    if not path_object.exists():
        return None

    if path_object.is_dir():
        print(Fore.BLUE + indentation + path_object.name)
        for path_item in sorted(path_object.iterdir()):
            if path_item.is_dir():
                print_directory(path_item.absolute(), indentation + '  ')
            else:
                print(Fore.GREEN + indentation + '  ' + path_item.name)
    else:
        print(Fore.GREEN + indentation + path_object.name)
