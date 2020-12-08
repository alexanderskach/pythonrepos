'''
Task 1
Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
'''
'''
line = ''
with open('my_file.txt', 'w') as f:
    while True:
        line = input('Input text:')
        if not line:
            break
        f.write(line + '\n')
'''

'''
Task 2
Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.


with open('my_file.txt') as f:
    str_lines = f.readlines()
    print('Total lines: ',len(str_lines))
    for i, line in enumerate(str_lines):
        print("Line ",i, "is, ", line, 'length: ', len(line))
'''

'''
Task 3
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и 
величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., 
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.


with open('data.txt') as f:
    str_lines = f.readlines()
    empls = list()
    sal=0.0
    for i, line in enumerate(str_lines):
        sal += float(line.split()[1])
        if float(line.split()[1]) < 20000:
            empls.append(line.split()[0])
    print('Salery < 20000:')
    for emp in (empls):
        print(emp)
    print('Everage sal: ', sal / i)

    '''

'''
Task 4
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и 
считывающую построчно данные. При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.


dictionary = {'one': 'odin', 'two': 'dva', 'three': 'tri', 'four': 'chetyri'}
transl_lines = list()
with open('data_2.txt') as f:
    str_lines = f.readlines()
    for i, line in enumerate(str_lines):
        print(line.split('-')[0])
        transl_lines.append((dictionary[(line.split('-')[0].lower()).strip()]))
        print(transl_lines)
with open('trans_data_2.txt', 'w') as f2:
    for i, line in enumerate(transl_lines):
        f2.write(line +'-' + str(i+1) + '\n')
 '''

'''
Task 5
Создать (программно) текстовый файл, записать в него программно набор чисел, 
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


from functools import reduce


def list_number(a, b):
    return a + b;


with open('data_3.txt', 'w') as f:
    num = input('Input num:')
    f.write(num)
    num = (map(int, num.split()))
    numbers = list(num)
    print(numbers)

print(reduce(list_number, numbers))

'''

'''
Task 6
6. Необходимо создать (не программно) текстовый файл, где каждая строка 
описывает учебный предмет и наличие лекционных, практических и лабораторных 
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета 
не обязательно были все типы занятий. Сформировать словарь, содержащий название 
предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

subj_dict = dict()
with open('data.txt') as f:
    str_lines = f.readlines()
    for i, line in enumerate(str_lines):
        subj_hours = int(line.split(':')[1].split('-')[0]) + int(line.split(':')[1].split('-')[1]) + int(line.split(':')[1].split('-')[2])
        subj_dict[line.split(':')[0]] = subj_hours
    print(subj_dict)
'''
'''
Task 7
7. Создать (не программно) текстовый файл, в котором каждая строка должна 
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а 
также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а 
также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.

'''
import json

firms_dict = {}
avg_rent = []
with open('firm_data.txt') as f:
    lines = f.readlines()

for line in lines:
    name, form, revenue, costs = line.split()
    rent = int(revenue) - int(costs)
    firms_dict[name] = rent
    if rent > 0:
        avg_rent.append(rent)

avg_rent = sum(avg_rent) / len(avg_rent)
info = [firms_dict, {'avg_rent': avg_rent}]

with open('firms_data.json', 'w') as f_json:
    json.dump(info, f_json)

with open('firms_data.json') as f_json:
    print(json.load(f_json))
