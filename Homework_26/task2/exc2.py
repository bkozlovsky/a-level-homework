""" 2) Написать класс, который будет читать .csv любых размеров, и будет отдавать ответ построчно аля генератор """

import sys
import time

f1 = sys.argv[1]

class CSVReader():
    def readCSV(self, filename):
        with open(filename, 'r') as file:
            try:
                iterator = iter(file.readlines())
                while True:
                    print(next(iterator))
                    time.sleep(0.3)
            except StopIteration:
                pass

myCSVReader = CSVReader()

myCSVReader.readCSV(f1)