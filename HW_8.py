
# 1
def privitannya (name = "Stas"):
    print(f"Hello, {name}")
privitannya("Ivan")

#2

def foo_y_x2():
    for x in range(-10,11):
        print(x*x/4)

foo_y_x2()

def foo_y_x_minus3():
    for x in range(-10,11):
        print(x/2-4)

foo_y_x_minus3()

#3

num1 = 0
num2 = 0

def input_num():
    global num1
    global num2
    num1 = int(input("Веедіть число 1: "))
    num2 = int(input("Веедіть число 2: "))

def sum(num1,num2):
    print()
    print(f"результат додавання: {num1 + num2}")
    print()

def minus(num1,num2):
    print()
    print(f"результат віднімання: {num1 - num2}")
    print()

def multiplication(num1,num2):
    print()
    print(f"результат множення: {num1 * num2}")
    print()

def division(num1,num2):
    print()
    print(f"результат ділення: {num1 / num2}")
    print()

def stupin(num1,num2):
    print()
    print(f"результат зведення в ступінь: {num1**num2}")
    print()


def sqrt_(num1,num2):
    print()
    print(f"результат знаходження кореню: {num1**(1/num2)}")
    print()


while True:
    inp = int(input("Введіть 1 для додавання, 2 для віднімання,\n3 для множення, 4 для ділення, 5 для зведення в ступінь,"
                " 6 для зведення до квадратного чи кубічного кореня,\n0  для виходу з програми: "))

    if inp == 1:
        input_num()
        sum(num1,num2)

    elif inp == 2:
        input_num()
        minus(num1,num2)

    elif inp == 3:
        input_num()
        multiplication(num1,num2)

    elif inp == 4:
        input_num()
        if num2 != 0:
            division(num1,num2)

    elif inp == 5:
        input_num()
        stupin(num1,num2)

    elif inp == 6:
        input_num()
        sqrt_(num1,num2)


    elif inp == 0:
        break


#4

def avg(num1, num2, num3):

    avg = (num1 + num2 + num3)/3
    print(avg)

while(True):

    ch = int(input("Введіть 1 для вводцу чисел, введіть 0 для виходу:   "))
    if ch ==1:
        num1 = int(input("Введіть число 1:   "))
        num2 = int(input("Введіть число 2:   "))
        num3 = int(input("Введіть число 3:   "))
        avg(num1, num2, num3)
    elif ch == 0:
        break

#5

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

#5
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
