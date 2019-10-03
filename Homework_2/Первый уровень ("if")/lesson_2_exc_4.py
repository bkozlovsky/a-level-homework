#Задача Ввести число, вывести его разряды и их множители.

x = int(input("Введите число: "))

number_length = len(str(x))

num_list = list(str(x))

num_position = []

for i in range(0, number_length):
    num_position.append(i)

res = list(zip(num_list, num_position[::-1]))

for r in res:
    print("%s * 10 ** %s" % r)