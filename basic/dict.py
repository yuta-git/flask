population = {'東京':900, '横浜':370, '大阪':250, '名古屋':230, '福岡':150}
population2 = dict(東京=900, 横浜=370, 大阪=250, 名古屋=230, 福岡=150)

cities = ['東京', '横浜', '大阪', '名古屋', '福岡']
nums = [900, 370, 250, 230, 150]

population3 = dict(zip(cities, nums))

population3['東京']

population3.get('東京')

'東京' in population3

900 in population3.values()

for k in population3:
  print(k)
  
for v in population3.values():
  print(v)
  
for k, v in population3.items():
  print(k, v)
  
fruits = {'apple': 100, 'pine':200, 'orange':300}
fruits['grape'] = 500 # 追加
animals = {'monkey': 3, 'dog': 6, 'cat': 10}
animals['monkey'] = 100 # 更新
mix = {}
mix.update(fruits)
mix.update(animals)

popped = mix.pop('grape')
del mix['apple'], mix['cat']
mix.clear()

mix2 = {}
mix2.update(fruits)
mix2.update(animals)
mix2_sorted = sorted(mix2.values())

mix3 = mix2.copy()

print(mix3)
