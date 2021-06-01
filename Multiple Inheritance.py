class BaseClass:
    def BaseMethod(self):
        print("This is a BaseClass")
class DerivedClass():
    def derivedMethod(self):
        print("This is a DerivedClass")
class DerivedClass2(BaseClass, DerivedClass):
    def derivedMethod2(self):
        pass

obj = DerivedClass2()
obj.BaseMethod()
obj.derivedMethod()