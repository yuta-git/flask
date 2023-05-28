import datetime

dt_now = datetime.datetime.now()
print(dt_now)
# 2018-02-02 18:31:13.271231

print(type(dt_now))
# <class 'datetime.datetime'>

print(dt_now.year)
# 2018

print(dt_now.hour)
# 18

"""
datetimeオブジェクトのコンストラクタ
datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
"""

dt = datetime.datetime(2018, 2, 1, 12, 15, 30, 2000)
print(dt)
# 2018-02-01 12:15:30.002000

print(dt.day)
# 1

print(dt.minute)
# 15

print(dt.microsecond)
# 2000

dt = datetime.datetime(2018, 2, 1)
print(dt)
# 2018-02-01 00:00:00

print(dt.minute)
# 0