# ◆ パターンマッチ(2)
# match()やsearch()で取り出せるマッチング文字列は１つ。
# ここでは複数個取り出す方法を紹介します。
import re # 正規表現を使うのでインポート

# ◆ 最短マッチと最長マッチ

## 最長マッチ
re.match('L.*n', 'Learn Python').group()# -> Learn Python
# 「.」は任意の１文字、「*」は１文字前のを０回以上繰り返す

## 最短マッチ
re.match('L.*?n', 'Learn Python').group()# -> Learn
# 「?」は直前の文字列の０回、または１回の繰り返し

# ◆ マッチしたすべての文字列を得る
# findall()メソッドを使うと、パターンにマッチした文字列をリストで得ることができます。
s = 'Learn Python'
mlist = re.findall('.n', s)# findall関数 マッチした文字列のリストを返す。
# '.n' -> rn, onがマッチ
# mlist にはmlist[0] = 'rn', mlist[1] = 'on'

# ◆ マッチしたすべての文字列とその位置情報を得る。
# 位置情報も取り出したいときは、
# finditer()メソッドを使う。
import re
s = 'Learn Python'
miter = re.finditer('.n', s)
for mobj in miter:
    print( mobj.group() )
    print( mobj.span() )
    # monj -> マッチングオブジェクト
    # miter -> イテレータオブジェクト, forなどの繰り返し制御文とともに用いる
    #          ことで、マッチングオブジェクトを取得可能。
# result
# rn
# (3, 5)
# on
# (10, 12)

# イテレータは因みに日本語では、反復子と訳されます。
