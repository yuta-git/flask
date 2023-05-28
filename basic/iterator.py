list = ["a", "b", "c"]

# items = iter(list)
# print(dir(items))

# for item in items:
#   print(next(item))

list.append("d")
list.insert(0, "z")
list.extend("e")
list.extend(["f", "g", "h"])
list_len = len(list)
first = list[0]
list.insert(list_len, "z")

list.pop(0)
list.pop()
list.clear()
list.append("a")
list.extend(["b", "c"])


list.reverse()
list = sorted(list)

import copy

list2 = copy.copy(list)
list2.reverse()
list2.insert(0, "d")
len = len(list2)
list2.pop(len - 1)
list2.append("a")
list2.pop()
list2.extend(["a", "b", "c"])
list2.append("z")

list3 = [[[1, 2, 3],[4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]

if False:
    # イテレータオブジェクト化
    items = iter(list)
elif False:
    items = iter(list2)
elif True:
    items = list3
else:
    pass

if False:
  for item in items:
    print(item)
else:
  pass
