"""Cats module"""

def get_cats_info(path: str) -> list[dict]:
    """Returns list of dictionaries with info about cats
    
    path:
        The path to file with cats data
    """
    cats_info = []

    try:
        with open(path, 'r', encoding="utf-8") as file:
            rows = file.readlines()
            for row in rows:
                row = row.split(',')
                id = row[0].strip()
                name = row[1].strip()
                age = row[2].strip()

                cat_info = {
                    "id": id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_info)
    except FileNotFoundError as e:
        print(e)
    except IndexError as e:
        print(e)
    return cats_info
