import sys
from pathlib import Path
from calendar import month_abbr, month_name


def check_args():
    args = sys.argv
    if len(args) < 4:
        print("Invalid number of arguments")
        exit()
    return args


def get_max_value(db, index):
    max = 0
    date = None
    for entry in db:
        try:
            if int(entry[index]) > max:
                max = int(entry[index])
                date = entry[0]
        except:
            pass
    return [date, max]


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
    return [date, min]


def get_avg_value(db, index):
    sum = 0
    readings = 0
    for entry in db:
        try:
            sum += int(entry[index])
            readings += 1
        except:
            pass
    return int(sum / readings)


def get_file_path(args, month=True):
    if month:
        date = args[2].split("/")
        file_path = f"{args[3]}{Path(args[3]).name}_{date[0]}_{month_abbr[int(date[1])]}.txt"
        return [file_path]
    else:
        paths = []
        for month in month_abbr:
            paths.append(f"{args[3]}{Path(args[3]).name}_{args[2]}_{month}.txt")
        return paths


def format_date(date):
    data = date.split("-")
    return f"{month_name[int(data[1])]} {data[2]}"


def draw_graph(db, date, inline=False):
    data = date.split("/")
    print(f"{month_name[int(data[1])]} {data[0]}")
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
                print(f"{day.zfill(2)} \033[91m{'+' * max_temp}\033[00m {max_temp}C")
            if min_temp != -1:
                print(f"{day.zfill(2)} \033[96m{'+' * min_temp}\033[00m {min_temp}C")
        else:
            if max_temp != -1 and min_temp != -1:
                print(f"{day.zfill(2)} "
                      f"\033[96m{'+' * min_temp}\033[00m\033[91m{'+' * max_temp}\033[00m "
                      f"{min_temp}C - {max_temp}C")
