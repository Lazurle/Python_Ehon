# ◆ ファイルへの書き出し
# テキストファイルに文字を書き出してみる

# ◆ 文字列の書き出し
#       ファイルに文字列を書き出すには、以下のようにします。
f = open('bye.txt', 'w')
n = f.write('さようなら　\n しおりさん\n')
f.close()
# result
# さようなら　
#  しおりさん

# ◆ with を使った書き方
print( '# ◆ with を使った書き方' )
# ファイルの読み書きでは最後にclose()メソッドを呼び出す必要がありますが、
# オブジェクトの後始末を自動で行ってくれるwithを使って、次の様に
# 描くことで、close()を省略することが可能です。

## 読み込み
f = open('hello.txt', 'r')
for r in f:
    print( r.strip() )
f.close()
# ↓ withを使ってこのように書ける ↓
with open('hello.txt', 'r') as f:
    for r in f:# 上の行かいたらインデント
        print( r.strip() )
## 書き出し
f = open('File2.txt', 'w')
f.write( 'File2' )
f.close()
# ↓ withを使ってこのように書ける ↓
with open('File3.txt', 'w') as f:
    f.write( 'File2' )

# ◆ 文字エンコーディングの指定
# codecsクラスを利用する
##ファイルの読み込み
# codecsモジュールのopen()関数を呼び出します。
import codecs

f = codecs.open('hello.txt', 'r', 'Shift-JIS')
for r in f:
    print( r.strip() )
f.close()

## ファイルの書き出し
import codecs

f = codecs.open('bye8.txt', 'w', 'UTF-8')
f.write('さようなら\n しおりさん')
f.close()
