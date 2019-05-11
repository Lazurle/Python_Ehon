# 基本的な文字列操作(2)

# ◆ 文字列の検索
# find()メソッド … 文字列の中から特定の「文字列の位置」を調べたい場合。
s = 'しんぶんはんばい'
n = s.find('ん')
print(n)
print(type(n))
# 1
# <class 'int'>
print() # 改行

# 検索範囲を限定したいとき。
n = s.find('ん', 2, 5)
# 'しんぶんはんばい'の「ぶんは」の範囲で検索する。
print(n) # 3が出力される
n = s.find('あ')
print( n )
# 指定した文字列が見つからない場合は「-1」が返る。

# ◆ index()メソッド
# index()メソッドはfind()と同じ働きをしますが、文字列が見つからなかった場合は
# エラー「ValueError」になる。
# n = s.index('あ')
# ValueError: substring not found

# ◆ 文字列が含まれているかを調べる(Boolean)
# result = '検索文字列' in 検索対象の文字列
s = 'しんぶんはんばい'
result = 'ん' in s

# ◆ 文字列の個数を調べる。(Integer)
# 文字列が何個含まれているかを調べるにはcount()メソッドを使う。
s = 'しんぶんはんばい'
n = s.count('ん')
print(n)
# 3
