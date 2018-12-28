import os

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

def count(lines):
    return len(lines)

def get_file_full_path(filename):
    currentFilePath = os.path.abspath(__file__)
    currentFileDir = os.path.dirname(currentFilePath)
    return os.path.join(currentFileDir, filename)

file_full_path = get_file_full_path('example_file.txt')
example_lines = read(file_full_path) 
lines_count = count(example_lines)
print(example_lines)     # => ['Hello world!\n', ...]
print(lines_count)       # => 4