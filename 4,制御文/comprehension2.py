# 　内包表記(2)

# 辞書の内包表記は基本的にリストの内包表記と同じだけど、返す値は「キー：値」のペアが返ってくる。
from random import randint
keys = ['Ichigo', 9, 'Mikan', 25, 'Ringo']
print(keys)
# ['Ichigo', 9, 'Mikan', 25, 'Ringo']

d = { x:randint(1, 100) for x in keys if(type(x) == str)}
# リストから文字列だけを取り出して、辞書を作っている。
print(d)
# {'Ichigo': 7, 'Mikan': 93, 'Ringo': 20}
# 構文にすると以下のようになる
# { キー:値 for 変数 in iterableObject (if 条件式)}

#　 集合の内包表記
a = {1, 4, 5, -1, 9, -2, 10, 9, 15, 4, -5}
print(a)
setA = { x for x in a if(0 < x <= 10)}
print(setA)
