import sys
import json


def load_data(filepath):
	with open(filepath, 'r') as string_from_file:
		return json.load(string_from_file)


def pretty_print_json(data):
	return json.dumps(data, indent=4, sort_keys=True)


if __name__ == '__main__':
	filepath = sys.argv[0]
	parsed_json = load_data(filepath)
	pretty_printed_json = pretty_print_json(parsed_json)
	print(pretty_printed_json)
