import pytest
import requests

BASE_URL_COUNTRIES = "https://restcountries.com/v3.1"

def test_country_details():
    # Testa detalhes sobre um país específico
    country_name = "Brazil"
    response = requests.get(f"{BASE_URL_COUNTRIES}/name/{country_name}")
    assert response.status_code == 200, "Erro ao acessar API de Países"
    data = response.json()
    assert len(data) > 0 and data[0]["name"]["common"] == country_name, "Nome do país não corresponde"
    print(f"País: {data[0]['name']['common']}, Capital: {data[0]['capital'][0]}, Região: {data[0]['region']}")

def test_all_countries():
    # Testa listagem de todos os países
    response = requests.get(f"{BASE_URL_COUNTRIES}/all")
    assert response.status_code == 200, "Erro ao acessar API de Países"
    data = response.json()
    assert isinstance(data, list) and len(data) > 0, "Lista de países não encontrada ou vazia"
    print(f"Número total de países disponíveis: {len(data)}")
