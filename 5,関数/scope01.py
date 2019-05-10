# 変数のスコープ
#   関数の中で使っている変数をローカル変数という。
#   関数の外側で定義している変数をグローバル変数という。

# 非ローカル変数の変更
a = 'グローバル変数a'
def funcA():
    a = 'funcA()の変数a'
    b = 'funcA()の変数b'
    def funcB():
        b = 'funcB()の変数b'
        c = 'funcB()の変数c'
        print(a, b, c)
    funcB()
    print(b)

funcA()
print(a)

# 関数の外側の変数を変更したいときは、globalまたはnonlocalを使って、
# 変数が非ローカルである事を宣言する必要がある。
a = 0
def funcA():
    global a
    a = 1
    b = 2
    def funcB():
        nonlocal b
        b = 2
        c = 2
        print(a, b, c)
    funcB()
    print(b)
funcA()
print(a)
