#abstract methods
from abc import ABC,abstractmethod

class A(ABC): # ABC se inherit karna zarori hai
    @abstractmethod
    def compulsoryMethod(self):
        return 1
class B(A):
    def compulsoryMethod(self):
        return 2
    # def tp(self):
    #     return 2
b = B()
print(b.compulsoryMethod())