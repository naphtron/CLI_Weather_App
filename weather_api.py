import requests
import json

x = requests.get('http://www.7timer.info/bin/astro.php?lon=113.17&lat=23.09&ac=0&lang=en&unit=metric&output=json&tzshift=0')
data = json.loads(x.text)
print(data['dataseries'][0]['wind10m']['direction'])

# Just learning how to consume APIs.
# API: 7timer weather API
# Monday 27th February 2023