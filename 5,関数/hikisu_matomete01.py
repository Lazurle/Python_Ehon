# 引数をまとめて受け取る

# タプルや辞書の仕組みを使って、引数をまとめて受け取る方法
#    仮引数の前に「*」を付けると、引数をタプルとして受け取る
#    仮引数の前に「**」を付けると、引数を辞書として受け取る
def avg(*args):
    sum = 0
    for n in args:
        sum = sum + n
    return sum / len(args)

tuple = (1, 3, 5, 7)
# average1 = avg(tuple)
print( avg(1, 2, 3, 4) )
# print('平均は:', average)


# sum()メソッドで簡単にタプルの合計を出せたりする。
# mean()メソッドでも簡単に直接平均を求められたりする、便利
def avg2(*args):
    return sum(args) / len(args)
print( avg2(1, 2, 3, 4) )


def avg3(args):
    return sum(args) / len(args)
print( avg3(tuple) )


# 辞書
def printDic(**args):
    for s, t, in args.items():
        print( s, ':', t )

printDic(a = 20, b = 30, c = 50)
