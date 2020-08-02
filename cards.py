#!/usr/bin/python3
import requests

URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

payload = {}

headers = {'Accept': 'application/json'}

response = requests.get(URL, headers=headers, data=payload)

respJSON = response.json()

print(respJSON)
print("Hope you enjoyed the card game!")
