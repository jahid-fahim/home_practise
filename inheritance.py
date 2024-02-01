class A:
    def showA(self):
        print("In class A")

class B(A):
    def showB(self):
        print("In class B")

obj = B()
obj.showA()