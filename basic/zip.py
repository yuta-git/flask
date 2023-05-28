places = ["東京","神奈川","千葉","埼玉"]
kanaPlaces = ["トウキョウ","カナガワ","チバ","サイタマ"]

for place, kanaPlace in zip(places, kanaPlaces):
  print(place + "の読み方は" + kanaPlace + "です")

for i, place in enumerate(places, 1):
  print(i, place)
  
for place in reversed(places):
  print(place)