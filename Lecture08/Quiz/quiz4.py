class test:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)

    def Change(self, var):
        var = 'New'

obj = test()
print(obj.variable)