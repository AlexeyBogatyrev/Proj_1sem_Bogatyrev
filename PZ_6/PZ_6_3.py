#Дан список размера N. Переставить в обратном порядке элементы список,
#расположенные между его минимальным и максимальным элементами, включая
#минимальный и максимальный элементы.


N = int(input("Введите количество элементов списка "))
from random import randint
lst = [randint(-100,100) for i in range(N)]
print(lst)
a = max(lst)
b = min(lst)
a = lst.pop(lst.index(a))
b = lst.pop(lst.index(b))
lst.reverse()
lst.insert (0,a)
lst.append(b)
print (lst)