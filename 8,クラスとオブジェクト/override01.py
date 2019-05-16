# ◆ オーバーライド
# オーバーライドとは継承したメソッドと同じ名前のメソッドを記述して、メソッドを上書きすることです。
class Book:
    def __init__(self, t, p):
        self.title = t
        self.price = p
    def printPrice(self, num):
        print( self.title, ":", num, "冊で", (self.price * num), "円")
class ColorBook(Book):
    color = '紫'
    def printPrice(self, num):
        print( self.title, ":", num, "冊で", self.price * num, "円")
        print( self.color )

book2 = ColorBook('絵本', 1680)
book2.printPrice(22)

# Pythonにはオーバーロードはない
# ◆ スーパークラスのメソッド参照
def printPrice(self, num):
    super().printPrice(num)
    print( self.color )
