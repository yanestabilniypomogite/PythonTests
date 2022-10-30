from urllib import response
import requests
import pytest
import random

url_petshop = "https://petstore.swagger.io/v2/pet"
names = ['Bob', 'Mike', 'Pup', 'Sam', 'Sharik', 'Basya', 'Doggie', 'Max' , 'Rex']
random_name = random.choice(names)
id = random.randint(0,100)

def test_add_a_new_pet_status_code() :
    data_pet = {
        "id": id,
        "category": {
        "id": 0,
        "name": "string"
         },
        "name": random_name,
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
    url = url_petshop
    assert requests.post(url, json = data_pet).status_code == 200

def test_find_pet_id_status_code():
    url = '/'.join([url_petshop, str(id)])
    assert requests.get(url).status_code == 200

def test_find_pet_id_check_name():
    url = '/'.join([url_petshop, str(id)])
    assert requests.get(url).json()["name"] == random_name