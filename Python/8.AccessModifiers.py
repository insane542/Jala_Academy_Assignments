class Parent:
    _var1 = None
    _var2 = None
    _var3 = None

    def __init__(self, var1, var2, var3):
        self._var1 = var1
        self._var2 = var2
        self._var3 = var3
    
    def public_member(self):
        print("Public Data Member: ",self._var1)
    
    def protected_member(self):
        print("Protected Data Member: ",self._var2)
    
    def private_member(self):
        print("Private Data Member: ",self._var3)
    
    def access_private_member(self):
        self.private_member()

class Child(Parent):
    def __init__(self, var1, var2, var3):
        Parent.__init__(self, var1, var2, var3)
    
    def access_protected_member(self):
        self.protected_member()
    
    def access_private_member_child(self):
        self.access_private_member()

def main():
    parent_object = Parent("Public Value", "Protected Value", "Private Value")
    parent_object.public_member()
    parent_object.protected_member()
    parent_object.private_member()

    child_object = Child("Public Value", "Protected Value", "Private Value")
    child_object.public_member()
    child_object.access_protected_member()
    child_object.access_private_member_child()
    print("Object is accessing protected member:", child_object._var2)

if __name__ == "__main__":
    main()