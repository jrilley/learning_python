number = 23
'''Принимаем ответ от пользователя

1 -- Принимаем ответ от пользователя (строка)
2 -- Преобразуем полученую строку в число при помощи int()
3 -- Сохраняем в переменную guess

'''
guess = int(input('Введите целое число: '))

if guess == number:
    print('Поздровляю, вы угадали,\n(хотя и не выиграли никакого приза)')
elif guess < number:
    print('Нет! Загаданное число немного больше')
else:
    print('Нет! Загаданное число немного меньше')

print('Завершено')