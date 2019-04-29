# 論理演算子

# and(かつ)
# 使い方：(a >= 10) and (a < 50)
# 訳：aは１０以上かつ、５０未満
a = 40
print('aは', a, 'である。')
print('aは10以上かつ50未満か？：', (10 <= a)and(a < 50) )
# result
# aは 40 である。
# aは10以上かつ50未満か？： True

# or(または)
# 使い方：(a == 1)or(a == 100)
# 意味：aが1または100の場合trueを返す

# not(～ではない)
# 使い方：not(a == 100)
# 意味：aが100でない場合trueを返す。

# 三項演算子
point = 90
a = '合格' if point > 75 else '不合格'
print('pointの点数は%dで ' % point, end='')
print(a ,"です。")
