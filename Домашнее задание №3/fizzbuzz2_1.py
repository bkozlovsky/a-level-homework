import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

f = open(filename1, 'r')

f2 = open(filename2,"a")

f2.write("Start of the document")

for num, string in enumerate(list(f), 1):
    string = string.split()
    fizz = int(string[0])
    buzz = int(string[1])
    number = int(string[2])
    
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
        string_list.append(str(i))

    f2 = open(filename2,"a")

    f2.write("\n\nBeginning of string #{}:\n\n".format(num))
    
    f2.write(" ".join(string_list))

    print("The result has been written to {}".format(filename2))

    f.close()
    f2.close()