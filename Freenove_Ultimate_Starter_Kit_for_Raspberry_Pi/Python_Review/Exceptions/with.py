def read_file_using_exception(filename):
    try:
        infile = open(filename)
        data = infile.read()
    finally:
        infile.close()

def read_file_using_with(filename):
    with open(filename) as infile:
        data = infile.read()

