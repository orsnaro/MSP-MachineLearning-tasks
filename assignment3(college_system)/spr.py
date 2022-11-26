import time
import datetime
import math
import os
import random
import sys
import api_gmail
import getpass
import smtplib , ssl
import numpy as np

from  enm import enm
# from enum import Enum
RUN : bool = True



# PARENT CLASSES
class Person: ...

class Building: ...

class Speciality: ...


    # TODO : log class will contain log_cntr_incrementer() ,tuple : date , pc name , state , type : startup , quit ,login , new   and save to college_log.txt - >
    # TODO : (optional) ALL LINES IN .TXT MUS BE SAME LENGTH
class Log:
    """history of all interactions with college system : 1)startup 2)quit 3) login 4) new_ac"""
    session_counter = 0
    tmp_log : list = []
    @classmethod
    def incCntr(cls) :
        cls.session_counter += 1 #maybe changed to total_logs_cntr

    @classmethod
    def dump_log(cls, log_state: enm) -> enm:
        # cls.state_holder = None
        log_file = open (r"log.txt", 'a')
        log_file.writelines(cls.tmp_log)
        log_file.close()

    @classmethod
    #TODO : later add acc_id = crnt_session_user_id to new_entry()
    def new_entry (cls , state : enm , entry_type = -1 , pc_name = getpass.getuser() ) -> enm :
        Log.incCntr()
        instance = [str(datetime.datetime.now()) , str(state) ,str(entry_type) , str(pc_name)]
        cls.tmp_log.append(str(instance)+'\n')





# GLOBAL  METHODS

# TODO : use hash function and dictionary and save to college_carden.text


class Cardentials:
    """Handled account sensitive data"""
    @classmethod
    def dump_carden(cls, carden_state: enm) -> enm:
        # state_holder = None
        pass


def disable_rand_hash() -> None:
    """WARNING THIS FUNCTION MAY CHANGE BUILT-IN 'hash()' *permenentally!!!*"""
    hashseed = os.getenv('PYTHONHASHSEED')
    if not hashseed:
        os.environ['PYTHONHASHSEED'] = '0'
        os.execv(sys.executable, [sys.executable] + sys.argv)


def connect(con_typ: int) -> enm:
    crnt_user : Person = Person.get_crnt_id_instance() #id of the user (objet name of Person class  childs instances)
    con_state : enm = None
    if con_typ == enm.CON_LOG:
     # search first if Person.ids -> list of objects has the account in crnt session so dont make new one
        pass
    elif con_typ == enm.CON_NEW:
     # search first if Person.ids -> list of objects has the account in crnt session so dont make new one
        pass


def main_menu() -> enm:
    Log.new_entry(enm.MAIN_MEN_OK)
    print("Main Menu : \n")
    op = input(" 1) Log in\n\n 2) Create Account\n\n 3) Quit\n\n>> ")

    if int(op) == 3:
        Log.new_entry(enm.MAIN_MEN_QUIT)
        Log.dump_log(enm.MAIN_MEN_OK)
        Cardentials.dump_carden(enm.MAIN_MEN_OK)
        return enm.MAIN_MEN_QUIT
    elif int(op) == 2:
        connect(enm.CON_NEW)
    elif int(op) == 1:
        connect(enm.CON_LOG)
    else:
        Log.new_entry(enm.MAIN_MEN_ER)
        Log.dump_log(enm.MAIN_MEN_ER)
        print("                              ***** ERROR : Invalid input *****\n")
        time.sleep(2)
        for i in range(2 , -1 , -1):
            os.system(r"clear")
            print(f"                         \nRestarting System in {i}...")
            time.sleep(0.5)
        os.system(r"clear")
        main_menu()
