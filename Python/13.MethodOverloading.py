# Write two methods with the same name but different number of parameters of same type and call the methods.
class Calculator:
    def addition(self, a, b, c = 0):
        return a + b + c

calc = Calculator()
result1 = calc.addition(12, 12)
print(f"Result of 2 parameters is {result1}.")
result2 = calc.addition(12, 12, 12)
print(f"Result of 3 parameters is {result2}.\n")

# Write two methods with the same name but different number of parameters of different data type and call the methods.
class different_overloading:
    def input_checker(self, is_input):
        if type(is_input) is str:
            print(f"{is_input} is string data.")
        elif type(is_input) is int:
            print(f"{is_input} is as integer data.\n")

display_object = different_overloading()
display_object.input_checker("Hello World")
display_object.input_checker(1398918)

# Write two methods with the same name and same number of parameters of same type.
class mixed_overloading:
    def same_parameters(self, value):
        if type(value) is int:
            self.integer_method(value)
        elif type(value) is str:
            self.string_method(value)
        else:
            print("Unsupported Datatype!")
    
    def integer_method(self, value):
        print("Integer method executed.")

    def string_method(self, value):
        print("String method executed.\n")

mixed = mixed_overloading()
mixed.same_parameters(1398918)
mixed.same_parameters("Hello World")