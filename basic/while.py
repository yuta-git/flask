"""
for文とwhile文は同じ繰り返し処理ですが、次の点が異なります。

for文は回数を指定して、指定した回数分の繰り返し処理を行います。
一方でwhile文は、条件を指定して、その条件がTrueの間は繰り返し処理を行い、Falseになれば繰り返し処理を抜けます。
"""

3
4
i = 0
while i < 3:
    print(i)
    i = i + 1
# >> 0 1 2

"""
break 3の倍数になったら処理を中止する
"""
a = 0
while a < 10: 
    a = a + 1
    if a % 3 == 0:
        break
    print(a)
# >> 1 2

"""
continue 3の倍数のときだけスキップ
"""
a = 0
while a < 10: 
    a = a + 1
    if a % 3 == 0:
        continue
    print(a)
# >> 1 2 4 5 7 8 10