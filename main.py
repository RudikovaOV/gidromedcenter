# При запуске выдается меню из действий:
# 1 - ввода температуры
# 2 - вывод температуры
# 3 - вывод макс температуры
# 4 - вывод мин температур
# 5 - вывод дней, когда была макс и мин температура
# ...
# Q - выход
# обязательно тоже самое только в файле
from file_funk import filesave
from functions import *
from UI import *
temps = [543, 33, 66, 88, 22, 33]
print(get_max_temp(temps))
user_choise = ""

while user_choise != "Q":
    menu()
    user_choise = input("Введите пункт меню")
    if user_choise == '3':
        print("Max temp = ", get_max_temp(temps))
    if user_choise == '4':
        print("Min temp = ", get_min_temp(temps))
    if user_choise == '5':
        print("day max min temp = ", get_max_min_temp(temps))

    if user_choise == '6':
        filesave("список температур.txt",temps)

