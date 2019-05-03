# 辞書の操作(2)

# 　辞書のキーのリストを作る
# 辞書のキーだけを取り出して取得するにはkeys()メソッドを使います。
a = {'PS3' : 30, 'PS4' : 3, 'PS2' : 50}
key = list( a.keys() ) # すべてのキーを取り出して、取り出したキーをリストに変換

print(a)
print(key)
# 辞書の値だけのリストを作る場合はvalues()メソッドを使います。
value = list( a.values() )
print('valueの中身は… ', value)

# 辞書の要素（キーと値）を取り出して取得するにはitems()メソッドを使う。
item = list( a.items() )
print('itemの中身は… ', item)
