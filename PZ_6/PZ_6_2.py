
N = int(input("Введите количество элементов списка "))
from random import randint
lst = [randint(-100,100) for i in range(N)]
print(lst)
a = max(lst)
print("Номер локального максимума: ", lst.index(a)+1)


