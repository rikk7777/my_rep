import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Посмотреть расположение МКС на карте
api_url = "http://api.open-notify.org/iss-now.json"
response = requests.get(api_url)
coordinates = response.json().get("iss_position")
formatted_coordinates = f"{coordinates['longitude']}%2C{coordinates['latitude']}"
map_url = f"https://yandex.com/maps/?ll={formatted_coordinates}&z=10"
with webdriver.Chrome() as driver:
    driver.get(map_url)
    time.sleep(30)

