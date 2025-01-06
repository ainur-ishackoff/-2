import os
from api import PetFriends
from settings import valid_email, valid_password

pf = PetFriends()

def test_add_new_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    pet_photo = os.path.join(os.path.dirname(__file__), 'images', 'cat.jpg')

    status, result = pf.add_new_pet(auth_key, "Барсик", "кот", "3", pet_photo)
    assert status == 200
    assert result['name'] == "Барсик"

def test_delete_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Барсик", "кот", "3", "images/cat.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status = pf.delete_pet(auth_key, pet_id)
    assert status == 200

def test_update_pet_info():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.update_pet_info(auth_key, pet_id, "Мурзик", "кот", "4")
        assert status == 200
        assert result['name'] == "Мурзик"
    else:
        raise Exception("There is no my pets")