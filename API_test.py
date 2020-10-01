import requests
import json
r = requests.get('http://api.open-notify.org/iss-now.json')
print(r.json()['iss_position'])

