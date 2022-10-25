from urllib import response
import requests
import pytest

def test_Add_a_new_pet_status_code() :
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
    url = "https://petstore.swagger.io/v2/pet"
    response = requests.post(url, json = data_pet)
    assert response.status_code == 200

def test_find_pet_id_status_code():
    data_find = 10
    url = f"https://petstore.swagger.io/v2/pet/{data_find}"
    find_pet = requests.get(url)
    assert find_pet.status_code == 200

def test_find_pet_id_check_name():
    data_find = 10
    url = f"https://petstore.swagger.io/v2/pet/{data_find}"
    find_pet = requests.get(url)
    find_pet = find_pet.json()
    assert find_pet["name"] == "Pup"