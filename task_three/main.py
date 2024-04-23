"""App entry point"""

import sys
from directory_printer import print_directory

def main():
    """Boots the application"""
    if len(sys.argv) > 1:
        print_directory(sys.argv[1])

if __name__ == "__main__":
    main()
