first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
operation = str(input("Введите одну из 4-х доступных операций, которая должна быть произведена над числами (+, -, /, *): "))

while True:
    if operation == "+":
        print("Результат сложения чисел {} и {} равен: {}".format(first_number, second_number, first_number + second_number))
        break
    elif operation == "-":
        print("Результат вычитания чисел {} и {} равен: {}".format(first_number, second_number, first_number - second_number))
        break
    elif operation == "/":
        print("Результат деления чисел {} и {} равен: {}".format(first_number, second_number, first_number / second_number))
        break
    elif operation == "*":
        print("Результат умножения чисел {} и {} равен: {}".format(first_number, second_number, first_number * second_number))
        break
    else:
        operation = str(input("Данная операция не поддерживается! Попробуйте снова: "))