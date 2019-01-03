class mystring():
    def __init__(self):
        self.str =""
    
    def get_String(self):
        self.str = input()

    def print_String(self):
        print(self.str.upper())

str = mystring()
str.get_String()
str.print_String()        