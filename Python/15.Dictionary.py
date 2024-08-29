#Create a Dictionary with at least 5 key value pairs of the Student ID and Name 
students = {1:"Akash", 2:"Bhavesh",3 :"Devesh", 4:"Eklavya", 5:"Ganesh"}

# Adding the values in dictionary
students[6] = "Harsh"
print("Adding new student Key = 6\n",students)
# Updating the values in dictionary
students[3] = "Dhanashree"
print(f"\nUpdating student with key = 3 from Devesh to {students}")
# Accessing the value in dictionary 
print("\nStudent with key = 2 is",students[2])
# Create a nested loop dictionary
nested_loop_students = {
    1 : {"Sr": 1, "Name":"Akash"},
    2 : {"Sr": 2, "Name":"Bhavesh"},
    3 : {"Sr": 3, "Name":"Devesh"},
    4 : {"Sr": 4, "Name":"Eklavya"},
    5 : {"Sr": 5, "Name":"Ganesh"}
}
print("\nNested Students Dictonary: ",nested_loop_students)
# Access the values of nested loop dictionary 
print("\nSr:No 2, Name:",nested_loop_students[2]["Name"])
print("\nKeys of students: ",students.keys())

del students[4]
print("\nStudents key value = 4. Deleted!\n",students)