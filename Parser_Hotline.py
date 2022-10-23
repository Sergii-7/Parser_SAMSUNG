import requests
from bs4 import BeautifulSoup
import csv
import time

ts = time.strftime("%d.%m.%Y")
CSV_3 = '{}_Hotline.csv'.format(ts)
HOST_3 = 'https://hotline.ua'
URL_1 = 'https://hotline.ua/ua/mobile/mobilnye-telefony-i-smartfony/133-294356/?gclid=EAIaIQobChMIo-_oxpny-gIVNQuiAx2eZAYYEAAYASAAEgLi_vD_BwE'
URL_2, URL_3, URL_4, URL_5, URL_6, URL_7, URL_8 = \
    f'{URL_1}&p=2', f'{URL_1}&p=3', f'{URL_1}&p=4', f'{URL_1}&p=5', f'{URL_1}&p=6', f'{URL_1}&p=7', f'{URL_1}&p=8'
URL_9 = f'{URL_1}&p=9'
HEADERS_1 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'}

def get_html_3(url, params=''):
    r = requests.get(url, headers=HEADERS_1, params=params)
    return r

def get_content_3(html):
    soup_1 = BeautifulSoup(html, 'html.parser')
    items_1 = soup_1.find_all('div', class_='list-item list-item--row')
    phones_1 = []
    for item in items_1:
        phones_1.append(
            {
                'title': item.find('a', class_='list-item__title text-md').get_text(strip=True),
                'model': item.find('a', class_='list-item__title text-md').get_text(strip=True)[-12:-1],
                'price': int(item.find('span', class_='price__value').get_text(strip=True)[:-4]
                         + item.find('span', class_='price__value').get_text(strip=True)[-3:]),
                'link_phone': HOST_3 + item.find('a', class_='list-item__title text-md').get('href')
            })
    return phones_1

def save_doc_3(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Назва', 'Модель', 'Ціна(грн)', 'Посилання на товар'])
        for item in items:
            writer.writerow([item['title'], item['model'], item['price'], item['link_phone']])

#html = get_html_3(URL_1)
phones_H = []
#phones_H.extend(get_content_3(html.text))

htmls = [get_html_3(URL_1), get_html_3(URL_2), get_html_3(URL_3), get_html_3(URL_4),
         get_html_3(URL_5), get_html_3(URL_6), get_html_3(URL_7), get_html_3(URL_8)]

for html in htmls:
    phones_H.extend(get_content_3(html.text))
save_doc_3(phones_H, CSV_3)
