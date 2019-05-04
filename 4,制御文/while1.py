# 　while文

# while 条件:
# 処理
# Pythonにはdo-while文はない

#　 while ~ else
# whileの繰り返しが終わった後に実行する処理をelseブロックで追加可能
a = 0
while (a <= 5):
    print(a)
    a += 1
else:
    print('whileの書き出しが終わりました。')
