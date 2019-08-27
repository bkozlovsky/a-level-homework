while True:
    try:
        month = int(input("Введите номер месяца: "))
        if month in [12, 1, 2]:
            print("Зима")
            break
        elif month in [3, 4, 5]:
            print("Весна")
            break
        elif month in [6, 7, 8]:
            print("Лето")
            break
        elif month in [9, 10, 11]:
            print("Осень")
            break
        else:
            print("Данные введены неверно. Нужно число от 1 до 12.")
    except ValueError:
        print("Ошибка, нужно число от 1 до 12, соответствующее месяцу.")