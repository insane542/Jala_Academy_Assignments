# Write a program to read text file.
file = open('textfile.txt', 'r')
content = file.read()
print(content)
file.close()

# Write a program to write text to .txt file using  InputStream.
file = open('textfile.txt', 'w')
user_input = input("Enter text to be write in file: ")
file.write(user_input)
file.close()
print("Your text has been updated in text file successfully.")

# Write a program to read a file stream.
with open('textfile.txt', 'r') as file:
    for line in file:
        print(line, end = '')

# Write a program to check whether a file is having read access and write access permissions.
import os
file_path = 'textfile.txt'
is_readable = os.access(file_path, os.R_OK)
is_writable = os.access(file_path, os.W_OK)
print("file is readable? ", is_readable)
print("file is writable? ", is_writable)