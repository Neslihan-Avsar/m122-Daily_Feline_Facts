import requests

URL = "https://catfact.ninja/fact"
JSON = requests.get(URL)
print(JSON) #prints <Response 200>
