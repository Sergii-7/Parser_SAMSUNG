import requests
from bs4 import BeautifulSoup
import csv
import time

ts = time.strftime("%d.%m.%Y")
CSV_1 = '{}_Foxtrot.csv'.format(ts)
HOST_1 = 'https://www.foxtrot.com.ua'
URL_1 = 'https://www.foxtrot.com.ua/uk/shop/mobilnye_telefony_samsung_smartfon.html?'
URL_2, URL_3, URL_4 = f'{URL_1}page=2', f'{URL_1}page=3', f'{URL_1}page=4'

HEADERS_1 = {
    'Accept': 'image/avif,image/webp,*/*',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

def get_html_1(url, params=''):
    r = requests.get(url, headers=HEADERS_1, params=params)
    return r

def get_content_1(html):
    soup_1 = BeautifulSoup(html, 'html.parser')
    items_1 = soup_1.find_all('div', class_='card__body')
    phones_1 = []
    for item in items_1:
        phones_1.append(
            {
                'title': item.find('a', class_='card__title').get_text(strip=True),
                'model': item.find('a', class_='card__title').get_text(strip=True)[-15:-4],
                'price': int(item.find('div', class_='card-price').get_text(strip=True)[:-6]+
                             item.find('div', class_='card-price').get_text(strip=True)[-5:-2]),
                'link_phone': HOST_1 + item.find('a', class_='card__title').get('href')
            })
    return phones_1

def save_doc_1(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Назва', 'Модель', 'Ціна(грн)', 'Посилання на товар'])
        for item in items:
            writer.writerow([item['title'], item['model'], item['price'], item['link_phone']])

#html = get_html_1(URL_1)
phones_F = []
#phones_F.extend(get_content_1(html.text))

htmls = [get_html_1(URL_1), get_html_1(URL_2), get_html_1(URL_3), get_html_1(URL_4)]
for html in htmls:
    phones_F.extend(get_content_1(html.text))

save_doc_1(phones_F, CSV_1)
