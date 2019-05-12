# ◆ ファイルの読み込み

# １行ずつ読み込む
f = open('hello.txt', 'r')
for r in f:
    print( r.strip() )
f.close()
# r には１行ずつ文字列が入る。（改行も含む）
# そしてその末尾の改行をstrip()で削除する。
# result
# [.txt は Shift-JIS]
# 野獣先輩


# ◆ いろいろな読み込み
f = open('hello.txt', 'r')
s1 = f.readline() # readline() １行読み込みます。（改行も含む）
s2 = f.readline() # ２回目の呼び出しは、次の文字から。
print( s1.strip() )
print( s2.strip() )
f.close()

# ◆ 指定文字数だけ読み込む
f = open('hello.txt', 'r')
print( f.read(3) )# read(3)引数を指定すると、その文字数文読み込む
f.close()
# result
# [.t

# ◆ 一度に全部読み込む
f = open('hello.txt', 'r')
print( f.read() )# read()で引数を指定しない場合、ファイルを全部読み込んでくれる
f.close()

# ◆ リストに読み込む
print( ' ◆ リストに読み込む' )
f = open('hello.txt', 'r')
l = f.readlines()

print('l[0]は… ', l[0].strip() )
print('l[1]は… ', l[1].strip() )

f.close()
# result
#  ◆ リストに読み込む
# l[0]は…  [.txt は Shift-JIS]
# l[1]は…  野獣先輩

## list()メソッドを使って、次の様に使える。
f = open('hello.txt', 'r')
l = list(f)
print( l[0].strip() )
f.close()
