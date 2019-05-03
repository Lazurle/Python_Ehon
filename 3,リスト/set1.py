# 集合（セット）

# リストと似ているが、要素に順序がない。
# リストは同じ値を持つことができるが、集合は重複して要素を持つことができない。
a = {'いちご', 'みかん', 'りんご', 'れもん'}
print(a)

# 　ほかの型から集合型（セット）へ変換
seta = set('ABCDE')
# 'ABCDE' → 'A','B','C'……
print(seta)

# リストから集合（セット）へ返還
li = [1, 5, 11, 9, 7, 1]
setb = set(li)
print(setb)

# 集合の要素数を取得する
colorM = {'C', 'M', 'Y', 'K'}
length = len(colorM)
print('集合colorMの要素数は… ', length)

# 値の有無を確認する
swt = {'チョコ', 'クッキー', 'アイス'}
chk = 'クッキー' in swt
print('集合swtに"クッキー"は含まれているか？ -> ', chk)
#chkの中にはBoolean型のTrueが入る
