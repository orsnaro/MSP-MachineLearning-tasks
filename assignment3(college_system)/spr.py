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



# ----------------------------- PARENT CLASSES -------------------------------------
class Person:
    ids = []

class Building: ...

class Speciality: ...


class Log:
    """history of all interactions with college system : 
       1)startup 2)quit 3) login 4) new_ac"""

    session_counter = 0 #make logCntrFile later to save total log instances
    tmp_logs : list = []
    crnt_user_id  : str = None
    @classmethod
    def incCntr(cls) :
        cls.session_counter += 1 #maybe changed to total_logs_cntr

    @classmethod
    def dump_log(cls, log_state: enm) -> enm:
        # cls.state_holder = None
        log_file = open (r"log.txt", 'a')
        for i in range ( len(cls.tmp_logs)) :
            for log in cls.tmp_logs[i] :
                log_file.writelines(log + ' ')
            log_file.writelines('\n')
        log_file.close()

    @classmethod
    #TODO : later add acc_id = crnt_session_user_id to new_entry()
    def new_log (cls , state : enm , entry_type = -1) -> enm :
        Log.incCntr()
        cls.pc_name = getpass.getuser()
        cls.time_Stamp = datetime.datetime.now()
        instance = [str(cls.time_stamp) , str(state) ,\
                    str(entry_type) , str(cls.pc_name) , cls.crnt_user_id ]

        cls.tmp_logs.append(instance)
class Credentials:
    """Handled account sensitive data"""
    tmp_creds = dict() #list of tuples #each element is tuple of (id(generated randonmly 8 chars exactly),passwordHASHED ( chars eactly))
    @classmethod
    def dump_cred(cls, cred_state: enm) -> enm:
        cred_file = open (r"cred.txt" , 'a')
        for id , hashed  in cls.tmp_creds.items() :
                cred_file.writelines( id + ' ' + hashed + '\n')
        cred_file.close()

    @classmethod
    def set_crnt_user(cls) :
        Log.crnt_user_id = cls._user_id

    @classmethod
    def new_cred (cls , _pass : str) : #assume passwords gets here are validated before
        _pass = hash(_pass) # make sure hash seed is set to 0 !
        cls._user_id = str(random.randint(10000000,99999999))
        cls.tmp_creds[cls._user_id] = _pass
        cls.set_crnt_user()

    @classmethod
    def comp_cred(cls , _user: str , _hashed_pass : str) -> enm :  ...
    #search in crnt creds then on txt or read whole txt and append to creds
    






# ------------------------------- GLOBAL  METHODS --------------------------------

# def disable_rand_hash() -> None:
#     """WARNING THIS FUNCTION MAY CHANGE BUILT-IN 'hash()' *permenentally!!!*"""
#     hashseed = os.getenv('PYTHONHASHSEED')
#     if not hashseed:
#         os.environ['PYTHONHASHSEED'] = '0'
#         os.execv(sys.executable, [sys.executable] + sys.argv)


def connect(con_typ: int) -> enm:
    crnt_user = Log.crnt_user_id #id of the user (objet name of Person class  childs instances)
    con_state : enm = None
    if con_typ == enm.CON_LOG:
        tmp_user = input ("UserID :\n>> ").strip()
        tmp_pass = hash(getpass.getpass("Password : \n>> ").strip())
        Credentials.comp_cred(tmp_user , tmp_pass)

     # search first if Person.ids -> list of objects has the account in crnt session so dont make new one
        #if not int
    elif con_typ == enm.CON_NEW:...
     # search first if Person.ids -> list of objects has the account in crnt session so dont make new one


def main_menu() -> enm:
    Log.new_entry(enm.MAIN_MEN_OK)
    print("Main Menu : \n")
    op = input(" 1) Log in\n\n 2) Create Account\n\n 3) Quit\n\n>> ")

    if int(op) == 3:
        Log.new_entry(enm.MAIN_MEN_QUIT)
        Log.dump_log(enm.MAIN_MEN_OK)
        Credentials.dump_cred(enm.MAIN_MEN_OK)
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
