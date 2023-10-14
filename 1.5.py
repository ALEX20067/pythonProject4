def auto_parts_shop():
    products = {
        "Запчасть 1": ["Описание 1", 100, 50],
        "Запчасть 2": ["Описание 2", 200, 30],
        "Запчасть 3": ["Описание 3", 150, 40],
        "Запчасть 4": ["Описание 4", 300, 20],
        "Запчасть 5": ["Описание 5", 50, 60],
    }

    while True:
        print("\nМеню:")
        print("1. Просмотр описания")
        print("2. Просмотр цены")
        print("3. Просмотр количества")
        print("4. Вся информация")
        print("5. Покупка")
        print("6. До свидания")
        choice = input("Выберите пункт меню (1-6): ")

        if choice == "1":
            product_name = input("Введите название продукции: ")
            description = products.get(product_name, ["Нет такой продукции"])[0]
            print(f"{product_name} - {description}")

        elif choice == "2":
            product_name = input("Введите название продукции: ")
            price = products.get(product_name, ["Нет такой продукции"])[1]
            print(f"{product_name} - Цена: {price}")

        elif choice == "3":
            product_name = input("Введите название продукции: ")
            quantity = products.get(product_name, ["Нет такой продукции"])[2]
            print(f"{product_name} - Количество: {quantity}")

        elif choice == "4":
            for product_name, product_info in products.items():
                description, price, quantity = product_info
                print(f"{product_name}: Описание: {description}, Цена: {price}, Количество: {quantity}")

        elif choice == "5":
            total_price = 0
            while True:
                product_name = input("Введите название продукции (или 'n' для завершения покупки): ")
                if product_name == "n":
                    break
                if product_name in products:
                    quantity_to_buy = int(input("Введите количество: "))
                    if quantity_to_buy <= products[product_name][2]:
                        products[product_name][2] -= quantity_to_buy
                        total_price += quantity_to_buy * products[product_name][1]
                        print(f"Товар {product_name} добавлен в корзину.")
                    else:
                        print("Недостаточно товара на складе.")
                else:
                    print("Такой продукции нет в магазине.")
            print(f"Общая стоимость покупки: {total_price}")

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите пункт меню от 1 до 6.")
auto_parts_shop()