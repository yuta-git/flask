s = "Python"
print(s[2:5])
# >> tho 

print(s[:5])
# >> Pytho

print(s[2:])
# >> thon

print(s[:])
# >> Python

s1 = [0, 1, 2, 3, 4, 5]
s2 = s1[:]
print(s2)
print(id(s1), id(s2))

"""
スライス操作が先に評価され、次に加算が評価されます。
'Pyt'という文字列と、'hon'という文字列の結合
"""
s3 = s[:3] + s[3:]
print(s3)

s4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = s4[::2]  # 偶数
odd = s4[1::2]  # 奇数
print(even)
print(odd)

print(s[::-1])
# >> 'nohtyP' (シーケンスをリバースする)

s5 = slice(None, None, -1).indices(len(s))
print(s5)
# >> (5, -1, -1)