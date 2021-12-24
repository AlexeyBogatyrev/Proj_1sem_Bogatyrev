
a = float(input('Введите число  '))
n = int(input('Введите целое число '))
result = [a ** i for i in range(1, n+1)]
print(sum(result)+1)



