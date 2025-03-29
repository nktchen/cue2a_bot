import random
import time

import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Настройки запроса
url = 'https://cue2a.netlify.app/'
boundary = '----geckoformboundary1a4d35842819e20d350893895dc468d'
with open('message.txt', 'r') as file:
    lines = file.readlines()
print("Количество строк:", len(lines))
while True:
    line = random.choice(lines)
    # Поля формы
    fields = [
        ('1_$ACTION_REF_1', ''),
        (
        '1_$ACTION_1:0', ('', '{"id":"608d353e304434dc729259b1db6a33c731349461bc","bound":"$@1"}', 'application/json')),
        ('1_$ACTION_1:1', '["$undefined"]'),
        ('1_$ACTION_KEY', 'k2107209644'),
        ('1_message', line[3:]),
        ('1_files', ('', '', 'application/octet-stream')),
        ('0', '["$undefined","$K1"]'),
    ]

    # Создаем multipart/form-data
    mp_encoder = MultipartEncoder(
        fields=fields,
        boundary=boundary
    )

    # Заголовки
    headers = {
        'Referer': 'https://cue2a.netlify.app/',
        'Origin': 'https://cue2a.netlify.app',
        'Next-Action': '608d353e304434dc729259b1db6a33c731349461bc',
        'Next-Router-State-Tree': '%5B%22%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2F%22%2C%22refresh%22%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
        'Content-Type': mp_encoder.content_type,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }

    # Отправляем запрос
    response = requests.post(url, data=mp_encoder, headers=headers)
    if response.status_code != 200:
        print(f'Status Code: {response.status_code}')
        print(f'Response: {response.text}')
    else:
        print('ok')
    time.sleep(10)

