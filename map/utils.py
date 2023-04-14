# import csv
# from map.models import Antenna
#
# path = '/home/virus/antenna_map.csv'
#
# def load_antennas_from_csv():
#     with open(path, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader) # skip header row
#         for row in reader:
#             name, configuration, latitude, longitude = row
#             Antenna.objects.create(name=name, configuration=configuration, latitude=latitude, longitude=longitude)

# import csv
# from decimal import Decimal
# from map.models import Antenna
#
# def load_antennas_from_csv():
#     path = '/home/virus/antenna_map.csv'
#     with open(path, 'r') as csvfile:
#         reader = csv.reader(csvfile)
#         next(reader) # skip header row
#         for row in reader:
#             name, configuration, latitude_str, longitude_str = row
#             latitude = Decimal(float(latitude_str[:-1]))  # убрать символ градуса и преобразовать в Decimal
#             longitude = Decimal(longitude_str)
#             Antenna.objects.create(name=name, configuration=configuration, latitude=latitude, longitude=longitude)


import csv
from decimal import Decimal
from map.models import Antenna


def load_antennas_from_csv():
    path = '/home/virus/antenna_map.csv'
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) # skip header row
        for row in reader:
            name, configuration, latitude_str, longitude_str = row
            latitude = Decimal(latitude_str)
            longitude = Decimal(longitude_str)
            Antenna.objects.create(name=name, configuration=configuration, latitude=latitude, longitude=longitude)
