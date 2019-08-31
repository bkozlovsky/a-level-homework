import sys

filename = sys.argv[1]

f = open(filename, 'r')

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

file2 = open("text2.txt","w+")

file2.write(" ".join(string_list))

f.close()
file2.close()