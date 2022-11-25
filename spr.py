
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
    def toggle_rand_hash_seed(_random: bool) -> None:
        _random = bool(_random)
        
        if _random:
            hashseed = os.getenv('PYTHONHASHSEED')
            if hashseed:
                os.environ['PYTHONHASHSEED'] = str(random.randint(1,400))
                os.execv(sys.executable, [sys.executable] + sys.argv)
        else : 
            hashseed = os.getenv('PYTHONHASHSEED')
            if not hashseed:
                os.environ['PYTHONHASHSEED'] = '0'
                os.execv(sys.executable, [sys.executable] + sys.argv)

    