import datetime

str1 = "abc"
print(type(str1))
# >> str

float1 = 3.14
print(type(float1))
# >> float

str2 = '34'
int_str2 = int(str2)
print(type(int_str2))
# >> int

date1 = datetime.datetime(2023, 4, 3, 8, 13, 52)
str_date1 = date1.strftime("%Y/%m/%d %H:%M:%S")
print(type(str_date1))
# >> str

str3 = '2020/01/31 12:36:45'
str4 = datetime.datetime.strptime(str3, '%Y/%m/%d %H:%M:%S')
print(type(str4))
# >> datetime.datetime