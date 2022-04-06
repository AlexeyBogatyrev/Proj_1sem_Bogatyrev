#В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
#2 раза.

import random

i,j = 3,3
mat = [[random.randrange(1,15) for x in range(i)]  for y in range (j)]
print('Первоночальная матрица \n',mat)
mat[0][1] = mat[0][1] * 2
mat[2][0] = mat[2][0] * 2
mat[2][1] = mat[2][1] * 2
mat[1][0] = mat[1][0] * 2
mat[0][2] = mat[0][2] * 2
mat[1][2] = mat[1][2] * 2




print('Матрица после вычислиений \n',mat)