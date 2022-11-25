
import math
import os
import sys
import cv2
import datetime
import random
import numpy as np
from enum import Enum
run: bool = True


# global vars and methods
def main_menu():
    pass


class error_enums(Enum):
    pass

    # super classes


class Person:
    pass


class Building:
    pass


class Speciality:
    pass


class Log:
    pass


class Cardentials:  # TODO : use hash function and dictionary
    @staticmethod
    def disable_rand_hash() -> "WARNING THIS FUNCTION MAY CHANGE BUILT-IN 'hash()' permenentally":
        hashseed = os.getenv('PYTHONHASHSEED')
        if not hashseed:
            os.environ['PYTHONHASHSEED'] = '0'
            os.execv(sys.executable, [sys.executable] + sys.argv)

    