# Задание №4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки.
# Сформировать из этих имён и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

list_of_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                     'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Вариант решения №1.
for employee in list_of_employees:
    employee = employee.rpartition(' ')
    employee = employee[-1].capitalize()
    print(f'Привет, {employee}!')

# Вариант решения №2.
for employee in list_of_employees:
    employee = employee[employee.rfind(' ') + 1:]
    employee = employee.capitalize()
    print(f'Привет, {employee}!')
