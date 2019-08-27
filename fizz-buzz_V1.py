fizz = int(input("Введите число Fizz: "))
buzz = int(input("Введите число Buzz: "))
number = int(input("Введите последнее число: "))

#Initializing list to collect numbers and letters in a single string
string_list = []

for i in range(1, number+1):
    if i%fizz == 0 and i%buzz == 0:
        i = "FB"
    elif  i%fizz == 0:
        i = "F"
    elif i%buzz == 0:
        i = "B"
    else:
        i
    string_list.append(i)

print(*string_list)