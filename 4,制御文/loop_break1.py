# 　ループの中断
a = 0
b = 5
while (a < 6):
    if (b - a) <= 0: # aが5以上になったらwhileループを抜ける。
        print('breakで抜けました')
        #elseもwhileの処理なので、whileの後のelseも飛ばしてbreakする。
        break
    print('aの値は… ', a)
    print('b-aは… ', b - a)
    a += 1
else:
    print('while条件で抜けました。')

# 　continue文
# やっている処理を中断して、そこからまた最初から処理をする
li = [1, 3, 5, '七', 9]
for a in li:
    if type(a) == str:#aのタイプが文字列ならば
        print(a, '数値ではなく文字列です。')
        continue # 18行目のfor文に戻る
    print(a)

# メソッドを抜ける：return
# ループを抜ける：break
# プログラムを終了するquit()
