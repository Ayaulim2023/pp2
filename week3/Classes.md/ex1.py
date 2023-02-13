class MyClass:
    def __init__(self):
        self.s=""
    
    def get_string(self):
        self.s=input()
    
    def print_string(self):
        print(self.s.upper())

str = MyClass()
str.get_string()
str.print_string()