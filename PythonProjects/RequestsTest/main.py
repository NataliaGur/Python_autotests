import requests

base_url = 'https://pokemonbattle.me:9104/'
token = 'd9d34c0111480cbb584e858ca8106cbc'

response = requests.post(f'{base_url}pokemons', headers={'trainer_token': token}, json={
    "name": "Эликсир",
    "photo": "https://dolnikov.ru/pokemons/albums/038.png"
})

print (response.json())

response_change_name = requests.put(f'{base_url}pokemons', headers={'trainer_token': token}, json={
    "pokemon_id": "9231",
    "name": "Авалор",
    "photo": "https://dolnikov.ru/pokemons/albums/038.png"
})

print (response_change_name.json())

response_pokeball = requests.post(f'{base_url}/trainers/add_pokeball', headers={'trainer_token': token}, json={
    "pokemon_id": "9231",
})

print (response_pokeball.json())