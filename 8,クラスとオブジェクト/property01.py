# ◆ プロパティ(1)
# Pythonのフィールドはどこからでも参照したり代入できたりするが、
# プロパティを使えばこれらを管理できる。

# プロパティ…
#    オブジェクト内にあるフィールドの値を取得、設定、削除するメソッドを考える。
#    これらの機能を持った変数のようなものをプロパティという
#    getter, setter, deleterなど
# privateフィールド
# privateにしたい場合は、「__」を変数の先頭に着ける。

# ◆ プロパティの定義
class Book:
    def __init__(self, t, p):
        self.title = t
        self.__price = p # 先頭に「__」を付けて隠蔽します。
    def getPrice(self):#ゲッター
        return self.__price
    def setPrice(self, p):#セッター
        self.__price = p
    def delPrice(self):
        self.__price = 0
    price = property(fget=getPrice, fset = setPrice, fdel = delPrice, doc = "価格のプロパティ")
    # property()関数、プロパティを作成する。
    # 引数をすべて定義する必要はない、例えばfgetだけを定義すると読み取り専用の
    # プロパティを作ることが可能。

book1 = Book('絵本', 1680)
print( book1.getPrice() )
book1.price = 2000 # プロパティの設定 = セッターメソッドの呼び出し
print( book1.price ) # ゲッターメソッドの「呼び出し
del( book1.price ) # デリーターメソッドの呼び出し
