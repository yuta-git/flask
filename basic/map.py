l = [-2, -1, 0]

for i in map(lambda x: abs(x), l):
  print(i)
  
  
l_s = ['apple', 'orange', 'strawberry']

print(list(map(len, l_s))) # l_s に入っている各要素の長さを返す
# >> [5, 6, 10]

print(list(map(lambda x: abs(x), range(-2, 1))))

print(list(map(lambda x: x**2, l)))

def square(x):
  return x ** 2

print(list(map(square, l)))

print([abs(x) for x in l]) # リスト内包表記

