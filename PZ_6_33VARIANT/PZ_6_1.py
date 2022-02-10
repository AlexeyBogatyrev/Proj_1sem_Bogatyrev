import random

a = random.randint()
n = int(input(''))
if n % 2 != 0:
    print('Невозможно поменять местами')
else:
    for i in range(n):
        ne = int(input())
        a.append(ne)
    print(a)
    print(a[n // 2:] + a[0: n // 2])