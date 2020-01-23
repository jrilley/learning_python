def func_total(initial=5, *numbers, **keywords):
    count = initial

    for number in numbers:
        count += number

    for key in keywords:
        count += keywords[key]

    return count


result = func_total(10, 1, 2, 3, 4, vegetables=50, fruits=100)
print(result)

'''Переменное число параметров

* -- кортеж
** -- словарь

'''