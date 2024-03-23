#One of the main reasons to use decorators is
#if we want to add the same functionality to a number of functions

#To understand how decorator works
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#When you call say_hello(), it's equivalent to calling my_decorator(say_hello)().
# The wrapper function within my_decorator wraps around say_hello.



