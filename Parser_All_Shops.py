import csv
import time
ts = time.strftime("%d.%m.%Y")
CSV = f'{ts}_Best_Price.csv'

import Parser_Comfy, Parser_Foxtrot, Parser_Hotline

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Назва', 'Модель', 'Ціна(грн)', 'Посилання на товар'])
        for item in items:
            writer.writerow([item['title'], item['model'], item['price'], item['link_phone']])

Parser_Comfy
Parser_Foxtrot
Parser_Hotline
l = []
for x in Parser_Comfy.phones_C:
    for y in Parser_Foxtrot.phones_F:
        for h in Parser_Hotline.phones_H:
            if x['model'] == y['model'] and x['price'] < y['price'] and x not in l:
                l.append(x)
            elif x['model'] == y['model'] and x['price'] > y['price'] and y not in l:
                l.append(y)
            elif x['model'] == h['model'] and x['price'] < h['price'] and x not in l:
                l.append(x)
            elif x['model'] == h['model'] and x['price'] > h['price'] and h not in l:
                l.append(h)
            elif h['model'] == y['model'] and h['price'] < y['price'] and h not in l:
                l.append(h)
            elif h['model'] == y['model'] and h['price'] > y['price'] and y not in l:
                l.append(y)

save_doc(l, CSV)
