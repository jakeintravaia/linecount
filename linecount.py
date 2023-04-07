# !/usr/bin/python
import os
import argparse

# Set up command line arguments via argparse

parser = argparse.ArgumentParser(description='This program recursively walks a given directory and counts the lines within specified file types.')

parser.add_argument('-d', '--dir', help='The directory you would like to search.', required=True)
parser.add_argument('-e', '--exts', nargs='+', help='The file extensions you would like to search for.', required=True)

args = parser.parse_args()

file_extensions = args.exts

# This function runs a check against valid file extensions
# defined by the user at run time

def check_valid(file):
    tmp = []
    for f in file_extensions:
        if f == file[1]:
            return True
    return False

# This function returns a list of valid files within the 
# defined directory

def get_valid(directory):
   tmp = []
   for root, dirs, files in os.walk(directory, topdown=False):
        for name in files:
            ext = name.split(".")
            if check_valid(ext):
                tmp.append(os.path.join(root, name))
   return tmp

# This function returns the line count of a specified file

def get_line_count(f):
    file = open(f, 'r')
    lines = file.readlines()
    return len(lines)

# This function asks a user for a directory and
# prints out valid file names along with their
# line count, and prints the total line count
# of all the valid files.

def main():
    directory = args.dir
    if os.path.exists(directory):
        total = 0
        for f in get_valid(directory):
            print(f'{f}: {get_line_count(f)} lines')
            total += get_line_count(f)
        print(f'Total lines written: {total} lines.')
    else:
        print("Error: Directory does not exist.")


if __name__ == "__main__":
    main()