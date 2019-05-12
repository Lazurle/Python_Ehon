# ◆ 正規表現による置換と積分
# 正規表現を使ってマッチした文字列を別の文字列に置換したり、
# マッチした文字列で分割する方法を見ていきます。

# ◆ 正規表現による置換
# 正規表現で検索した文字列を別の文字列に置換するには
# sub()メソッドを使います。
import re
s1 = 'Python Fang'
s2 = re.sub('[A-Z].{2}', '野獣先輩', s1)
# sub() … マッチした文字列を置換します。
# '[A-Z].{2}' … 検索するパターン、この場合は「英大文字＋任意の２文字」を表します。
# '野獣先輩' … 置換後の文字列
# s1 … 置換対象の文字列
print( s1 )
print( s2 )
# result
# Python Fang
# 野獣先輩hon 野獣先輩g

# ◆ 正規表現による分割
# 正規表現で表される文字列によって文字列を分割するには
# split()メソッドを使います。結果はリストで得られる。
import re
s = 'Learn Python, Shiori'
mlist = re.split('.n', s)
print( s )
print( mlist )
# result
# Learn Python, Shiori
# ['Lea', ' Pyth', ', Shiori']
