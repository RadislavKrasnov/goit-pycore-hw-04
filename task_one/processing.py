"""Processing salaries data"""

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
