# リストの操作(1)

# ◆ 要素を追加する ◆
# append()メソッドで末尾に要素を追加できる。
a = [1, 2, 3]
print(a)
a.append(4)
print(a)

# 特定の箇所に挿入したい時は、insert()メソッドで可能
a.insert(1, 114514)
# a[1]に2がはいる
print(a)

# ◆ リストを連結する ◆
list1 = ['red', 'blue', 'yellow']
list2 = ['white', 'black']
print(list1)
print(list2)
list3 = list1 + list2
print('連結したlistは', list3)

temp_list = list2
list1 = list1 + list2
print(list1)
# list1.extend(list2)とlist1 = list1 + list2, list1 += list2は同義
