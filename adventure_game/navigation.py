from PIL import Image

map_image = Image.open('map.jpg')

coordinates = {'зеленая': [1, 11], 'желтая': [2, 12], 'красная': [3, 13], 'коворкинг': [4, 21], 'ресепшн': [5, 22], 'коричневая': [6, 23], 'макдональдс': [7, 31], 'коридор': [8, 32], 'уборная': [9, 33]}

actions = {'Вперед':'W', 'Назад':'S', 'Влево':'A', 'Вправо':'D', 'Телепорт': 'T', 'Лифт': 'L', 'Показать карту': 'M'}

try:
    direction_request = int(input('\nВведи цифру локации, откуда хочешь начать: \n\n' + "\n".join([" \n".join(str(index)) + " - " + loc for index, loc in enumerate(coordinates.keys(), 1)]) + "\n ------------------ \n\n"))
except ValueError:
    direction_request = int(input("\nЭй! Я же попросил цифру :) Давай еще разок. \n ------------------ \n\n"))

direction_request = str([i[1] for i in list(coordinates.values()) if i[0] == direction_request][0])

while True:
    try:
        available_actions = {}
        print("\nТы находишься в локации: {}".format([key for key, value in coordinates.items() if str(value[1]) == direction_request][0].title()) + "\n")
        if int(direction_request[1]) < 3:
            available_actions[list(actions.keys())[3]] = list(actions.values())[3]
        if int(direction_request[1]) > 1:
            available_actions[list(actions.keys())[2]] = list(actions.values())[2]
        if int(direction_request[0]) < 3 and int(direction_request) != 21:
            available_actions[list(actions.keys())[1]] = list(actions.values())[1]
        if int(direction_request[0]) > 1 and int(direction_request) != 31:
            available_actions[list(actions.keys())[0]] = list(actions.values())[0]
        if int(direction_request) == 31 or int(direction_request) == 32:
            available_actions[list(actions.keys())[5]] = list(actions.values())[5]
        available_actions[list(actions.keys())[4]] = list(actions.values())[4]
        available_actions[list(actions.keys())[6]] = list(actions.values())[6]
    
        move_request = input("\nДоступны следующие действия. \n\n" + "\n".join([v + " - " + k for k, v in available_actions.items()]) + "\n ------------------ \n")
        if move_request.lower() == list(actions.values())[0].lower():
            direction_request = str(int(direction_request) - 10)
        elif move_request.lower() == list(actions.values())[1].lower():
            direction_request = str(int(direction_request) + 10)
        elif move_request.lower() == list(actions.values())[2].lower():
            direction_request = str(int(direction_request) - 1)
        elif move_request.lower() == list(actions.values())[3].lower():
            direction_request = str(int(direction_request) + 1)
        elif move_request.lower() == list(actions.values())[4].lower():
            direction_request = int(input('\nТы открыл Телепорт! Введи цифру чтобы перейти в локацию: \n\n' + "\n".join([" \n".join(str(index)) + " - " + loc for index, loc in enumerate(coordinates.keys(), 1)]) + "\n\n"))
            direction_request = str([i[1] for i in list(coordinates.values()) if i[0] == direction_request][0])
        elif move_request.lower() == list(actions.values())[5].lower():
            print("\nТы зашел в лифт")
            break
        elif move_request.lower() == list(actions.values())[6].lower():
            map_image.show()
        else:
            move_request = input("\nНе понимаю что делать. Введи правильную команду.\n\n")
    
    except IndexError:
        print("\nКажется ты ввел неправильную команду, попробуй еще раз")
        break