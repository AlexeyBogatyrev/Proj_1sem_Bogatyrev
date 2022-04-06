#Если в матрице имеются положительные элементы, то вывести TRUE, иначе FALSE.
import random

i,j = 3,3
mat = [[random.randrange(-10,15) for x in range(i)]  for y in range (j)]
print(mat)
a = 0
for n in mat:
    for b in n:
        if b > 0:
            a += 1
if a > 1:
    print('TRUE')
else:
 print('FALSE')