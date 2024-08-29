# Different ways creating a string 
string = "I am Groot"
print(string)

string1 = 'Programming '
print(string1)

string2='''World'''
print(string2)

string3 = """I
AM
Ironman"""
print(string3,"\n")

# Concatenating two strings using + operator 
str1 = string1 + string2
print(str1)

# Finding the length of the string 
print("length of the string:",len(str1))

# Extract a string using Substring 
# Searching in strings using index() 
string1 = "Ironman"
string2 = "man"
print("\n",string1)
print("Position of man:",string1.index(string2),"\n")

# Matching a String Against a Regular Expression With matches().
import re
is_match = "James"
string = "Bond James Bond"
match =re.search(is_match, string)

if match:
    print("Match found:",match.group())
else:
    print("\nMatch not found:\n")

# Comparing strings.
string1 = 'Anthony Stark'
string2 = 'Morgan Stark'
string3 = string1
print(string1 == string2)
print(string1 == string3)
print(string2 == string3)
print(string1 != string2,"\n")

# startsWith(), endsWith() and compareTo() 
string1 = "Wade Winston Wilson"
print(string1.startswith("Wade"))
print(string1.endswith("son"),"\n")

# Trimming strings with strip()
string1 = "Hello World python"
print(string1.strip("python"),"\n")

# Replacing characters in strings with replace()
string1 = 'Hi World'
print(string.replace("Hi","Hello"),"\n")

# Splitting strings with split()
string1 = 'hi-hello-bye'
print(string1.split("-"),"\n")

# Converting integer objects to Strings.
num = int(input("Enter number to be typecast as string: "))
str_num = str(num)
print("Number has been converted to string:",str_num,type(str_num),"\n")

# Converting to uppercase and lowercase.
input = "Deadpool"
print(input)
lowercase = input.lower()
uppercase = input.upper()
print("Lowercase input: ",lowercase)
print("Uppercase input: ",uppercase)