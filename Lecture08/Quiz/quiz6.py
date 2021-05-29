class A():
    def disp(self):
        print("A disp()")

class B(A):
    pass

obj = B()
obj.disp()