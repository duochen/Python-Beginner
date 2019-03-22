import os

def read_file_using_exception(filename):
    try:
        infile = open(filename)
        data = infile.read()
        print(data)
    finally:
        infile.close()

def read_file_using_with(filename):
    with open(filename) as infile:
        data = infile.read()
        print(data)

def get_file_full_path(filename):
    currentFilePath = os.path.abspath(__file__)
    currentFileDir = os.path.dirname(currentFilePath)
    return os.path.join(currentFileDir, filename)

file_with_full_path = get_file_full_path("with.py")

read_file_using_with(file_with_full_path)
read_file_using_exception(file_with_full_path)