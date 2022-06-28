from utilities.database import create_db
from utilities.utils import *

args = check_args()
if args[1] == '-e':
    files = get_file_path(args, month=False)
    db = create_db(files)
    highest_temp = get_max_value(db, 2)
    lowest_temp = get_min_value(db, 2)
    highest_humidity = get_max_value(db, 8)
    print(f"Highest: {highest_temp[1]}C on {format_date(highest_temp[0])}")
    print(f"Lowest: {lowest_temp[1]}C on {format_date(lowest_temp[0])}")
    print(f"Humid: {highest_humidity[1]}% on {format_date(highest_humidity[0])}")
else:
    files = get_file_path(args, month=True)
    db = create_db(files)
    if args[1] == '-a':
        print(f"Highest Average: {get_avg_value(db, 1)}C")  # ind 1 -> Max_Temp
        print(f"Lowest Average: {get_avg_value(db, 3)}C")  # ind 3 -> Min_Temp
        print(f"Average Humidity: {get_avg_value(db, 8)}%")  # ind 8 -> Mean_Humidity
    elif args[1] == '-c':
        draw_graph(db, args[2], inline=False)
    elif args[1] == '-f':
        draw_graph(db, args[2], inline=True)
