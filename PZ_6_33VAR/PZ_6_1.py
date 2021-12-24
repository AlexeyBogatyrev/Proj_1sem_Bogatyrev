import random
n = int(input("Введите размер списка A: "))

a = []
b = []
t = 0

while t < n:
    a.append(random.randint(0, 100))
    t += 1
print(a)

for i in range(len(a)):
    if i < len(a) / 2:
        continue
    else:
        b.append(a[i])

for i in range(len(b)):
    b.append(a[i])
if len(a) % 2 != 0:
    b.insert(int(len(b) / 2), a[int((len(a)+1)/2)-1])
print(b)