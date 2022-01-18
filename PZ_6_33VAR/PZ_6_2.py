import random
n = int(input("Введите размер списка A: "))

a = []
b = []
t = 0
s = 0
while t < n:
    a.append(random.randint(0, 100))
    t += 1
print(a)
for i in range(len(a)):
    s = 0
    for p in range(i, len(a)):
        s += a[p]
    s /= len(a)-i
    b.append(round(s))
print(b)
