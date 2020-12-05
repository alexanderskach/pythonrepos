from sys import argv

from functools import reduce
from itertools import count
from itertools import cycle

'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''

script_name, hour_param, cost_param, bonus_param = argv

def my_sum(hour_param, cost_param, bonus_param):
    s = int(hour_param) * int(cost_param) + int(bonus_param)
    return print("Sallary is: ", s)

my_sum(hour_param, cost_param, bonus_param)


'''
Task 2
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
'''
list_num = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_res = [x for i, x in enumerate(list_num) if list_num[i] > list_num[i - 1] and i < len(list_num) - 1 and i != 0]
print(list_res)

'''
Task 3
Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
'''
nums = [i for i in range(20, 240) if (i % 20 == 0 or i % 21 == 0)]
print(nums)

'''
Task4
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
 соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. 
 Для выполнения задания обязательно использовать генератор.
'''

list_num = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_res = [i for i in list_num if list_num.count(i) < 2]
print(list_res)

'''
Task5
 Реализовать формирование списка, используя функцию range() и возможности генератора. 
 В список должны войти четные числа от 100 до 1000 (включая границы). 
 Необходимо получить результат вычисления произведения всех элементов списка.
'''

def list_number(a, b):
    return a * b;


numbers = [i for i in range(100, 1001) if i % 2 == 0]

print(reduce(list_number, numbers))

'''
Task6
Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного,
'''
for i in count(1):
    print
    i,
    if i > 100:
        break

print
"\n"
'''
Task6
итератор, повторяющий элементы некоторого списка, определенного заранее.
'''
count = 0
for item in cycle('XYZ'):
    if count > 7:
        break
    print(item)
    count += 1

'''
Task7
 Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
 При вызове функции должен создаваться объект-генератор. 
 Функция должна вызываться следующим образом: for el in fact(n). 
 Функция отвечает за получение факториала числа, 
 а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
'''


def fact(x):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
        yield factorial


res = [el for el in fact(2)]
print(res)
