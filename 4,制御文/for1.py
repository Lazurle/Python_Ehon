# for文(1)

# for文を使ってリストの値を取り出す。
# リストwを順に取り出してwdayに格納して、それをすべて表示する。
w = ['月', '火', '水', '木', '金', '土', '日']
for wday in w:
    print(wday)

# for文にelseブロックを追加することで、繰り返しが終了したときに実行される処理を指定できる
w2 = ['金', '土', '日']
for wday2 in w2:
    print(wday2)
else:
    print('週末です。')

# for文を使って、辞書の内容を取り出す。
we = {'金':'Fri', '土':'Sat', '日':'Sun'}
# 辞書をそのまま記述すると、キーのみを取得する。
for keys in we:
    print(keys)
# values()メソッドを使うと値を取り出す。
for value in we.values():
    print(value)
# items()メソッドを使って辞書のキーと値のペアをダブルで取得します。
for item in we.items():
    print(item)
