# Create a Person class and Student class. 
# The Student class is derived from Person class

class Person():
    def __init__(self, name = '', age = 20, sex = 'man'):
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)
    
    def setName(self, name):
        if not isinstance(name, str):
            print('name must be string.')
            return
        self._name = name
    
    def setAge(self, age):
        if not isinstance(age, int):
            print('age must be integer.')
            return
        self._age = age
    
    def setSex(self, sex):
        if sex != 'man' and sex != 'woman':
            print('sex must be "man" or "woman"')
            return
        self._sex = sex
    
    def show(self):
        print(self._name)
        print(self._age)
        print(self._sex)

class Student(Person):
    def __init__(self, name = '', age = 30, sex = 'man', major = 'Computer'):
        super().__init__(name, age, sex)
        self.setMajor(major)
    def setMajor(self, major):
        if not isinstance(major, str):
            print('major must be a string.')
            return
        self._major = major
    def show(self):
        super().show()
        print(self._major)

if __name__ == '__main__':
    peter = Person('Peter Lee', 19, 'man')
    peter.show()
    sam = Student('Sam Cook', 32, 'man', 'Math')
    sam.show()

