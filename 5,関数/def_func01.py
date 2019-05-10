# a + bをしたものを返すプログラム
def add(a, b):
    x = a + b
    return x

def getHello():
    return 'Hello'

# Helloが表示される。
print(getHello())


# return文がない場合は省略可能
def printHello(name):
    print('Hello', name)

printHello('野獣先輩')

#   何もしない関数を作るときは中身にpassと記載する。
# 関数の中にpassがあると、関数の中身がすべて無効になる
def noWork():
    pass

# 実行しても何もしない
noWork()
