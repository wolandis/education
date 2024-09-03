# print("hello!")
# # Завдання 2
#
# # Створіть програму, яка емулює роботу сервісу зі скорочення посилань. Повинна бути реалізована можливість введення
# # початкового посилання та короткої назви і отримання початкового посилання за її назвою.
# abr_dict = {}
# while 1:
#     vibir = int(input("введіть 1 для внесення данних\nвведіть 2 для перегляду\nвведіть 0 для виходу"))
#
#     if vibir == 1:
#         key = input("Введіть повний текст посилання")
#         value = input("Введіть абревіатуру посилання посилання")
#         abr_dict.setdefault(key[, value])

# Створіть програму калькулятор:
#
# Користувач вводить два числа та обирає одну з дій + - * /
#
# Виконайте потрібну дію та виведіть результат на екран
#
# Кожна дія має бути оформлена як функція яка буде приймати два аргументи та повертати потрібне значення

# import turtle
# def draw(size, color = "red", width = 5):
#     turtle.color(color)
#     turtle.width(width)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
#     turtle.forward(size)
#     turtle.left(90)
# draw(100)
# turtle.exitonclick()

# def privitannya (name = "Stas"):
#     print(f"Hello, {name}")
# privitannya("Ivan")

#
# def avg(num1, num2, num3):
#
#     avg = (num1 + num2 + num3)/3
#     print(avg)
#
# while(True):
#
#     ch = int(input("Введіть 1 для вводцу чисел, введіть 0 для виходу:   "))
#     if ch ==1:
#         num1 = int(input("Введіть число 1:   "))
#         num2 = int(input("Введіть число 2:   "))
#         num3 = int(input("Введіть число 3:   "))
#         avg(num1, num2, num3)
#     elif ch == 0:
#         break


    # num1 = int(input("Введіть число 1:   "))
    # num2 = int(input("Введіть число 2:   "))
    # num3 = int(input("Введіть число 3:   "))


def ind(height, weight):
    ind = weight / (height * height)
    if ind < 18.5:
        print("Недостатня вага")

    elif ind < 24.9:
        print("Нормальна вага")

    elif ind < 20.9:
        print("Зайва вага")

    else:
        print("ознаки ожиріння")


while (True):

    ch = input("Введіть start для вводу пареметрів, введіть off для виходу:   ")
    if ch == "start":
        weight = float(input("Введіть вагу в кг:   "))
        height = float(input("Введіть зріст в метрах:   "))

        ind(height, weight)
    elif ch == "off":
        break