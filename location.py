import requests

r = requests.get('https://geojs.io')

rjson = requests.get('https://get.geojs.io/v1/ip.json')

IP = rjson.json()['ip']

getloc = requests.get('https://get.geojs.io/v1/geo/' + IP + '.json' )


print(getloc.json()['city'])