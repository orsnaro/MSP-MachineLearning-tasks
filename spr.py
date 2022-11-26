import time
import datetime
import math
import os
import random
import sys

import numpy as np

# from enum import Enum


# PAREMT CLASSES
class enm:
    """since python doesnt has enum data-type 
    all funtion states will use this values 
    to implement good program signaling"""
    OK = 0
    MAIN_MEN_QUIT = 1
    MAIN_MEN_ER = 2
    CON_ER = 3
    CON_BAD_DATA = 4


class Person: ...

class Building: ...

class Speciality: ...


    # TODO : log class will contain log_cntr_incrementer() ,tuple : date , acc hint , operation , type : startup , quit ,login , new   and save to college_log.txt
class Log:
    """history of all interactions with college system"""
    @classmethod
    def dump_log(cls, log_state: enm) -> enm:
        state_holder = None
        pass


# GLOBAL VARS. AND FUNCTIONS
run: bool = True

# TODO : use hash function and dictionary and save to college_carden.text


class Cardentials:
    """Handled account sensitive data"""
    @classmethod
    def dump_carden(cls, carden_state: enm) -> enm:
        state_holder = None
        pass


def disable_rand_hash() -> None:
    """WARNING THIS FUNCTION MAY CHANGE BUILT-IN 'hash()' *permenentally!!!*"""
    hashseed = os.getenv('PYTHONHASHSEED')
    if not hashseed:
        os.environ['PYTHONHASHSEED'] = '0'
        os.execv(sys.executable, [sys.executable] + sys.argv)


def connect(con_typ: int) -> enm:
    state_holder = None
    if con_typ == 1:
        ...

    elif con_typ == 2:
        ...


def main_menu() -> enm:
    print("Main Menu : \n")
    op = input(" 1) Log in\n\n 2) Create Account\n\n 3) Quit\n\n>> ")

    if int(op) == 3:
        Log.dump_log(enm.OK)
        Cardentials.dump_carden(enm.OK)
        return enm.MAIN_MEN_QUIT
    elif int(op) == 2:
        connect(int(op))
    elif int(op) == 1:
        connect(int(op))
    else:
        Log.dump_log(enm.MAIN_MEN_ER)
        print("                              ***** ERROR : Invalid input *****\n")
        time.sleep(2)
        for i in range(2 , -1 , -1):
            os.system(r"clear")
            print(f"                         \nRestarting System in {i}...")
            time.sleep(0.5)
        os.system(r"clear")
        main_menu()
