from array import array
from logging import error
from tokenize import String
import requests
import json
from os.path import exists

PAGE_URL = "http://google.com"
DATA_PATH = "data.json"

def add_url(url: String):
    try:
        response = requests.get(url)
    except :
        print("invalid URL: " + url)
        return

    if response.status_code == 200:

        file = None
        json_data = None

        if not exists(DATA_PATH):
            json_data = {url: {
                "last_checked": 0,
                "last_updates": [],
                "last_hash": 0
            }}
        else:
            file = open(DATA_PATH, "r")
            json_data = json.load(file)
            if json_data[url]:
                return
            file.close()

            json_data[url] = {
                "last_checked": 0,
                "last_updates": [],
                "last_hash": 0
            }

        file = open(DATA_PATH, "w")
        file.write(json.dumps(json_data))
        file.close

add_url(PAGE_URL)

with open(DATA_PATH, "r+") as file:
    json_data = json.load(file)
    for url, value in json_data.items():
        try: 
            response = requests.get(url)
            if response.status_code == 200:
                print(response.text)
        except:
            print("Error while checking for updates on url " + url)

