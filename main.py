import csv
import matplotlib.pyplot as plt


def read_csv(file_name):
    buffer = open(file_name,'r')
    data_array = csv.DictReader(buffer)
    return data_array

matches  = read_csv('matches.csv')
deliveries = read_csv('deliveries.csv')
umpires = read_csv('umpires.csv')

color_codes = [
        "#FF5733",  # Red
        "#33FF57",  # Green
        "#3366FF",  # Blue
        "#FFFF33",  # Yellow
        "#FF33FF",  # Pink
        "#33FFFF",  # Cyan
        "#FF9933",  # Orange
        "#9933FF",  # Purple
        "#33FF99",  # Teal
        "#FF33CC",  # Magenta
        "#33CCFF",  # Sky Blue
        "#FFCC33",  # Gold
        "#33FFCC",  # Sea Green
        "#CC33FF",  # Lavender
        "#33CC99",  # Forest Green
    ]