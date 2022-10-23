import requests
from bs4 import BeautifulSoup
import csv
import time

ts = time.strftime("%d.%m.%Y")
CSV_2 = '{}_Comfy.csv'.format(ts)
HOST_2 = 'https://comfy.ua'
URL_1 = 'https://comfy.ua/ua/smartfon/brand__samsung/'
URL_2, URL_3 = f'{URL_1}?p=2', f'{URL_1}?p=3'

HEADERS_2 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

def get_html_2(url, params=''):
    r = requests.get(url, headers=HEADERS_2, params=params)
    return r

def get_content_2(html):
    soup_1 = BeautifulSoup(html, 'html.parser')
    items_1 = soup_1.find_all('div', class_='products-list-item__info')
    phones_1 = []
    for item in items_1:
        phones_1.append(
            {
                'title': item.find('a', class_='products-list-item__name').get_text(strip=True),
                'model': item.find('a', class_='products-list-item__name').get_text(strip=True)[-15:-4],
                'price': int(item.find('div', class_='products-list-item__actions-price-current').get_text(strip=True)[:-5]+
                             item.find('div', class_='products-list-item__actions-price-current').get_text(strip=True)[-4:-1]),
                'link_phone': item.find('a', class_='products-list-item__name').get('href')
            })
    return phones_1

def save_doc_2(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Назва', 'Модель', 'Ціна(грн)', 'Посилання на товар'])
        for item in items:
            writer.writerow([item['title'], item['model'], item['price'], item['link_phone']])

#html = get_html_2(URL_1)
phones_C = []
#phones_C.extend(get_content_2(html.text))

htmls = [get_html_2(URL_1), get_html_2(URL_2), get_html_2(URL_3)]
for html in htmls:
    phones_C.extend(get_content_2(html.text))

save_doc_2(phones_C, CSV_2)