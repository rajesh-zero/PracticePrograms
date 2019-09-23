#overriding  super()
class Funky:
    def groove(self):
        print("Hi in Funky")

class Donkey(Funky):
    def groove(self):
        super().groove()# first it will run funky method after that it will run current method
        print("Hi in donkey")
    

a_donkey = Donkey()
a_donkey.groove()

