from abc import ABC, abstractmethod


class Abstract_Class(ABC):
    _value = None

    def __init__(self, value):
        self._value = value

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print(f"Value: {self._value}")

class Sub_Class(Abstract_Class):
    def abstract_method(self):
        print("Implement Abstract method from parent.")

    def use_abstract_class(self):
        instance = Sub_Class("Sub class instance of abstract method.")
        instance.abstract_method()
    
    def use_non_abstract_class(self):
        instance = Sub_Class("Sub class instance of non abstract method.")
        instance.non_abstract_method()

def main():
    subClass_instance = Sub_Class("Abstract")
    
    subClass_instance.non_abstract_method()
    subClass_instance.abstract_method()

    subClass_instance.use_abstract_class()
    subClass_instance.use_non_abstract_class()

if __name__ == "__main__":
    main()