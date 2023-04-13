#!/usr/bin/python3
# 1-number_of_lines.py
"""Defines a text file character counting function."""


def write_file(filename="", text=""):
    """Return the number of characters in a text file."""
    ch = 0
    with open(filename, "r+", encoding="utf-8") as f:
        f.write(text)
        filecont = f.read()
        for character in filecont:
            ch = ch + 1
    return ch     
