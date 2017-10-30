import json
from geopy.distance import vincenty


def load_data(filepath):
    with open(filepath, 'r') as the_file:
        return json.load(the_file)


def get_biggest_bar(data):
    pass


def get_smallest_bar(data):
    pass


def get_closest_bar(bars_list, longitude, latitude):
    
    pass


if __name__ == '__main__':
    filepath = sys.argv[1]
    parsed_json = load_data(filepath)
    bars_list = parsed_json['features']
	smallest_bar = get_smallest_bar(bars_list)
	biggest_bar = get_biggest_bar(bars_list)
	
	my_coordinates = input("Longitude, Latitude: ")
	closest_bar = get_closest_bar(bars_list, my_coordinates[0], my_coordinates[1])
    print("")
