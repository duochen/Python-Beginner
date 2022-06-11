class Test:
    def __init__(self):
        self.x = 0

class Derived_Test(Test):
    def __init__(self):
        self.y = 1

def main():
    b = Derived_Test()
    print(b.x, b.y)

main()