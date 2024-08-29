# Write a program to print  “Bright IT Career”  ten times using for loop.
string = "Bright IT Career"
for i in range(10):
    print(string)
print()

# Write a java program to print 1 to 20 numbers using the while loop.
i = 1
while i <= 20:
    print(i)
    i+=1
print()

# Program to equal operator and not equal operators.
a = 10
b = 11
print("Is value of 'a' equal to 'b'",a == b'\n')
print("Is value of 'a' not equal to 'b'",a != b'\n')

# Write a program to print the odd and even numbers. 
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for i in List:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("Odd numbers:",odd,'\n')

# Write a program to print largest number among three numbers.
a = 10
b = 20
c = 30
if a > b and a > c:
    print("'a' is the largest number.'\n'")
elif b > a and b > c:
    print("'b' is the largest number.'\n'")
else:
    print("'c' is the largest number.'\n'")

# Write a  program to print even number between 10 and 20 using while loop.
a = 10
while a <= 20:
    if a % 2 == 0:
        print(f"{a} is Even number.")
    else:
        print(f"{a} is odd number.")
    a += 1

# Write a program to print 1 to 10 using the do-while loop statement.
i = 1
print("Print 1 to 10 using the do-while loop statement:")
while True:
    print(i)
    i += 1
    if i > 10:
        break

# Write a program to find Armstrong number or not.
num = int(input("\nEnter a number to check if it is an Armstrong: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    cube = digit ** 3
    sum += cube
    temp //= 10

if sum == num:
    print("It is an armstrong number.\n")
else:
    print("It is not an armstrong number.\n")

# Write a program to find the prime or not.
num = int(input("Enter a number to check if it is Prime: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number.\n")
            break
    else:
        print(f"{num} is a prime number.\n")
else:
    print(f"{num} is not a prime number")

# Write a program to palindrome or not.
num = int(input("Enter number to check palindrome or not: "))
temp = num
reverse = 0
while(num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if(temp == reverse):
    print("The number is a palindrome!\n")
else:
    print("The number isn't a palindrome!\n")

# Program to check whether a number is EVEN or ODD using switch.
num = int(input("Enter a number to check if it is Prime: "))

def is_even():
    print(f"{num} is EVEN\n")
def is_odd():
    print(f"{num} is ODD\n")

switch = {
    0: is_even,
    1: is_odd,
}
switch[num % 2]()

# Print gender (Male/Female) program according to given M/F using switch.
print("Check Input gender is Male or Female(M/F): ")
gender_char = 'F'  

def male():
    print("Male")
def female():
    print("Female")
def invalid():
    print("Invalid input")

switch = {
    'M': male,
    'F': female
}

switch.get(gender_char, invalid)()
