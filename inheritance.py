class A:
    def showA(self):
        print("A")

class B:
    def showB(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.showA()
obj.showB()