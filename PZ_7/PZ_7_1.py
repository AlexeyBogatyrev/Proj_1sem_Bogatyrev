#Дано целое число N (1 < N < 26). Вывести N первых прописных (то есть заглавных)
#букв латинского алфавита

from random import randint
a = (randint(1,26))
print(a)
for i in range(a):
    print(chr(ord('А')+i), end=" ")
