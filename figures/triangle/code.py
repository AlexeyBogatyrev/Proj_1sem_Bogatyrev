import math


def triangle_perimeter(a=7, b=2, c=8):
    res = int(a) + int(b) + int(c)
    print('Периметр треугольника:', res)


def triangle_area(a=7, b=2, c=8):
    p = (a + b + c) * 0.5
    res = p * (p - a) * (p - b) * (p - c)
    print('Площадь треугольника:', math.sqrt(res))

