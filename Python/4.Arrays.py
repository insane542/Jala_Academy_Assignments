# Write a function to add integer values of an array.
def sum_of_array_elements(array):
    sum = 0
    for i in range(0, len(array)):
        sum += array[i]
    print(f"Sum of elements in array is {sum}.\n")

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array)
sum_of_array_elements(array)

# Write a function to calculate the average value of an array of integers.
def find_average(array):
    sum = 0
    for i in range(0, len(array)):
        sum += array[i]
        avg = sum / len(array)
    print(f"Averrage of elements in array is {avg}.")

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array)
find_average(array)

# Write a program to find the index of an array element
array = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print()
for i in range(0,len(array)):
    print(f"Index: {i}, Element: {array[i]}.")
print()

# Write a function to test if array contains a specific value.
def element_in_array(array, num):
    for i in range(0, len(array)):
        if num == array[i]:
            print("This number is present in the array.")
            return
    print("This number is not present in the array.")

num = int(input("Enter a number to check if it is in array: "))
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
element_in_array(array, num)

# Write a function to remove a specific element from an array.
def remove_element(array, element):
    while element in array:
        array.remove(element)
    print(array)
    
element = int(input("Enter number to eliminated from array: "))
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array)
remove_element(array, element)

# Write a function to copy an array to another array.
def copy_array(array, copy):
    for i in range(len(array)):
        copy.append(array[i])
    print(f"copy_array = {copy}")

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"array = {array}")
copy = []
copy_array(array,copy)

# Write a function to insert an element at a specific position in the array.
array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
array.insert(11,110)
print(array)

# Write a function to find the minimum and maximum value of an array.
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mimimum = array.index(min(array))
print("\nMinimum element in this array is present at ",mimimum)

maximum = array.index(max(array))
print(f"Minimum element in this array is present at {maximum}.\n")

# Write a function to reverse an array of integer values.
def reverse_array(array):
    start = 0
    end = len(array) - 1
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"array: {array}")
reversed_array = reverse_array(array)
print("Reversed array:", reversed_array)

# Write a function to find the duplicate values of an array 
def find_duplicate(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                print("Found duplicate value:",array[j])

array = [4, 3, -7, 1, 3, 3, 1, -4]
find_duplicate(array)

# Write a program to find the common values between two arrays
def find_common_values(array1, array2):
    common_values = []
    for value in array1:
        if value in array2:
            common_values.append(value)
    return common_values

array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
common_values = find_common_values(array1, array2)
print("Common values:", common_values)

# Write a method to remove duplicate elements from an array.
array = [10, 20, 30, 20, 60, 10, 20, 50, 30, 90]
print("\nArray =",array)
new_array = []
for i in array:
    if i not in new_array:
        new_array.append(i)
print(new_array)

# Write a method to find the second largest number in an array.
array = [57, 20, 55, 1, 62, 37, 56, 86, 98, 73]
print("\nArray =",array)
sorted = []
while array:
    max_element = array[0]
    for i in array:
        if i > max_element:
            max_element = i
    sorted.append(max_element)
    array.remove(max_element)
print("Sorted array =",sorted)
print("Second Largest element in array =",sorted[1])

# Write a method to find number of even number and odd numbers in an array.
array = [11, 39, 90, 64, 95, 95, 75, 87, 87, 14]
print("\nArray =",array)
Even = []
Odd = []
i = 0
while i < len(array):
    if array[i] % 2 == 0:
        Even.append(array[i])
    else:
        Odd.append(array[i])
    i += 1
print("Even number =",Even)
print("Odd number =",Odd)

# Write a function to get the difference of largest and smallest value.
def difference_of_largest_and_smallest(array):
    max_value = array[0]
    min_value = array[0]

    for i in array:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i
    print("Largest value:", max_value)
    print("Smallest value:", min_value)
    
    difference =  max_value - min_value
    return difference

array = [28, 55, 18, 66, 18, 67, 13, 94, 46, 57]
print("\nArray =",array)
result = difference_of_largest_and_smallest(array)
print("Difference between largest and smallest value in array is",result)

# Write a method to verify if the array contains two specified elements(12,23)
array = [12, 51, 58, 48, 23, 47, 90, 52, 96, 55]
print("\nCheck if 12 and 23 are present in array",array)
i = 0
while i < len(array):
    if array[i] == 12 or array[i] == 23:
        print(f"{array[i]} Present in array.")
    i += 1

# Write a program to remove the duplicate elements and return the new array.
array = [92, 90, 65, 82, 82, 90, 14, 14, 65, 92]
print("\nArray =",array)
unique = []
i = 0
for i in array:
    if i not in unique:
        unique.append(i)
    i += 1
print("New Array =",unique)