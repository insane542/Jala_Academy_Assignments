# A, B and C are classes
# Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C
class A:
    # A is a super class
    def method_1A(self):
        print("Method 1 inside class A")
    def method_2A(self):
        print("Method 2 inside class A")
    def override_method(self):
        print("Override method in class A")

class B(A):
    # B is a sub class of A.
    def method_1B(self):
        print("Method inside class B")
    def method_2B(self):
        print("Method 2 inside class B")
    def override_method(self):
        print("Override method in class B")

class C(B):
    # C is a sub class of B
    def method_1C(self):
        print("Method 1 inside class C")
    def method_2C(self):
        print("Method 2 inside class C")
    def override_method(self):
        print("Override method in class C")

class Main:
    # class with main method
    def main():
        # Object for each class A, B and C and call every method of each class using its own instance.
        a = A()
        a.method_1A()
        a.method_2A()
        a.override_method()
        b = B()
        b.method_1B()
        b.method_2B()
        b.override_method()
        c = C()
        c.method_1C()
        c.method_2C()
        c.override_method()
        
        # Call an overridden method with super class reference to B and C class’s objects 
        a_reference_b = A()
        a_reference_b = b
        a_reference_b.override_method()

        a_reference_c = A()
        a_reference_c = c
        a_reference_c.override_method()


if __name__ == "__main__":
    Main.main()