# ◆ 日付
# 日付を扱うには、datetimeモジュールを使う

# ◆ datetimeモジュール
## ◆ 日付を扱う
print( "日付を扱う" )
# 日付を扱うには、年/月/日を操作できるdateクラスを使います
# dateクラスの、today()メソッドで今日の日付を取得できる。
import datetime #

myDay = datetime.date.today() # 今日の日付を取得
print( myDay )
myDay = datetime.date(2018, 1, 11) # 日付を生成
print( myDay, "\n" )
# result
# 2019-05-17
# 2018-01-11
## ◆ 時刻を扱う
print( "時刻を扱う" )
myTime = datetime.time(16, 45, 50, 6712)
print( myTime, "\n" )
# (時, 分, 秒, マイクロ秒)
# 16:45:50.006712

# ◆ 日付と時刻を扱う。
print( "日付と時刻を扱う" )
# datetimeモジュールのdatetimeクラスを使えば、日付と時刻の両方を操作することが可能。
myDate = datetime.datetime.today()
print( myDate )
myDate = datetime.datetime(2018, 1, 11, 16, 45, 50, 6712)
print( myDate, "\n")

# 2019-05-17 18:52:15.871844
# 2018-01-11 16:45:50.006712
