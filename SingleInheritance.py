class BaseClass:
    def BaseMethod(self):
        print("This is a BaseClass")
class DerivedClass(BaseClass):
    def derivedMethod(self):
        print("This is a DerivedClass")
obj = DerivedClass()
obj.BaseMethod()
