# format()メソッド

print('東京は{}位です。'.format(3))
a = 3
print('東京は{}位です。'.format(a))
# result
# 東京は3位です

# 改行
print('\n')

# 複数のデータを表示する時
a = '東京'
b = 3
print('{}は{}位です。'.format(a, b))
# result
# 東京は3位です。

print('{1}位は{0}です。'.format(a, b))
# 順番を指定する事も可能

# f文字列
# f'{値}'
print(f'{a}は{b}です。')
print('aaa' + a)
