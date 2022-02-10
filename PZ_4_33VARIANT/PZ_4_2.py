import random
N = random.randint(1,1000)
print(N)
s = N
k = 0
while s >= 1:
    a = s % 10
    s = int(s/10)
    k = k * 10 + a
print(k)
