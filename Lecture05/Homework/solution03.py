class MyClass:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

m = MyClass()
print(m.reverse_words('Hello World'))  # => World Hello
