from utilities.database import create_db
from utilities.utils import *

args = check_args()

if args[1] == '-e':
    files = get_file_path(args, month=False)
    db = create_db(files)
    highest_temp = get_max_value(db, 2)
    lowest_temp = get_min_value(db, 2)
    highest_humidity = get_max_value(db, 8)
    print(f"Highest: {highest_temp[1]} on {format_date(highest_temp[0])}")
    print(f"Lowest: {lowest_temp[1]}C on {format_date(lowest_temp[0])}")
    print(f"Humid: {highest_humidity[1]}% on {format_date(highest_humidity[0])}")
elif args[1] == '-a':
    files = get_file_path(args, month=True)
    db = create_db(files)
    highest_avg = get_avg_value(db, 1)
    lowest_avg = get_avg_value(db, 3)
    avg_humidity = get_avg_value(db, 8)
    """
    ind 1 -> Max_Temp
    ind 3 -> Min_Temp
    ind 8 -> Mean_Humidity
    """
    print(f"Highest Average: {f'{highest_avg}C' if highest_avg != -1 else 'Data Not Found'}")
    print(f"Lowest Average: {f'{lowest_avg}C' if lowest_avg != -1 else 'Data Not Found'}")
    print(f"Average Humidity: {f'{avg_humidity}%' if avg_humidity != -1 else 'Data Not Found'}")
elif args[1] == '-c':
    files = get_file_path(args, month=True)
    db = create_db(files)
    draw_graph(db, args[2], inline=False)
elif args[1] == '-f':
    files = get_file_path(args, month=True)
    db = create_db(files)
    draw_graph(db, args[2], inline=True)
else:
    print("Invalid Flag")
