# Define a static variable and access that through a class, through a instance, change within the instance, change within the class.
class Python:
    staticVariable = 9

print("Access through class:", Python.staticVariable)

#change within the class
Python.staticVariable = 12
print("After changing through class:", Python.staticVariable)  # Gives 12

# through instance
instance = Python()
print("Access through instance:", instance.staticVariable)  # Gives 12

# change within instance
instance.staticVariable = 15
print("After changing through instance (instance.staticVariable):", instance.staticVariable)  # Gives 15
print("Access through class after instance change:", Python.staticVariable)  # Still gives 12