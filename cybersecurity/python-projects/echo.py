#!/usr/bin/python3

"""
This script processes command-line arguments to simulate a simplified echo
command.It concatenates the arguments into a single string and prints the
result to standard output (stdout).

Usage:
    - If no arguments are provided, prints a blank line.
    - If one or more arguments are provided, prints them concatenated into
      a single string.

Modules:
    sys: Provides access to command-line arguments and standard input/output
    streams.
"""

import sys


def array_to_string(arr):
    """
    Converts a list of strings into a single concatenated string with spaces
    between each element.

    Args:
        arr (list of str): A list of strings to be concatenated.

    Returns:
        str: A single string with each element of the list separated by a
        space.
    """
    return ' '.join(arr)


if __name__ == "__main__":
    args = sys.argv[1:]
    result = array_to_string(args)
    print(result)
