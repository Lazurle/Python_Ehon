# 文字列の連結

print('夏' + '休み')

a = '夏'
b = '休み'
c = a + b
print(c)

# a + bでも連結可能
# print()ないで文字列同士連結も可能。


# 「*」演算子を使うと、文字列を指定した回数分、繰り返して表示する。
a = 'Hey! \n'
b = a * 3
print(b)
# 出力結果
# Hey!
# Hey!
# Hey!

# 文字列中の文字の参照
# 0123456
# package
# 7654321(-1)
a = 'package'
print(a[2])
print(a[-1])
# 出力結果
# c
# g
