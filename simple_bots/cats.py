import requests
import time


API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_DOG = 'https://random.dog/woof.json'
BOT_TOKEN = '7284383193:AAHf6TnCgB0gW4wGIDYn79Vi7Iv2ukwOor4'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('
TEXT = 'Я котик;)'

offset = -2
counter = 0
cat_response: requests.Response
cat_link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            answer = result['message']['text']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                if answer == 'Собаку':
                    dog_response = requests.get(API_DOG)
                    dog_link = dog_response.json()['url']
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={dog_link}')
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Смотри=)')
                else:
                    cat_link = cat_response.json()[0]['url']
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1