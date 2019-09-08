import sys

filename1 = sys.argv[1]
filename2 = sys.argv[2]

f = open(filename1, 'r')

first_string = list(f)[0].split()

fizz = int(first_string[0])
buzz = int(first_string[1])
number = int(first_string[2])

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
   string_list.append(str(i))

f2 = open(filename2,"w+")

f2.write(" ".join(string_list))

print("The result has been written to {}".format(filename2))

f.close()
f2.close()