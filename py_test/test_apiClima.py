import pytest
import requests

BASE_URL_WEATHER = "https://api.open-meteo.com/v1/forecast"

def test_weather_current():
    # Testa dados climáticos atuais para uma localização específica
    response = requests.get(BASE_URL_WEATHER, params={
        "latitude": 51.5074,  # Latitude de Londres
        "longitude": -0.1278, # Longitude de Londres
        "current_weather": True
    })
    assert response.status_code == 200, "Erro ao acessar API de Clima"
    data = response.json()
    assert "current_weather" in data, "Dados climáticos atuais não encontrados"
    print(f"Clima atual em Londres: {data['current_weather']}")

def test_weather_daily_forecast():
    # Testa previsão climática diária para Londres
    response = requests.get(BASE_URL_WEATHER, params={
        "latitude": 51.5074,
        "longitude": -0.1278,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "Europe/London"
    })
    assert response.status_code == 200, "Erro ao acessar API de Clima"
    data = response.json()
    assert "daily" in data, "Dados de previsão diária não encontrados"
    print(f"Previsão diária em Londres: {data['daily']}")