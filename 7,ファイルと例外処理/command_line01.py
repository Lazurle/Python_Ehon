# ◆ コマンドライン引数

# プログラム側でコマンドライン引数を受け取るのは簡単。
# 標準のsysモジュールのargvがコマンドライン引数のリストになっている。
# input -> python command_line01.py abc 123
# out -> ['.\\command_line01.py', '123', 'abc']

import sys
print(sys.argv)

# ◆ コマンドライン引数
import sys
f = ""
sum = 0
for s in sys.argv:
    try:
        n = int(s) # int()メソッド、無理やりint型に変える。できない場合はValueError
        f = f + s + '+'
        sum = sum + n
    except ValueError:
        try:
            n = float(s) # float()メソッド無理やりfloat型に変える。
            f = f + s + '+'
            sum = sum + n
        except:
            pass
print(f.strip('+'), '=', sum)

# python .\command_line01.py 123 489438 721321
# ['.\\command_line01.py', '123', '489438', '721321']
# 123+489438+721321 = 1210882
