import pytest
import requests

def add_new_pet():
    data_pet = {
        "id": 10,
        "category": {
        "id": 0,
        "name": "string"
         },
        "name": "Pup",
         "photoUrls": [
        "string"
        ],
        "tags": [
         {
          "id": 0,
             "name": "string"
         }
        ],
        "status": "available"
        }
    add_pet = requests.post("https://petstore.swagger.io/v2/pet", json = data_pet)
    print(add_pet.text)

def update_pet():
    data_update_pet = {
        "id": 10,
        "category": {
            "id": 0,
            "name": "string"
         },
        "name": "doggie",
        "photoUrls": [
         "string"
         ],
        "tags": [
         {
           "id": 0,
              "name": "string"
        }
         ],
        "status": "available"
        }
    update = requests.put("https://petstore.swagger.io/v2/pet", json = data_update_pet)
    print(update.text)

def find_pet_id():
    data_find = 10
    find_pet = requests.get(f"https://petstore.swagger.io/v2/pet/{data_find}")
    print(find_pet.text)

add_new_pet()
update_pet()
find_pet_id()
