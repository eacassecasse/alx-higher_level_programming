#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    my_list = []

    for i in range(len(sys.argv) - 1):
        my_list.append(sys.argv[i + 1])
