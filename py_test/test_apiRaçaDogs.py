import pytest
import requests


BASE_URL_DOGS = "https://dog.ceo/api"

def test_random_dog_image():
    # Testa a obtenção de uma imagem aleatória de cachorro
    response = requests.get(f"{BASE_URL_DOGS}/breeds/image/random")
    assert response.status_code == 200, "Erro ao acessar API de Cachorros"
    data = response.json()
    assert data["status"] == "success", "Não foi possível obter a imagem"
    print(f"Imagem de cachorro aleatória: {data['message']}")

def test_all_breeds():
    # Testa a listagem de todas as raças de cachorros
    response = requests.get(f"{BASE_URL_DOGS}/breeds/list/all")
    assert response.status_code == 200, "Erro ao acessar API de Cachorros"
    data = response.json()
    assert data["status"] == "success", "Não foi possível obter a lista de raças"
    print(f"Lista de raças de cachorros: {', '.join(data['message'].keys())}")

def test_random_image_by_breed():
    # Testa a obtenção de uma imagem aleatória de uma raça específica
    breed = "labrador"
    response = requests.get(f"{BASE_URL_DOGS}/breed/{breed}/images/random")
    assert response.status_code == 200, f"Erro ao acessar API de Cachorros para a raça {breed}"
    data = response.json()
    assert data["status"] == "success", f"Não foi possível obter uma imagem da raça {breed}"
    print(f"Imagem aleatória de um {breed}: {data['message']}")
