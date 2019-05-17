# ◆ クラスメソッド
# クラスメソッドはオブジェクトによらず、同じクラスであれば同じ動きをするメソッドの事です。
class Book:
    @classmethod
    def printMaxNum(cls): # 自分自身のクラスを表します。
        print(20)#オブジェクトにい依存しない処理を書きます。

Book.printMaxNum() # クラス名、クラスメソッド名の形式で呼び出す
