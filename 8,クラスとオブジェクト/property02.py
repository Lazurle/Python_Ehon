# ◆ プロパティ(2)
#   デコレータを使った定義方法を紹介します。
#   Pythonには「デコレータ」という、@で始まる特別な機能を持ったキーワードがあります。
class Book:
    def __init__(self, t, p):
        self.title = t
        self.__price = p # private変数

    @property # プロパティの宣言とゲッターメソッドの定義
    def price(self): # ゲッターメソッド, プロパティ名がpriceになる。
        return self.__price

    @price.setter # セッターメソッドの定義（プロパティ名.setter）
    def price(self, p):
        self.__price = p

    @price.deleter # デリーターメソッドの定義（プロパティ名.deleter)
    def price(self):
        self.__price = 0

book1 = Book("絵本", 1680)
book1.price = 2000
print( book1.price )
del( book1.price )
