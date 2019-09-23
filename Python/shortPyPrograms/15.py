#overriding  super()
class Funky:
    a=10
    def groove(self):
        print("Hi in Funky")

class Donkey(Funky):
    def groove(self):
        super().groove()# first it will run funky method after that it will run current method
        print("Hi in donkey")
        a=11
        print(super().a)
        print(a)
    

a_donkey = Donkey()
a_donkey.groove()

