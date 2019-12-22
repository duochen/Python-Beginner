""" File: hello.py """

def greet(name):
    print("Hey {}, I'm Python!".format(name))

# Run only if called as a script
if __name__ == '__main__':
    name = input("What is your name? ")
    greet(name)