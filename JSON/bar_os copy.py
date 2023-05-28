
import requests


url = 'https://api.aoikujira.com/like/api.php?m=get&item_id=8'
res = requests.get(url)

body = {
  'id':5
}

res1 = requests.get(url, body)

res.status_code

res.json()[:5]

