import sys
import json


def load_data(filepath):
    with open(filepath, 'r') as the_file:
        return json.load(the_file)


def pretty_print_json(data):
    return json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    filepath = sys.argv[1]
    parsed_json = load_data(filepath)
    pretty_printed_json = pretty_print_json(parsed_json)
    print(pretty_printed_json)
