#!/usr/bin/python3
"""Defines load_from_json_file method"""
import sys

if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file


try:
    list = load("add_item.json")
except FileNotFoundError:
    list = []
list.extend(sys.argv[1:])
save(list, "add_items.json")
