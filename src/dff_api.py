import requests
import json

URL = 'https://catfact.ninja/fact'
JSON = requests.get(URL, timeout=2.0)
FACT = JSON.json().get('fact')

if FACT is not None:
    print('Cat Fact: ', FACT)
else:
    print('Failed to fetch cat fact.')
