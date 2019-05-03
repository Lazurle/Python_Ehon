# for文(2)

#　 range()を使った繰り返し
# range()レンジ を使うことで、あらかじめ何かに値を格納しなくても、指定した範囲のぶんだけ数値を作成できる。
for a in range(7):
    print(a)
# result
# 0 1 2 3 4 5 6
# (7は含まれない)

print() # 改行

# 開始値、終端値、ステップ（増加量）を指定したりして、特定の範囲の値を得ることもできます。
for a in range(10, 5, -1):
    print(a)
# result
# 10 9 8 7 6

print() # 改行
for a in range(20, 31, 2):
    print(a)
# result
# 20 22 24 26 28 30

# 　range()を使ったリストの作成
li = list( range(20, 31, 2) )
