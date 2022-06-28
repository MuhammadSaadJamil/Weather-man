"""
All functions related to creating db required by main application
"""

"""Convert txt file data to db ( list of lists ) 
Inputs -> path: path to file
Output -> db: list of lists, empty list in case of no data
"""


def load_single_txt_file(path):
    try:
        file = open(path, 'r')
        return [line.split(",") for line in file if "," in line and "Max TemperatureC" not in line]
    except FileNotFoundError:
        return []


"""Convert all txt file data to single db ( list of lists ) 
Inputs -> file_list: list of file paths
Output -> db: list of lists, terminate execution with error message in case of no data
"""


def create_db(file_list):
    db = []
    for file in file_list:
        db += load_single_txt_file(file)
    if not len(db) > 0:
        print("Data Not Found.")
        exit()
    return db
