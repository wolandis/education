# #1
#
# slovo = str(input())
# a = slovo[::-1]
# if slovo == a:
#   print("yes")
# else:
#   print("no")

def quadratic_equation(a, b, c):
    x1 = None
    x2 = None

    def calc_result ():
        nonlocal x1, x2
        print(a)
        d = b**2 - 4*a*c
        if d >= 0:
            x1 = (-b + d**0.5)/(2*a)
            x2 = (-b - d**0.5)/(2*a)

            return x1, x2
        else:
            return None
result = quadratic_equation(2, 3, -5)


if result != None:
    print('Result = ', result)
else:
    print('no roots')

