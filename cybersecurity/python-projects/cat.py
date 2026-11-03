#!/usr/bin/python3

"""
This script processes input either from standard input (stdin) or from a
specified file. Reads lines from stdin or a file and prints them to standard
output (stdout).

Usage:
    - If no arguments are provided, reads from stdin.
    - If a filename is provided as a command-line argument, reads from that
      file.

Modules:
    sys: Provides access to command-line arguments and standard input/output
    streams.
"""
import sys

def std_in():
    """
    This function reads input from standard input (stdin) and prints each line
    to standard output (stdout). This simulates the behavior of the 'cat' command.
    """
    for line in sys.stdin:
        sys.stdout.write(line)

def infile(file):
    """
    This function reads from the specified file and prints its contents to
    standard output (stdout).

    Args:
        file (str): The path to the file to be read.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        with open(file, 'r') as f:
            for line in f:
                sys.stdout.write(line)
    except FileNotFoundError:
        sys.stderr.write(f"cat: {file}: No such file or directory\n")
        sys.exit(1)

# Determine whether to read from stdin or from a file based on
# command-line arguments. The length of sys.argv is checked to
# decide the source of input. sys.argv[0] is the name of this
# script, so we check for additional arguments (i.e., len(sys.argv) > 1).


if __name__ == "__main__":
    # Check the number of command-line arguments
    # If more than one argument is provided, use the second argument as the file path.
    # Otherwise, read from standard input.
    if len(sys.argv) > 1:
        infile(sys.argv[1])
    else:
        std_in()
