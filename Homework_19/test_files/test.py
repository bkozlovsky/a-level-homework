import os
full_path = os.getcwd()

dirs = os.listdir(full_path)

for file in dirs:
    print(file)
