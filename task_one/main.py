"""The entry point module"""

from data import load_salaries_data
from processing import calculate_avarage

def main():
    """Boots the application"""
    filename = 'salaries.txt'
    salaries = load_salaries_data(filename)
    avarage = calculate_avarage(salaries)
    total_sum = sum(salaries, 0)
    return (total_sum, avarage)

if __name__ == "__main__":
    print(main())
