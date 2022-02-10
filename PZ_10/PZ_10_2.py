#Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
#количество символов, принадлежащих к группе букв. Сформировать новый файл, в
#который поместить текст в стихотворной форме предварительно заменив символы верхнего
#регистра на нижний.

buk = 0

for i in open('text18-4.txt', encoding='UTF-8'):
    print(i, end='')
    for m in i:
        if m.islower() and m.capitalize():
            buk += 1
print("\nКоличество букв :", buk)


f2 = open('text18-4(2).txt', 'w', encoding='UTF-8')
f1 = open('text18-4.txt','r', encoding='UTF-8')
low = f1.read().lower()
for line in low:
    print(line, end = '', file=f2)
f1.close()