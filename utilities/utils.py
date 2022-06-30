import sys
from pathlib import Path
from calendar import month_abbr, month_name

"""This module contain all utilities required by main application"""

"""Check if correct number of arguments are passed
"""


def check_args():
    args = sys.argv
    if len(args) < 4 or len(args) > 4:
        print("Invalid number of arguments")
        print("Format:\n\tpython3 weatherman.py -[flag] [Date] [/path/to/file]")
        exit()
    return args


"""Get max value from given index column
Inputs -> db: database, index: index of required value
Output -> [date_of_max_value, max_value]
"""


def get_max_value(db, index):
    max = -1
    date = None
    for entry in db:
        try:
            if int(entry[index]) > max:
                max = int(entry[index])
                date = entry[0]
        except:
            pass
    if max == -1:
        return [date, -1]
    return [date, max]


"""Get min value from given index column
Inputs -> db: database, index: index of required value
Output -> [date_of_min_value, min_value]
"""


def get_min_value(db, index):
    min = 10000
    date = None
    for entry in db:
        try:
            if int(entry[index]) < min:
                min = int(entry[index])
                date = entry[0]
        except:
            pass
    if min == 10000:
        return [date, -1]
    return [date, min]


"""Get avg value from given index column
Inputs -> db: database, index: index of required value
Output -> avg_value | -1 in case of no data
"""


def get_avg_value(db, index):
    sum = 0
    readings = 0
    for entry in db:
        try:
            sum += int(entry[index])
            readings += 1
        except:
            pass
    try:
        return int(sum / readings)
    except:
        return -1


"""Create file/files path from args and return a list of files
Inputs -> args: list of arguments passed on command line, month: boolean if command line argument contain month
Output -> list of all paths
"""


def get_file_path(args, month=True):
    if month:
        date = args[2].split("/")
        try:
            if int(date[1]) < 1:
                raise Exception()
            file_path = f"{args[3]}{Path(args[3]).name}_{date[0]}_{month_abbr[int(date[1])]}.txt"
            return [file_path]
        except:
            print("Missing / Invalid input for month. Use format YYYY/MM or YYYY/M for date.")
            exit()
    else:
        if "/" in args[2]:
            print("Invalid Date Entered. Enter Date of Format YYYY.")
            exit()
        paths = []
        for month in month_abbr:
            paths.append(f"{args[3]}{Path(args[3]).name}_{args[2]}_{month}.txt")
        return paths


"""Format date from YYYY-MM-DD to Month Date
Inputs -> date: string date of format YYYY-MM-DD
Output -> string fate of format Month Date
"""


def format_date(date):
    data = date.split("-")
    return f"{month_name[int(data[1])]} {data[2]}"


"""Draw graph for all values in DB either inline or on separate line for all dates 
Inputs -> db: database, date: date passed as argument, inline: boolean if graph will be inline
Output -> Graph
"""


def draw_graph(db, date, inline=False):
    # Format date
    data = date.split("/")
    print(f"{month_name[int(data[1])]} {data[0]}")
    # Draw graph for every entry of db if data is present
    data_flag = False
    for entry in db:
        day = entry[0].split("-")[2]
        max_temp = -1
        min_temp = -1
        try:
            max_temp = int(entry[1])
        except:
            pass
        try:
            min_temp = int(entry[3])
        except:
            pass
        if not inline:
            if max_temp != -1:
                data_flag = True
                print(f"{day.zfill(2)} \033[91m{'+' * max_temp}\033[00m {max_temp}C")
            if min_temp != -1:
                data_flag = True
                print(f"{day.zfill(2)} \033[96m{'+' * min_temp}\033[00m {min_temp}C")
        else:
            if max_temp != -1 and min_temp != -1:
                data_flag = True
                print(f"{day.zfill(2)} "
                      f"\033[96m{'+' * min_temp}\033[00m\033[91m{'+' * max_temp}\033[00m "
                      f"{min_temp}C - {max_temp}C")
    if not data_flag:
        print('No Data Found.')
