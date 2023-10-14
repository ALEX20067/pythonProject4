def count_letter_pairs():
    word = input("Введите слово: ")
    upper_lower_pairs = 0
    upper_count = 0
    lower_count = 0
    for i in range(len(word) - 1):
        if word[i].isupper() and word[i+1].islower():
            upper_lower_pairs += 1
        elif word[i].islower() and word[i+1].isupper():
            upper_lower_pairs += 1
        if word[i].isupper():
            upper_count += 1
        elif word[i].islower():
            lower_count += 1
    total_letters = upper_count + lower_count
    print(f"Пар верхнего и нижнего регистра: {upper_lower_pairs}")
    print(f"Всего букв в слове: {total_letters}")
count_letter_pairs()