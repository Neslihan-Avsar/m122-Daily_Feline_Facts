import requests
import json

URL = 'https://catfact.ninja/fact'
JSON = requests.get(URL, timeout=2.0)
FACT = JSON.json().get('fact') #prints only the fact

if FACT is not None:
    print('Cat Fact: ', FACT)
else:
    print('Failed to fetch cat fact.')

TOKEN = 'https://discord.com/api/webhooks/1221841988383539300/IxoAgD1alags5MQ4udTClPdm8MjmvbVbIoyNMtVViitziDVz4n0xL8rPIpLGaVMnuKJl'
POST = '{"content": "Daily Feline Facts!", "embeds": [{"description": '+FACT+', "color": 6580991}], "attachments": []}'
HEADER = {'Content-Type': 'application/json'}

print(POST) #prints the entire json body for the webhook
