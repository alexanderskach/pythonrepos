'''
Task 1
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

'''

class Matrix:
    def __init__(self, data_for_matr):
        self.data = data_for_matr

    def __str__(self):
        #for i, x in enumerate(self.data):
            #print(' '.join([str(x) for x in (self.data[i])]))
            #print('\n'.join(' '.join([str(x) for x in (line)])) for line in (self.data))
        return '\n'.join(' '.join([str(x) for x in (line)]) for line in (self.data))

    def __add__(self, other):
        sum_matrix = ''
        #sum_matrix = list()
        line = list(zip(self.data, other.data))
        for n, y in enumerate(line):
            print(list(zip(self.data, other.data))[n])
            a = list(zip(self.data, other.data))[n][0]
            b = list(zip(self.data, other.data))[n][1]
            print('sum: ',[x + y for x, y in zip(a, b)] )
            temp = [x + y for x, y in zip(a, b)]
            sum_matrix += ' '.join([str(i) for i in temp])+'\n'
            #sum_matrix.append(temp)
        return sum_matrix

matrix_1 = [[1,2], [3,5]]
matrix_2 = [[7,5], [1,2]]

m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)

print(m_1)
print(m_1 + m_2)

#print(Matrix(a))



'''
Task 2
Реализовать проект расчета суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм. 
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
 Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

'''
from abc import ABC, abstractmethod

class Clothes(ABC):
    
    def __init__(self, size):
        self.size = size
        
    @abstractmethod
    def calcMaterial(self):
        pass
    

class Coat(Clothes):
    
    @property
    def calcMaterial(self):
        return self.size/6.5 + 0.5

class Suit(Clothes):
    
    @property
    def calcMaterial(self):
        return self.size * 2 + 0.3

#Try to use Composition
class Production:
    
    def __init__(self):
        
        self.coats = []
        self.suits = []
    
    def add_coat(self, size):
        self.coats.append(Coat(size))
        
    def add_suit(self, size):
        self.suits.append(Suit(size))
        
    @property
    def sum_material(self):
        sum_mat = 0.0
        for c in self.coats:
            sum_mat += c.calcMaterial
        for s in self.suits:
            sum_mat += s.calcMaterial
        
        return sum_mat
        
    
    
    
    
c = Coat(10)
s = Suit(10)

print(c.calcMaterial)
print(s.calcMaterial)
    
prod = Production()

prod.add_coat(10)
prod.add_suit(10)
prod.add_suit(20)

print('Common material: ', prod.sum_material)



'''
Task 3

Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
 В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), 
 вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
 Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, 
 умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления 
 должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества 
ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется 
как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
 целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и 
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между 
\n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний 
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. 
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. 
Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''

from itertools import count

class Cito:

    def __init__(self, num_of_cell):
        self.num_of_cell = num_of_cell

    def __add__(self, other):
        return self.num_of_cell + other.num_of_cell

    def __sub__(self, other):
        if self.num_of_cell - other.num_of_cell > 0:
            return self.num_of_cell - other.num_of_cell
        else:
            print('Error! Operation is not valid')

    def __mul__(self, other):
        return self.num_of_cell * other.num_of_cell

    def __truediv__(self, other):
        return round(self.num_of_cell / other.num_of_cell)

    def make_order(self, num_of_cell_in_row):

        if self.num_of_cell % num_of_cell_in_row == 0:
            return '\\n'.join(['*' * num_of_cell_in_row for i in range(self.num_of_cell//num_of_cell_in_row)])
        else:
            return '\\n'.join(['*' * num_of_cell_in_row for i in range(self.num_of_cell//num_of_cell_in_row)]) + '\\n' + '*' * (self.num_of_cell % num_of_cell_in_row)

c_1 = Cito(12)
c_2 = Cito(5)

print(c_1.make_order(5))

print(c_1 + c_2)
print(c_2 - c_1)
print(c_1 - c_2)
print(c_1 / c_2)
