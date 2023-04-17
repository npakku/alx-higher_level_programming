#!/usr/bin/python3
# 1-number_of_lines.py
"""Defines a text file character counting function."""


def write_file(filename="", text=""):
    """Return the number of characters in a text file."""
    with open(filename, "r+", encoding="utf-8") as f:
        write = f.write(text)
    return write
