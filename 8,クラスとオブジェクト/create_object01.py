# ◆ オブジェクトの生成
class Book:
    title = '絵本'
    price = 1680
    def printPrice(self, num):
        print(self.title, ':', num, ' 冊で', self.price * num, '円')

book1 = Book()
book1.printPrice(2)
# result
# 絵本 : 2  冊で 3360 円
