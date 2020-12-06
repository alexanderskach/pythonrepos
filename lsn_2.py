'''
Task 1
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у
пользователя, а указать явно, в программе.
'''
list = ['lala', {'d':444}, 0.0, True, 567]
for i in list:
    type_d = type(i)
    print(f'Тип данных элемента: {i} соответствует {type_d}')
'''
Task 2
Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
'''
string = "123456789"
el_reverse = ''
symbols = list(string)
a = symbols[0::2]
b = symbols[1::2]
print(a)
print(b)
print('length: ',(a if len(a) >= len(b) else b))
c = [x+y for x,y in zip(b,a)] + (a if len(a) >= len(b) else b)[min(len(a), len(b)):]
print(''.join(c))

'''Task 3
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict.
'''
'''
month = int(input('Введите месяц: '))
season = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print('Данному месяцу соответствует: ', season[month-1])

'''
season = {[12,1,2]:'зима'}
month = int(input('Введите месяц: '))
print(month.get(1))
'''
season = {1:'зима', 2:'весна', 3:'лето', 4:'осень'}
month = int(input('Введите месяц: '))
if month in [12,1,2]:
    key = 1
    print(season.get(key))
elif month in [3,4,5]:
    key = 2
    print(season.get(key))
elif month in [6,7,8]:
    key = 3
    print(season.get(key))
elif month in [9,10,11]:
    key = 4
    print(season.get(key))
'''
'''
Task 4
Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''
'''
words = input('Введите слова через пробел: ')
print(words.split(' '))
list_words = words.split(' ')
i = 1
for w in list_words:
    if len(w) > 10:
        w = w[:10]
    print(i,') ', w)
    i+=1
'''
'''
Task 5
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, то новый 
элемент с тем же значением должен разместиться после них.
'''

my_list = [7, 5, 3, 3, 2]
elr = int(input('Введите элемент рейтинга: '))
cnt = my_list.count(elr)
print(cnt)
if cnt >= 1:
    ind = my_list.index(elr)
    print(ind)
    my_list.insert(ind + cnt-1,elr)
else:
    if elr > max(my_list):
        my_list.insert(0, elr)
    elif elr < min(my_list):
        my_list.append(elr)
    else:
        for ind, number in enumerate(my_list):
            if int(elr) < int(number):
                continue
            my_list.insert(ind, elr)
            break
        else:
            my_list.append(elr)

print(my_list)

'''
Task 6
'''

