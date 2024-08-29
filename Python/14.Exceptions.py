# Write a program to generate Arithmetic Exception without exception handling.
a = 10
b = 0
print("ERROR: Number cannot be divided by zero!")
result = a / b
print(result)

# Handle the Arithmetic exception using try-catch block
try:
    a = 100
    b = 0
    result = a / b
    print("ERROR")
except ZeroDivisionError:
    print("ZeroDivisionError: Number cannot be divided by 0")

# Write a method which throws exception, Call that method in main class without try block.x
class ExceptionClass(Exception):
    pass

def exception_method():
    raise ExceptionClass("Exception: Raising Exception from exception_method")

def main():
    exception_method()

if __name__ == "__main__":
    main()

# Write a program with multiple catch blocks.
def multiple_exception(a, b):
    try:
        result = a / b
        print("Result of division is",result)
    except ZeroDivisionError:
        print("ERROR: Number cannot be divided by zero!")
    except TypeError:
        print("ERROR: Invalid input data type! Only numbers allowed.")
    except Exception as e:
        print("An unexpected error occurred",e)
    
multiple_exception(10, 2)
multiple_exception(10, 0)
multiple_exception(10, "0")
multiple_exception("10", "2")

# Write a program to throw exception with your own message .
number = -1
if number < 0:
    raise ValueError("Number must be greater than 0")

try:
    number
except ValueError as e:
    print(f"Exception detected: {e}")

# Write a program to create your own exception.
# Write a program with finally block
class I_AM_EXCEPTION(Exception):
    pass

def is_exception_working(inp):
    if inp < 0:
        raise I_AM_EXCEPTION("AAAAAA Error: Input Cannot be negative!")

try:
    is_exception_working(-1)
except I_AM_EXCEPTION as e:
    print(f"{e}")
finally:
    print("I_AM_EXCEPTION was executed successfully.")

# Write a program to generate Arithmetic Exception.
def divide_by_zero():
    result = 10 / 0
    print(f"Result: {result}")

divide_by_zero()

# Write a program to generate FileNotFoundException.
def file_not_found_exception():
    with open('textfile.txt','r') as file:
        content = file.read()

file_not_found_exception()

# Write a program to generate ClassNotFoundException.
try:
    with open('textfile.txt','r') as file:
        content = file.read()
except FileNotFoundError as e:
    print("File doesnot exist.\n",e)

# Write a program to generate IOException.
try:
    with open('textfile.txt','r') as file:
        content = file.read()
        print(content)
except IOError as e:
    print("I/O Error Occured.\n",e)


# Write a program to generate NoSuchFieldException.
class NoSuchFieldFound():
    def __init__(self):
        self.field = "I am alive."
    
try:
    obj = NoSuchFieldFound()
    obj.no_field()
except AttributeError as e:
    print("Attribute not found.\n",e)