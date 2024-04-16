#!/usr/bin/python3
"""This script processes arguments from cmd"""
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []

for i in range(1, len(sys.argv)):
    obj.append(sys.argv[i])
save_to_json_file(obj, filename)
