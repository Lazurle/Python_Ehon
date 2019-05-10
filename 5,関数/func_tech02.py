# 関数オブジェクト
#    関数の最後に()を付けずに、名前だけ書いたものは関数そのものを表す。
#    これを関数オブジェクトという。
def printHello(name):
    print('Hello', name)

# 関数そのものを返して代入
func = printHello
func('野獣先輩')

# 関数のネスト
#  関数の中に関数を定義することが可能、内側の関数の事を"ローカル変数"という。
def funcA():
        def funcB():
            print('funcB()が呼び出されました。')
    print('funcA()が呼び出されました。')
    funcB()

funcA()
