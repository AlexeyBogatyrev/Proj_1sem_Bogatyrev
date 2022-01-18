#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Элементы, умноженные на первый максимальный элемент:


l = ['-12 8 9 -89 15 -16 8']
f1 = open('file_1.txt', 'w', encoding='utf-8')
f1.writelines(l)
f1.close()

f2 = open('file_2.txt', 'w', encoding='utf-8')
f2.write('Исходные данные: ')
f2.write('\n')
f2.writelines(l)
f2.close()

f1 = open('file_1.txt', encoding='utf-8')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

f1 = open('file_1.txt', encoding='utf-8')
min1, t = 0, 0
for i in range(len(k)):
    min1 = min1 if min1 < k[i] else k[i]
    if k[i] < 0:
        t += 1

f1 = open('file_1.txt', encoding='utf-8')
max1, t = 0, 0
for i in range(len(k)):
    max1 = max1 if max1 > k[i] else k[i]
    if k[i] < 0:
        t += 1


l1 = []
k = f1.read()
k = k.split()
for i in k:
    i = int(i)
    l1.append(i * max1)

f2 = open('file_2.txt', 'a', encoding='utf-8')
f2.write('\n')
print('Количество элементов: ', len(k), file=f2)
f2.write('\n')
print('Минимальный элемент: ', min1, file=f2)
f2.write('\n')
print('Элементы, умноженные на первый максимальный элемент: ', l1, file=f2)
f2.close()
