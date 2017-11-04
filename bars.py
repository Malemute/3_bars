import sys
import json
from geopy.distance import vincenty


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as the_file:
        return json.load(the_file)


def get_biggest_bar(bars_list):
    biggest_bar = max(bars_list, key=
                      lambda index:
                      index['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bars_list):
    smallest_bar = min(bars_list, key=
                       lambda index:
                       index['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_distance(first_point, second_point_reversed):

    #Beware! Merry guys from Mos.ru keep coordinates in reversed order: E, N
    # (say, for Moscow it's 37, 55 - not 55, 37!

    second_point_normal = [second_point_reversed[1], second_point_reversed[0]]

    return vincenty(tuple(first_point), tuple(second_point_normal)).kilometers


def get_closest_bar(bars_list, coordinates):
    closest_bar = min(bars_list, key=lambda bar: get_distance(coordinates,
                        bar['geometry']['coordinates']))
    return closest_bar


def get_attributes_of_the_bar(the_bar):
    return the_bar['properties']['Attributes']


if __name__ == '__main__':
    filepath = sys.argv[1]
    parsed_json = load_data(filepath)
    bars_list = parsed_json['features']
    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)

    my_coordinates_list = list(map(float, input("Latitude, Longitude: ")
                                   .split(",")))
    closest_bar = get_closest_bar(bars_list, my_coordinates_list)

    biggest_bar_attr = get_attributes_of_the_bar(biggest_bar)
    print("The biggest bar is {} at {} with {} places"
          .format(biggest_bar_attr['Name'],
                  biggest_bar_attr['Address'],
                  biggest_bar_attr['SeatsCount']))

    smallest_bar_attr = get_attributes_of_the_bar(smallest_bar)
    print("The smallest bar is {} at {} with {} places"
          .format(smallest_bar_attr['Name'],
                  smallest_bar_attr['Address'],
                  smallest_bar_attr['SeatsCount']))

    closest_bar_attr = get_attributes_of_the_bar(closest_bar)
    print("The closest bar is {} at {}"
          .format(closest_bar_attr['Name'],
                  closest_bar_attr['Address']))
