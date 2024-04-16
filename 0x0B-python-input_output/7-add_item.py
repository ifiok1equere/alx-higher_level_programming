#!/usr/bin/python3
"""This script processes arguments from cmd"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
obj = []

if len(sys.argv) == 1:
    save_to_json_file(obj, filename)
else:
    obj = load_from_json_file(filename)
    for i in range(1, len(sys.argv)):
        obj.append(sys.argv[i])
    save_to_json_file(obj, filename)
