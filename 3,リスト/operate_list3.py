# ◆ リストの操作 ◆

# リストのソート
# list.sort()で昇順に並び替えます。
a = [52, 3, 80, 1, 17]
a.sort()
print(a)

# reverse = trueを入れると降順で並べ替えを行う事が可能
a.sort(reverse = True)
print(a)

# sorted()は元のリストはそのままに並べ変えた結果を別のリストとして返します。
b = [30, 45, 1, 4, 80]
print(b)
c = sorted(b)
print(c)
