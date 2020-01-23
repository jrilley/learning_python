x = 2


def func():
    global x

    print('x равно: ', x)
    x = 5
    print('Заменяем глобалное значение x на', x)


func()
print('Значение x составляет', x)