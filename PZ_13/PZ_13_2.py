# Составить генератор (yield), который выводит из строки только буквы.
from string import ascii_letters

def letters(lst):
    yield from [n for n in lst if n in ascii_letters]

A = "i go at school 3 times a week"

list1 = ""
for i in letters(A):
    list1 += i
print(list1)


