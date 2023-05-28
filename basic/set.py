"""
set は、重複しない要素を格納するミュータブルなオブジェクト

setに同一の要素は重複できない。
setにミュータブルな要素は格納できない。
setに要素の順序はない。
"""

set = {1, 1, 2, 2.0, 3, 3.00, 4, 4.000} 
# >> {1, 2, 3, 4}

set1 = {1, (1,2,3), '二', (4, '五', 6.0)}
# >> {'二', 1, (4, '五', 6.0), (1, 2, 3)}

list = [0, 1, 1.0, -1,  2, -2,  3, 3.00, -3, 3.0, 4, -4, -4, 5, -5]

set2 = frozenset(list) # イミュータブルな set の作成

colors = {"blue"}

colors.add("red") # 追加
colors.add("orange") # 追加
# >> {'orange', 'blue', 'red'}

colors.remove("blue") # 削除
# >> {'red', 'orange'}

colors.discard("blue") # 存在しない要素を指定してもエラーにならない

# print(colors)

fruits = {"orange", "banana", "apple", "pine", "grape"}
popped = fruits.pop() # ランダムに要素を取り脱して削除
print(fruits) # 1つの要素が削除されたあとの set 
print(popped) # ランダムに取り出された削除された要素

fruits.clear() # 全削除
