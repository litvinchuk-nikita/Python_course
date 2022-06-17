# Задание №4. Реализуйте базовый класс Car:
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула на{direction}')

    def show_speed(self):
        print(f'Машина едет со скоростью {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Машина едет с привышением разрешенной скорость в 60 км/ч. Ваша скорость {self.speed} км/ч.')
        else:
            print(f'Машина едет со скоростью {self.speed} км/ч.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Машина едет с привышением разрешенной скорость в 40 км/ч. Ваша скорость {self.speed} км/ч.')
        else:
            print(f'Машина едет со скоростью {self.speed} км/ч.')


class PoliceCar(Car):
    pass


town_car = TownCar(65, 'red', 'kia', False)
work_car = WorkCar(41, 'blue', 'ford', False)
print(town_car.speed, town_car.color, town_car.name)
print(work_car.speed, work_car.color, work_car.name)
town_car.show_speed()
work_car.show_speed()
