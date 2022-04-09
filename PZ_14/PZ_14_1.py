#В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить
#фразу «Министерства образования Ростовской области», посчитать количество
#произведённых добавлений. Сколько номеров телефонов заканчивается на «03»,
#«50». Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.



import re

with open('hotline.txt', 'r', encoding='utf-8') as file:
    text = file.read()
f1 = open("hotline_2.txt", "w", encoding="UTF-8")
with open("hotline_2.txt", "w", encoding="UTF-8") as file:
    text = re.sub("«Горячая линия»", "«Горячая линия Министерства образования Ростовской области»", text)
    f1.write(text)
    a = text.count("«Горячая линия Министерства образования Ростовской области»")
    print('Количество произведенный дополнений:'  , a)
p = re.compile(r"[05]+[03]")

print('Количество телефонов, заканчивающихся на 03 или 50:  ', len(p.findall(text)))




a = re.compile(r"ЕГЭ.+\d+")
s = a.findall(text)
print('Номера телефонов горячих линий, связанных с ЕГЭ/ГИА: \n', s)