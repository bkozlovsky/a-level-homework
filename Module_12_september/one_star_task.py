import first_test

d = {
    'spam': first_test.spam,
    'my_sum': first_test.my_sum,
    'shortener': first_test.shortener,
    'compare_ends': first_test.compare_ends

}

user_input = input("Choose the function you'd like to initiate: \n\n" + "\n".join(d.keys()) + "\n\n")

def launcher(func):
    if func == 'spam':
        user_arg = input("\nPlease input number: \n\n")
        print(d.get(func)(user_arg))
    if func == 'my_sum':
        args = []
        while True:
            user_arg = input("\nEnter your number:\n" + "Send 'sum' when finished.\n\n")
            if user_arg == "sum":
                break
            else:
                args.append(int(user_arg))
        print("\n\nThe sum is {}".format(d.get(func)(args)))
    if func == 'shortener':
        user_arg = input("\nPlease send me a string: \n\n")
        print("\n\nThe shortened string is:\n\n{}".format(d.get(func)(user_arg)))
    if func == 'compare_ends':
        words = []
        while True:
            user_arg = input("\nEnter your word:\n" + "Send 'compare' when finished.\n\n")
            if user_arg == "compare":
                break
            else:
                words.append(str(user_arg))
        print("\n\nThe number of strings is {}".format(d.get(func)(words)))

while True:
    if user_input not in d.keys():
        user_input = input("Wrong name of the function, please try again: \n\n" + "\n".join(d.keys()) + "\n\n")
    else:
        launcher(user_input)
        break