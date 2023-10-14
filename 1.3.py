def sum_of_negatives_between_zeros():
    numbers = list(map(int, input("Введите список чисел через пробел: ").split()))
    negative_sum = 0
    zero_count = 0
    for num in numbers:
        if num < 0:
            negative_sum += num
        elif num == 0:
            zero_count += 1
            if zero_count == 2:
                break
    if zero_count < 2:
        negative_sum = 0
    print(f"Сумма отрицательных элементов: {negative_sum}")
sum_of_negatives_between_zeros()