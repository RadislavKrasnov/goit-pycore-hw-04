"""Entry point of the app"""

from cats import get_cats_info

def main():
    """Boots the app"""
    filename = 'cats.txt'
    cats_info = get_cats_info(filename)
    print(cats_info)

if __name__ == "__main__":
    main()
