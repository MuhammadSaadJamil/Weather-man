"""DB Format:
GST/PST,Max TemperatureC,Mean TemperatureC,Min TemperatureC,Dew PointC,MeanDew PointC,Min DewpointC,
Max Humidity, Mean Humidity, Min Humidity, Max Sea Level PressurehPa, Mean Sea Level PressurehPa, Min Sea Level
PressurehPa, Max VisibilityKm, Mean VisibilityKm, Min VisibilitykM, Max Wind SpeedKm/h, Mean Wind SpeedKm/h,
Max Gust SpeedKm/h,Precipitationmm, CloudCover, Events,WindDirDegrees

"""


def load_single_txt_file(path):
    try:
        file = open(path, 'r')
        return [line.split(",") for line in file if "," in line and "Max TemperatureC" not in line]
    except FileNotFoundError:
        return []


def create_db(file_list):
    db = []
    for file in file_list:
        db += load_single_txt_file(file)
    if not len(db) > 0:
        print("Data Not Found.")
        exit()
    return db
