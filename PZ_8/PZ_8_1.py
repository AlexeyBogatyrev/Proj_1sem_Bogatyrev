#Дан словарь с четным количеством элементов. Найти суммы значений
#элементов первой и второй половин с использованием функции. Результаты вывести
#на экран.
def get_two_sum(data_dict):
    d1 = sum(list(data_dict.values())[:len(numbers_dict)//2])
    d2 = sum(list(data_dict.values())[len(numbers_dict)//2:])
    return d1, d2


numbers_dict = {1: 10,
2: 30,
3: 50,
4: 100,
5: 300,
6: 500}


sum_1, sum_2 = get_two_sum(numbers_dict)
print('Сумма первой половины: ', sum_1)
print('Сумма второй половины: ', sum_2)