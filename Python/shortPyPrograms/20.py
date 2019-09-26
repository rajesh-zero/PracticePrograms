#getter and setter

class A():
    def __init__(self):
        self.x=1
    @property
    def y(self):
        return self.x
    @y.setter
    def y(self,string):
        self.x = string
a = A()
a.y="hello bro"
print(a.y)