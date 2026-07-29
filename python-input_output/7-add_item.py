#!/usr/bin/python3
"""Defines an argument appending script that syncs to a JSON tracking file."""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    current_items = load_from_json_file(filename)
except FileNotFoundError:
    current_items = []

current_items.extend(sys.argv[1:])
save_to_json_file(current_items, filename)
