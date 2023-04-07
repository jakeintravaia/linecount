# !/usr/bin/python
import os

file_extensions = ["css", "js", "py", "html", "php"] # Change these as you please

# This function runs a check against valid file extensions
# previously defined in the file_extensions list

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
        extensions = []
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
    directory = input("Please input a valid directory: ")
    
    total = 0
    for f in get_valid(directory):
        print(f'{f}: {get_line_count(f)} lines')
        total += get_line_count(f)
    print(f'Total lines written: {total} lines.')


if __name__ == "__main__":
    main()