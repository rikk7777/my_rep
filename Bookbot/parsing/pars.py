from bs4 import BeautifulSoup
import requests
import random

all_pices = []

response = requests.get('https://www.kinomania.ru/film/208060/frames')
soup=BeautifulSoup(response.text, 'lxml')
pic_urls = ['https:' + item['data-original'] for item in soup.find_all('img', class_='image-cover')]

def get_pic():
    random_pic = random.choice(pic_urls)
    r2 = requests.get(random_pic)
    with open('images/picture.jpg', 'wb') as file:
        file.write(r2.content)
