""" 2) Написать класс, который будет читать .csv любых размеров, и будет отдавать ответ построчно аля генератор """

import sys
import time

f1 = sys.argv[1]

class MyProfiler:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.time_delta = None

    def _get_current_time(self):
        return time.time()

    def __enter__(self):
        self.start_time = self._get_current_time()
        print(f"START {self.start_time}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = self._get_current_time()
        print(f"END {self.end_time}")
        self.time_delta = self.end_time - self.start_time
        print(f"TIME SPEND {self.time_delta}")

#My Version
class CSVReader():
    def readCSV(self, filename):
        with open(filename, 'r') as file:
            try:
                iterator = iter(file.readlines())
                while True:
                    return next(iterator)
            except StopIteration:
                pass

#Teacher's Version
class ReadBigFile:
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        with open(self.filename) as file:
            yield from file

myCSVReader1 = ReadBigFile(f1)

myCSVReader2 = CSVReader()

def class1():
    for line in myCSVReader1:
        print(line)

def class2():
    myCSVReader2.readCSV(f1)

with MyProfiler():
    class1() #0.02322077751159668 time to process
    class2() #0.0003139972686767578 time to process