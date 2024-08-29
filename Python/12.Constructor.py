class Class1:
    #Default Constructor
    def __init__(self):
        self.name = "Mihir"
    
    def print_class1(self):
        print(self.name)

class Class2(Class1):
    def __init__(self):
        super().__init__()
        self.name = "Mihir Mane"
    
    def print_class2(self):
        print(self.name)

#Public Protected and Private access modifiers
class Class3:
    _name = None                                                        #Public
    _salary = None                                                      #Protected
    _bankAccount = None                                                 #Private

    def __init__(self, name, salary, account):
        self._name = name
        self._salary = salary
        self._bankAccount = account

    def print_name(self):
        print(f"Name: {self._name}")

    def print_salary(self):
        print(f"Salary: {self._salary}")                                

    def print_bank_account(self):
        print(f"Bank Account Number: {self._bankAccount}")
    
    
    def access_print_bank_account(self):
        self.print_bank_account()                                       #Accessing Private data member

class Class4(Class3):
    def __init__(self, name, salary, account):
        super().__init__(name, salary, account)
    
    def access_print_salary(self):                                      #Accessing Protected data member
        self.print_salary()

#instance of class 1
obj1 = Class1()
#instance of class 2
obj2 = Class2()
#instance of class 4 and passing parameters for public, protected and private methods.
obj3 = Class4("Mihir", 35000, "AC1234567890")
obj1.print_class1()
obj2.print_class2()
obj3.print_name()
obj3.access_print_salary()
obj3.access_print_bank_account()