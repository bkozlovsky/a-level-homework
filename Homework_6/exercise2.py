sizes = {
    's': {'russia': 40, ('belgium', 'germany', 'netherlands', 'norway', 'finland', 'sweden'): 34, ('france', 'switzerland'): 36, 'italy': 38, 'great britain': 8, 'usa': 6},
    'm': {'russia': [42, 44], ('belgium', 'germany', 'netherlands', 'norway', 'finland', 'sweden'): [36, 38], ('france', 'switzerland'): [38, 40], 'italy': [40, 42], 'great britain': [10, 12], 'usa': [8, 10]},
    'l': {'russia': [46, 48], ('belgium', 'germany', 'netherlands', 'norway', 'finland', 'sweden'): [40, 42], ('france', 'switzerland'): [42, 44], 'italy': [44, 46], 'great britain': [14, 16], 'usa': [12, 14]},
    'xl': {'russia': [50, 52], ('belgium', 'germany', 'netherlands', 'norway', 'finland', 'sweden'): [44, 46], ('france', 'switzerland'): [46, 48], 'italy': [48, 50], 'great britain': [18, 20], 'usa': [16, 18]},
    'xxl': {'russia': 54, ('belgium', 'germany', 'netherlands', 'norway', 'finland', 'sweden'): 48, ('france', 'switzerland'): 50, 'italy': 52, 'great britain': 22, 'usa': 20}
    }

while True:
    try:
        incomingSize = input('Please enter your size: ')

        incomingCountry = input('Where are you from? ')

        def return_size(size, country):
            internation_size = sizes.get(size.lower())
            country_size = internation_size.get(country.lower())
            if type(country_size) == list:
                return str(country_size)[1:-1]
            else:
                for key, value in internation_size.items():
                    if country in key:
                        return value

        if return_size(incomingSize, incomingCountry) == None:
            print('\nWrong data provided, please try again!\n\n')
            continue
        else:
            print(return_size(incomingSize, incomingCountry))
            break
    except AttributeError:
        print('\nWrong data provided, please try again!\n\n')
        continue

