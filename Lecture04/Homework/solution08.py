def decorator(fn):
    def wrapper():
        print("Before the function is called")
        fn()
        print("After the function is called")

    return wrapper

@decorator
def foo():
    print("Hello World!")    

foo()
# Before the function is called
# Hello World!
# After the function is called