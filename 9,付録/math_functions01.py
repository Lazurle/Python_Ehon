# ◆ 数学に関する関数
# 平方根などの数学レベルの計算にはMathモジュールを使用する。

# fabs() … 絶対値 a = math.fabs(x) , a = |x|
# 切り上げ、切り捨て、平方根、指数、log（自然対数、対数）
# べき乗、サイン、コサイン、タンジェント
# sin(), cos, tan()の三角関数では角度をラジアンで指定する。
# ラジアンは次の式で求められる値。
# ラジアン = ( 角度[°] * π ) / ( 180 )
# ◆ 単位を変換
# radians() ... 度 -> ラジアン,b = math.radians(a)
# degrees() ... ラジアン -> 度, a = math.degrees(b)
# ◆ 定数
# pi ... 円周率(3.141592653589793), a = math.py
# e ... 自然対数の底(2.718281828459045), a = math.e

# ◆ 乱数を作る
# random関数、標準ライブラリのrandomモジュールをインポートする
import random
import math

print( random.random() )
# random() で作られる乱数は、0.0以上1.0未満の実数です。そのため、たとえば
# ０～９の整数を生成したい場合は１０倍にして小数点以下を切り捨てる必要がある
a = math.floor( random.random() * 10 )
print( a )
# math.floor() ... 小数点以下を切り捨てる。

# 例
import math

deg = 30
rad = math.radians(deg)

sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

print( "角度{}".format(deg) )
print( "sin{:.5f}".format(sin) )
print( "cos{:.5f}".format(cos) )
print( "tan{:.5f}".format(tan) )
