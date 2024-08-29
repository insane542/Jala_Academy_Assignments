# Write a program to print your name.
print("Mihir Mane")

# Write a program for a Single line comment and multi-line comments.

#This is a single Line Comment

"""
This is a 
multi-line
comment
"""

# Define variables for different Data Types int, Boolean, char, float, double and print on the Console.
age = 22
print(age,type(age))

documents = True
print(documents,type(documents))

decimal = 3.14
print(decimal,type(decimal))

string = "Hello"
print(string[0],type(string))

# Define the local and Global variables with the same name and print both variables and understand the scope of the variables 
a = 20
def firstFnc():
    print("Default firstFnc, a =",a)

def localFnc():
    a = 40
    print("Inside LocalFnc, a =",a)

def globalFnc():
    global a
    a = 60
    print("Defined as GlobalFnc, a =",a)

print("Before redefining value of a =",a)
firstFnc() #This will print 20, as it uses the global 'a' outside the function defaultly
localFnc() #This will print 40, as it uses the local 'a' inside the function
globalFnc() #This will print 60, as it will redefine global 'a' to 60

print("Final value of 'a', after redefining global is",a)