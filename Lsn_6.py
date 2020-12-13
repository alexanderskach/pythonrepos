'''
Task 1
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и
метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
from time import sleep
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self.__color = (('Red', 7), ('Yellow', 2),('Green', 4))
    def running(self):
        for color, sec in cycle(self.__color):
            print('color: ', color, 'Delay', sec, 'seconds')
            sleep(sec)

tl = TrafficLight()
tl.running()

'''
Task 2
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, 
необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
'''

class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        m = self._length * self._width * 25 * 5
        print('Mass asfalt is :', m, 'kg')

ma = Road(30, 10000)
ma.mass()


'''
Task 3
Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и 
дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных 
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:

    def __init__(self, name, surname, position, prem):
        self.name = name
        self.surname = surname
        self.position = position
        #self.prem = prem = {'wage': wage, 'bonus': bonus}
        self._wage = prem['wage']
        self._bonus = prem['bonus']
# for value in prem:
# param='_'+[value]
# setattr(self, self.param=prem['wage'])


class Position(Worker):

    def get_full_name(self):
        print (self.name, self.surname)

    def get_total_income(self):
        total = self._wage + self._bonus
        print('Total: ' + str(total))

p = Position('Alex', 'Skach', 'eng', {'wage': 100, 'bonus': 50})
p.get_full_name()
p.get_total_income()



'''
Task 4
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: 
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), 
которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''

class Car:

    def __init__(self, speed, color, name, is_police):

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(' {} Start driving'.format(self.name))


    def stop(self):
        print("{} is Stopping".format(self.name))

    def turn(self, direction):
        print('{} is Driving at {}'.format(self.name, direction))

    def show_speed(self):
        print('{} speed is {}'.format(self.name, self.speed))


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed is too high!')

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed is too high!')


class PoliceCar(Car):

    pass

tc = TownCar(90, 'red', 'mazda', False)
tc.show_speed()
tc.go()
tc.stop()
tc.turn('left')


'''
Task 5
 Реализовать класс Stationery (канцелярская принадлежность). 
 Определить в нем атрибут title (название) и метод draw (отрисовка). 
 Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), 
 Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. 
 Для каждого из классов методы должен выводить уникальное сообщение. 
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    def draw(self):
        print('pen is drawing')


class Pencil(Stationery):
    def draw(self):
        print('pencil is drawing')


class Handle(Stationery):
    def draw(self):
        print('handle is drawing')


pen = Pen('pen')
pen.draw()
pencil = Pencil('pen')
pencil.draw()
handle = Handle('pen')
handle.draw()