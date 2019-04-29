# 書式の指定方法

# 整数を表示する書式設定
a = 3
print('{:d}'.format(a))

# 3桁の区切り
a = 123456789
print('{:,}'.format(a))
# result
# 123,456,789

# 右詰めで4文字で表示
print('{:>4}'.format(25))
# result
# __25

# 左詰めで4文字で表示
print('{:<4}'.format(25))
# result
# 25__

# 中央に4文字で表示
print('{:^4}'.format(25))
# result
# _25_

# 例
a = 10
b = 3.14
print('{:>10}'.format(a))
print('x{:>9.3}'.format(b))
print('-' * 10)
print('{:>10.5f}'.format(a * b))
# result
#________10
#x_____3.14
#------------
#  31.40000
