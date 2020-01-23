number = 23
running = True

while running:
    guess = int(input('Введите целое число: '))

    if guess == number:
        print('Поздровляю, ты угадал число!')
        running = False
    elif guess < number:
        print('Нет, число немного больше!')
    else:
        print('Нет, число немного меньше!')
else:
    print('Цикл while закончен')

print('Завершено')
