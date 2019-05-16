# ◆ クラスの継承
class Book:
    def __init__(self, t, p):
        self.title = t
        self.price = p
    def printPrice(self, num):
        print( self.title, ":", num, "冊で", (self.price * num), "円")

class ColorBook(Book): #
    color = '紫'

book2 = ColorBook("絵本", 1680)
book2.printPrice(514)
