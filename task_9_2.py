# Задание №2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

# Вариант с выводом формулы.
class Road:
    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width

    def mass_of_asphalt(self, asphalt_thickness):
        return f'{self._length} м * {self._width} м * 25 кг * {asphalt_thickness} см = ' \
               f'{int(self._length * self._width * 25 * asphalt_thickness / 1000)} т.'


road = Road(5000, 20)
print(road.mass_of_asphalt(5))


# Вариант с выводом ответа.
class Road2:
    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width

    def mass_of_asphalt(self, asphalt_thickness):
        return f'{int(self._length * self._width * 25 * asphalt_thickness / 1000)} т.'


road_2 = Road2(5000, 20)
print(road_2.mass_of_asphalt(5))
