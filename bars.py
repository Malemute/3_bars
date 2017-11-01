import json
from geopy.distance import vincenty


def load_data(filepath):
    with open(filepath, 'r') as the_file:
        return json.load(the_file)


def get_biggest_bar(bars_list):
    biggest_bar = max(bars_list,
                      lambda index: index['properties']['Attributes']['SeatsCount'])
    return biggest_bar


def get_smallest_bar(bars_list):
    smallest_bar = min(bars_list,
                       lambda index: index['properties']['Attributes']['SeatsCount'])
    return smallest_bar


def get_distance(first_point, second_point):
    return vincenty(first_point, second_point)


def get_closest_bar(bars_list, coordinates):
    closest_bar = min(bars_list, key=get_distance(coordinates,
                        lambda index: index['geometry']['coordinates']))
    return closest_bar


if __name__ == '__main__':
    filepath = sys.argv[1]
    parsed_json = load_data(filepath)
    bars_list = parsed_json['features']
    biggest_bar = get_biggest_bar(bars_list)
    smallest_bar = get_smallest_bar(bars_list)

    my_coordinates = map(float, input("Longitude, Latitude: ").split(","))
    closest_bar = get_closest_bar(bars_list, my_coordinates)

    print("The biggest bar is {} at {}".format())
