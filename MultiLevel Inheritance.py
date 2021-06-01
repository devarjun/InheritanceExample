class BaseClass:
    def BaseMethod(self):
        print("This is a BaseClass")
class DerivedClass(BaseClass):
    def derivedMethod(self):
        print("This is a DerivedClass")
class DerivedClass2(DerivedClass):
    def derivedMethod2(self):
        pass
obj = DerivedClass2()
obj.BaseMethod()
