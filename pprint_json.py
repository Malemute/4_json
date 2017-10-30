import sys
import json


def load_data(filepath):
    with open(filepath, 'r') as the_file:
        return json.load(the_file)


def format_json_for_human(json_formatted_stream):
    return json.dumps(json_formatted_stream, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    filepath = sys.argv[1]
    parsed_json = load_data(filepath)
    human_readable_json = format_json_for_human(parsed_json)
    print(human_readable_json)
