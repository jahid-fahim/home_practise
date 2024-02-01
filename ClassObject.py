class DemoClass:
    a = 10
    def __init__(self):
        print("Welcome into constructor.")
    def display(self):
        print(self.a)

obj = DemoClass()
obj.display()
