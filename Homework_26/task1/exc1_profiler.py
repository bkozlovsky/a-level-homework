""" Задача, написать класс, который будет работать с контекстным менеджером, чтобы можно профилировать участок кода. """

import cProfile
import sys
import time

sysFile = sys.argv[1]

class Profiler:
    def read_code(self, filename):
        with open(filename, 'r') as file:
            for line in file.readlines():
                if len(line) == 0:
                    pass
                else:
                    cProfile.run(line)
                    time.sleep(5)

myProfiler = Profiler()

myProfiler.read_code(sysFile)
