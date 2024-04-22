"""Salary module"""

from data import load_salaries_data

def total_salary(path: str) -> tuple:
    """Returns total summary
    
    path:
        path to the file with data
    """
    salaries = load_salaries_data(path)
    avarage = calculate_avarage(salaries)
    total_sum = sum(salaries, 0)
    return (total_sum, avarage)

def calculate_avarage(salaries: list) -> int:
    """Returns avarage of salaries
    
    salaries:
        The list of salaries
    """
    avarage = 0
    salaries_length = len(salaries)

    if salaries_length > 0:
        avarage = sum(salaries, 0) // len(salaries)
    return avarage
