from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления '
'квадратного корня из заданного числа'
print(message)


def calculatesquareroot(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float):
    """Вычисляет квадратный корень из заданного числа."""
    if your_number <= 0:
        return 0
    else:
        root = calculatesquareroot(your_number)
        return print('Мы вычислили квадратный корень из введённого вами числа. '
                     'Это будет: ', root)


print(message)
calc(25.5)
