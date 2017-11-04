import sys
import json
from geopy.distance import vincenty


def load_data(filepath):
    with open(filepath, 'r', encoding="utf-8") as the_file:
        return json.load(the_file)


def get_biggest_bar(bars_list):
    biggest_bar = max(bars_list,
                      key=lambda index:
                      index['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bars_list):
    smallest_bar = min(bars_list,
                       key=lambda index:
                       index['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_distance(first_point, second_point):

    second_point.reverse()

    return vincenty(first_point, second_point).kilometers


def get_closest_bar(bars_list, coordinates):
    closest_bar = min(bars_list, key=lambda bar: get_distance(coordinates,
                      bar['geometry']['coordinates']))
    return closest_bar


def get_bar_details(the_bar):
    return the_bar['properties']['Attributes']


def get_bar_descr(bar_attributes, descr_kind):
    return "The {} bar is {} at {}".format(descr_kind,
                                           bar_attributes['Name'],
                                           bar_attributes['Address'])


if __name__ == '__main__':
    filepath = sys.argv[1]
    parsed_json = load_data(filepath)
    bars_list = parsed_json['features']
    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)

    my_coordinates_list = list(map(float, input("Latitude, Longitude: ")
                                   .split(",")))
    closest_bar = get_closest_bar(bars_list, my_coordinates_list)

    biggest_bar_attr = get_bar_details(biggest_bar)
    print(get_bar_descr(biggest_bar_attr, "biggest") + " with {} places"
          .format(biggest_bar_attr['SeatsCount']))

    smallest_bar_attr = get_bar_details(smallest_bar)
    print(get_bar_descr(smallest_bar_attr, "smallest") + " with {} places"
          .format(smallest_bar_attr['SeatsCount']))

    closest_bar_attr = get_bar_details(closest_bar)
    print(get_bar_descr(closest_bar_attr, "closest"))
