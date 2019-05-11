# ◆ パターンマッチ(1)
# 文字列がパターンと一致することを「マッチする」、
# 一致しないことを「マッチしない」といい、
# マッチするかどうか調べることを「パターンマッチ」という。
# パターンマッチを行うにはmatch()関数を使います。
import re # 正規表現を利用するためにreモジュールをインポート。
s = 'Learn Python' # 評価する文字列

mobj = re.match('Le', s)
# match()関数、第1引数のパターンが第2引数の文字列にマッチすれば、
# マッチング情報を持つオブジェクトを返します
# マッチしない場合はNoneを返す。

# mobjはマッチングオブジェクト
print(type(mobj))# <class 're.Match'>
if mobj:
    print( mobj.group() )
    # group()メソッドはマッチングオブジェクトからマッチした文字列を取り出す。
# 出力結果 -> Le

# なお、match()によるマッチングは文字列の先頭から一致するかを評価する。
# 途中の文字列で一致してもマッチしたとはみなされません。
# 途中からでもマッチされたいときは、search()関数を使う。
# 使い方はmatch()と同じ
mobj = re.search('Py', s)
if mobj:
    print( mobj.group() )
# 出力結果 -> Py

# ◆ マッチした文字列だけでなく、マッチングオブジェクトからは範囲も取り出せる。
# マッチした文字列の先頭インデックスを取得する
print( mobj.start() )
# result -> 6

# マッチした文字列の末尾のインデックスに１を足したものを取得する。
print( mobj.end() )
# result -> 8

# 上記インデックスを要素とするタプルを取得する
print( mobj.span() )
# result -> (6, 8)


# ◆ パターンのコンパイル
# 同じパターンでいろいろな文字列を評価したいときは、
# パターンをコンパイルした正規表現オブジェクトを作っておくと、
# マッチングが高速にできる。
import re
s = 'Learn Python'

# compile()関数 -> パターンをコンパイルして正規表現オブジェクトを返す
reobj = re.compile('Le')
mobj = reobj.match(s)
if mobj:
    print( mobj.group() )
# result -> Le


# ◆ 大文字と小文字の区別
# 大文字と小文字を区別せずにマッチさせたいときは、次の様に書きます。

# コンパイルなし
mobj = re.match('Le', s, re.IGNORECASE)
# コンパイルあり
reobj = re.compile('Le', re.IGNORECASE)
