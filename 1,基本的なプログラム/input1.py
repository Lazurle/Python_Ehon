# 文字列を入力する
name = input('あなたのお名前は？:')
print('こんにちは！' + name + 'さん')

a = '24'
print(a + '歳学生です。')
#Javaのように使うには文字列じゃないとだめ

# Pythonでは標準出力と標準エラー出力に値を書き込むには、次のように書きます。
import sys
sys.stdout.write('標準出力です \n')
sys.stderr.write('標準エラー出力です \n')

sl = sys.stdin.readline()
#readLine()ではなく、readline()

# readlines() 複数行取得して、リストとして返す
# read() 複数行取得して、文字列として返す。

# sep=''とend=''
# sep=''は「,」による空白区切りなしで詰めてくれる。
# end=''はprintの改行をなくしてくれる
print('a', 'b', 'c', sep='', end='')
print('d', 'e', 'f', sep='')
# result
# abcdef
