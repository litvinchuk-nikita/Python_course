# Задание №3. Реализовать базовый класс Worker (работник):
# ● определить атрибуты: name, surname, position (должность), income (доход);
# ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
# элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
# ● создать класс Position (должность) на базе класса Worker;
# ● в классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учётом премии (get_total_income);
# ● проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': None, 'bonus': None}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self, wage, bonus):
        self._income['wage'] = wage
        self._income['bonus'] = bonus
        return self._income['wage'] + self._income['bonus']


h1 = Position('Alex', 'Aleksandrov', 'developer')
print(h1.name, h1.surname, h1.position)
print(h1.get_full_name())
print(h1.get_total_income(30000, 15000))
