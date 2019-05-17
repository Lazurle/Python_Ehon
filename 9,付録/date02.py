import datetime
myDate = datetime.datetime.today()
wlist = ('月', '火', '水', '木', '金', '土', '日')
y = myDate.year
m = myDate.month
d = myDate.day
h = myDate.hour
mn = myDate.minute
s = myDate.second
w = wlist[ myDate.weekday() ] # weekday()メソッド曜日を整数で返します(0~6、月曜日を0とする)

print('現在の日時', myDate)
print('ISO8601形式', myDate.isoformat() )
# isoformat()メソッドISO8601形式の日付や時間を返します。
# YYYY-MM-DDTHH:MM:SS.mmmmmm
print(y, m, d, h, mn, s, w)
