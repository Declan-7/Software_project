import requests
STATIONS_URI = "https://api.jcdecaux.com/vls/v1/stations"
r = requests.get(STATIONS_URI, params={"apiKey": "0c33c118bceda4c97332fd6d6e80949f12932213", 
                                       "contract": 'Dublin'})
print(r.content)