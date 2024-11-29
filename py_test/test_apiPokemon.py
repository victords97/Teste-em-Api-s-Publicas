import pytest
import requests

BASE_URL = "https://pokeapi.co/api/v2"

def test_pokemon_data():
    # Testa dados de um Pokémon específico
    pokemon_name = "pikachu"
    response = requests.get(f"{BASE_URL}/pokemon/{pokemon_name}")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert "name" in data and data["name"] == pokemon_name, "Nome do Pokémon não corresponde"
    print(f"Dados do Pokémon: {data['name']}, ID: {data['id']}")

def test_pokemon_abilities():
    # Testa habilidades de um Pokémon
    pokemon_name = "bulbasaur"
    response = requests.get(f"{BASE_URL}/pokemon/{pokemon_name}")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert "abilities" in data, "Habilidades não encontradas"
    abilities = [ability['ability']['name'] for ability in data['abilities']]
    print(f"Habilidades do Pokémon {pokemon_name}: {abilities}")

def test_pokemon_type():
    # Testa tipos de um Pokémon
    pokemon_name = "charmander"
    response = requests.get(f"{BASE_URL}/pokemon/{pokemon_name}")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert "types" in data, "Tipos não encontrados"
    types = [ptype['type']['name'] for ptype in data['types']]
    print(f"Tipos do Pokémon {pokemon_name}: {types}")

def test_pokemon_list():
    # Testa listagem de Pokémons
    limit = 5
    response = requests.get(f"{BASE_URL}/pokemon", params={"limit": limit})
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert "results" in data, "Lista de Pokémons não encontrada"
    assert len(data["results"]) == limit, f"Esperado {limit} Pokémons, mas retornou {len(data['results'])}"
    print(f"Lista de Pokémons: {[pokemon['name'] for pokemon in data['results']]}")

def test_pokemon_species():
    # Testa informações sobre uma espécie de Pokémon
    species_name = "pikachu"
    response = requests.get(f"{BASE_URL}/pokemon-species/{species_name}")
    assert response.status_code == 200, "Erro ao acessar API"
    data = response.json()
    assert "name" in data and data["name"] == species_name, "Nome da espécie não corresponde"
    print(f"Espécie do Pokémon: {data['name']}, Habitat: {data.get('habitat', {}).get('name', 'Desconhecido')}")
