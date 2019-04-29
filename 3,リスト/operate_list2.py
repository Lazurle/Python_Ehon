# ◆ リストの操作(2) ◆

# 要素を削除する
# 削除する場合はlist.pop(箇所)またはlist.del(箇所)で削除できます
a = ['tea', 'coffee', 'soda', 'milk', 'juice']
print(a)
a.pop(2)
print(a)

# 要素XXを削除する
# 削除する場合はlist.remove(XX)で削除可能です
a.remove('coffee')
print(a)

# リストを変数に分割する
x, y, z = a
print(x, y, z)

#['tea', 'coffee', 'soda', 'milk', 'juice']
#['tea', 'coffee', 'milk', 'juice']
#['tea', 'milk', 'juice']
#tea milk juice
