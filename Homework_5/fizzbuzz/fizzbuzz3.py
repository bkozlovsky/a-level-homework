import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

with open(filename1, 'r') as f:
    strings_list = [string.strip() for string in f]

def fizz_buzz(string):
    string = string.split()
    fizz = int(string[0])
    buzz = int(string[1])
    number = int(string[2])

    updated_string = []

    for i in range(1, number+1):
        if i%fizz == 0 and i%buzz == 0:
            i = "FB"
        elif  i%fizz == 0:
            i = "F"
        elif i%buzz == 0:
            i = "B"
        else:
            i
        updated_string.append(str(i))
    return " ".join(updated_string)

with open(filename2,"a") as f2:
    f2.write("Start of the document")
    for index, item in enumerate(list(map(fizz_buzz,strings_list)),1):
        f2.write("\n\nBeginning of string #{}:\n\n".format(index))
        f2.write(item)

print("The result has been written to {}".format(filename2))

f.close()
f2.close()