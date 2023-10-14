# Создаем кортеж целых чисел
def corteg_numbers():
    numbers = list(map(int, input("Введите список чисел через пробел: ").split()))

    # Находим максимальный и минимальный элементы в кортеже
    max_num = max(numbers)
    min_num = min(numbers)

    # Выводим результаты
    print(f"Максимальный элемент: {max_num}")
    print(f"Минимальный элемент: {min_num}")
corteg_numbers()