
places = ["東京","神奈川","千葉","埼玉"]

if False:
  for place in places:
    if place == "神奈川":
      break
    print(place + "に行きました")
else:
  for place in places:
    if place == "神奈川":
      continue
    print(place + "に行きました")
  else:
    print("繰り返し終了")

for i in range(5):
  print(i)
# >> 0 1 2 3 4 5

for i in range(5, 10):
  print(i)
# >> 5 6 7 8 9

for i in range(0, 10, 3):
  print(i)
# >> 0 3 6 9