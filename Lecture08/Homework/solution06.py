class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
print(error.msg)