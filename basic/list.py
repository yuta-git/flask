lst = []         #宣言
lst = [1, 2, 3]  #初期化

lst.append(4)

lst.insert(0, 5)

# lst = lst + [6, 7, 8]

lst.extend([6, 7, 8])

print(lst)

lst = [1, 2, 3]  #初期化

del lst[1] # 2番目の要素を削除 

lst = [1, 2, 3]  #初期化

lst.pop(1) # 2 を削除 

lst.pop() # 末尾 を削除 

lst.clear() # 全削除

lst = [3, 2, 1]  #初期化

lst.sort()
# >> [1, 2, 3]

lst = [3, 2, 1]  #初期化

newLst = sorted(lst)
# >> [1, 2, 3]

print(lst)
print(newLst)

lst = [1, 2, 3]  #初期化

lst.reverse()

import copy

lstA = [4, 2, 3, 1]  #初期化

lstB = copy.copy(lstA)
lstB.sort()

print(lstA)
print(lstB)

list_str = ['a', 'b', 'c']
print(list_str)

foods = []
foods.append({'name':'ラーメン', 'price':700})
foods.append({'name':'カレー', 'price':500})
foods.append({'name':'かつ丼', 'price':800})

print(foods)
for food in foods:
  for k, v in food.items():
    print(k, v)