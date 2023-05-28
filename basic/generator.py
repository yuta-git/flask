def animal_generator():
  yield 'dog'
  yield 'cat'
  yield 'mouse'
  
animal = animal_generator()
for a in animal:
  print(a)
  
def range_generator(start, stop, step):
  n = start
  while n < stop:
    yield n
    n += step
    
for i in range_generator(0, 10 ,1):
  print(i)
  
if True:
  def fact_generator():
    prev = 1 # 直前の値の初期値
    n = 1 # 現在の値の初期値
    while n <= 10:
      fact = prev * n # nの階乗を演算する
      yield fact # nの階乗を算出する
      prev = fact # 直前に算出した値を記録する
      n += 1
      
  for data in fact_generator():
    print(data)
    
else:
  def fact_generator():
    prev = 1 # 直前の値の初期値
    n = 1 # 現在の値の初期値
    while n <= 10:
      fact = prev * n # nの階乗を演算する
      n += 1
      
  for data in fact_generator():
    print(data)