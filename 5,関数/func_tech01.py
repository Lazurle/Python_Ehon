# 関数のテックニック
#   デフォルト引数は右側から複数設定可能
def multiply(n, t = 2):
    x = n * t
    return x

a = multiply(18782)
print(a)

# OKな例
def func1(a, b = 1, c = 2):
    pass
# NGな例(エラー出る)
def func2(a, b = 2, c):
    pass
