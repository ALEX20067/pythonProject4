def count_even_and_odd_digits():
    number = input("Введите число: ")
    even_count = 0
    odd_count = 0
    for digit in number:
        if digit.isdigit():
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    print(f"Четных цифр: {even_count}, Нечетных цифр: {odd_count}")
count_even_and_odd_digits()