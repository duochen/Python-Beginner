import os

class LinCounter:
    def __init__(self, filename):
        self.file = open(filename)
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)

def get_file_full_path(filename):
    currentFilePath = os.path.abspath(__file__)
    currentFileDir = os.path.dirname(currentFilePath)
    return os.path.join(currentFileDir, filename)

file_full_path = get_file_full_path('example_file.txt')
lc = LinCounter(file_full_path) 
print(lc.lines)     # => []
print(lc.count())   # => 0

# The lc object must read the file to 
# set the lines property
lc.read()
# The 'lc.lines' property has been changed.
# This is called changing the state of the lc object
print(lc.lines)     # => ['Hello world!\n', ...]
print(lc.count())   # => 4



