# ◆ クラス変数
class Book:
    title = "絵本"
    price = 1680
    def printPrice(self, num):
        print( self.title, ":", num, "冊で", (self.price * num), "円です")

print( Book.title )
book1 = Book()
book1.title = "辞典"
book1.price = 2000
book1.printPrice(2)

print( Book.title )

# result ->

# 絵本
# 辞典 : 2 冊で 4000 円です
# 絵本

# このようにオブジェクトに依存しない変数の事をクラス変数といいます。
