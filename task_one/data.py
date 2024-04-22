"""Load salaries data from file"""

def load_salaries_data(path: str) -> list[int]:
    """Reads and returns the list of salaries from file

    path:
        path to the file with data
    """
    salaries = []

    try:
        with open(path, 'r', encoding="utf-8") as file:
            rows = file.readlines()
            for row in rows:
                row = row.split(',')

                if len(row) > 1:
                    salary = row[1].strip()
                    salaries.append(int(salary))
    except FileNotFoundError as e:
        print(e)
    return salaries
