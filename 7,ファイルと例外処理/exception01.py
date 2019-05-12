# ◆ 例外処理

# ◆ 例外処理の方法
# try:
#     例外が起こりそうな処理
#except 例外クラス名 as 変数名:
    # except ZeroDivisionError as e
    # すべての例外をキャッチして、例外情報が必要ないときは
    # except:と記述するだけでも良い
#    例外が起こった時の処理
#else:
#    例外が起こらなかった時の処理

# ◆ 例外を発生させる
# 意図的に例外を発生させて、任意のタイミングで例外処理を実行する事も可能。
# 意図的に例外を発生させるにはraise()を使います。
try:
    print('例外を発生させる')
    raise Exception('例外', 'エラー')
    print('tryブロック,raise実行後')
except Exception as e:
    a1, a2 = e.args#argsはタプル
    print('a1 = ', a1, 'a2 = ', a2)
# result
# 例外を発生させる
# a1 =  例外 a2 =  エラー

print('例２\n')
# ◆ 例２
try:
    f = open('foo.txt', 'r')
    for r in f:
        print( r.strip() )
    f.close()
except FileNotFoundError:
    print('ファイルが見つかりません')
except Exception as e:
    print(e.args)
