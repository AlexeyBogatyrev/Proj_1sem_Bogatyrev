#В последовательности на n целых чисел умножить элементы до n-1 на элемент
#n.

N = int(input("Введите количество элементов списка "))
from random import randint
lst = [randint(-100,100) for i in range(N)]
print(lst)
elem = lst[-1]
lst1 = (list(map(lambda x: x*elem, lst)))

lst1[-1]=lst[-1]

print(lst1)
