import requests
import pytest

def test_status_code():
    base_url = 'https://pokemonbattle.me:9104/'
    token = 'd9d34c0111480cbb584e858ca8106cbc'  
    response_trainers_info = requests.get(f'{base_url}trainers')

    assert response_trainers_info.status_code == 200
    
def test_my_trainer():
    base_url = 'https://pokemonbattle.me:9104/'
    token = 'd9d34c0111480cbb584e858ca8106cbc'  
    response_my_trainer = requests.get(f'{base_url}trainers', params={'trainer_id' : 3438})
    
    assert response_my_trainer.json()['trainer_name'] == "Треник"