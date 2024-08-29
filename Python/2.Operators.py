# Write a function for arithmetic operators.

def arithmetic_Operators(a, b):
    print(f"\nAddition of {a} and {b} is",a+b)
    print(f"Subtraction of {a} and {b} is",a-b)
    print(f"Multiplication of {a} and {b} is",a*b)
    print(f"Division of {a} and {b} is",a/b)
    print(f"Modulus of {a} and {b} is",a%b)

a = int(input("Enter value for num1: "))
b = int(input("Enter value for num2: "))
arithmetic_Operators(a, b)

# Write a method for increment and decrement operators

a = 1
print("Value of a:",a)
a += 1
print("After Increment:",a)
a -= 1
print("After Decrement:",a)
print()

#Using increment with For Loop, start = 1, end = 5-1, step = 1
print("Increment using For Loop from 1 to 4:")
for i in range(1, 5):
    print(i)
print()
#Using decrement with For Loop, start = 4, end = 0, step = -1
print("Decrement using For Loop from 4 to 1:")
for i in range(4, 0, -1):
    print(i)
print()

# Write a program to find the two numbers equal or not.
print("Find two numbers are equal or not.")
a = input('Enter first number: ')
b = input('Enter second number: ')

if a == b:
    print(f"Value {a} and {b} are same.")
else:
    print(f"values {a} and {b} are not same.")

# Write a Program for relational operators (<,<==, >, >==)

a = 10
b = 20
print(a > b) #This returns true if the left variable is greater than right variable.
print(a >= b) #This returns true if the left variable is greater than or equal to right variable.
print(a < b) #This returns true if the left variable is less than right variable.
print(a <= b) #This returns true if the left variable is less than or equal to right variable.
print(a == b) #This returns true if the left variable and right variable have same value.
print(a != b) #This returns true if the left variable and right variable are not same values.

# Print the smaller and larger number.
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))

if a > b:                           #Condition for Larger number
     print(f"{a} is greater number.")
else:
    print(f"{b} is greater number.")

if a < b:                           #Condition for Smaller number
     print(f"{a} is smaller number.")
else:
    print(f"{b} is smaller number.")