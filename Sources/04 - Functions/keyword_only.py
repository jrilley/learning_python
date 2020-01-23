def total(initial=5, *numbers, extra_num):
    count = initial

    for num in numbers:
        count += num

    count += extra_num
    print(count)


total(10, 1, 2, 3, extra_num=25)
total(10, 1, 2, 3)