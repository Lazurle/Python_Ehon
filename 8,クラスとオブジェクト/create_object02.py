# ◆ コンストラクタ
# オブジェクトの生成時、自動的に呼び出される特殊なメソッド
class Book:
    def __init__(self, t, p): # コンストラクタ、メソッド名は必ず「__init__」にします。
        self.title = t
        self.price = p

    def printPrice(self, num):
            print(self.title, ":", num, "冊で", (self.price * num), "円")

book1 = Book("絵本", 1680)
book1.printPrice(2)
