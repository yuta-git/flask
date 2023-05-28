# japanize_matplotlib:matplotlib を日本語表示対応させる
import json, requests, japanize_matplotlib
import matplotlib.pyplot as plt

url = 'https://api.aoikujira.com/like/api.php?m=get&item_id=8'
r = requests.get(url)

data = json.loads(r.text)

labels, values = [], []

for it in data['answers']:
  labels.append(it['label'])
  values.append(it['point'])
  
plt.barh(labels, values)
plt.title('好きなOSは?')
plt.show()