# if文(1)
a = 5
if a % 2 == 0:
    # true(余りが０ならば)
    print(a, 'は偶数です。')
else:
    print(a, 'は奇数です。')
# if 条件:
#       処理
# else:
#       処理
#Pythonではインデントで処理を分けている。この処理の固まりを「ブロック」という。

# if文(2)
#  連続したif文
b = 1000
print(b, 'は')
if (0 <= a) & (a <= 9):
    print('1桁の数字です。')
elif (10 <= a) & (a <= 99):
    print('2桁の数字です。')
elif (100 <= a)&(a <= 999):
    print('3桁の数字です。')
else:
    print('4桁以上です。')
