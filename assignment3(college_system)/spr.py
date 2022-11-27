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
                log_file.writelines(str(log) + ' ')
            log_file.writelines('\n')
        log_file.close()

    @classmethod
    #TODO : later add acc_id = crnt_session_user_id to new_log()
    def new_log (cls , state : enm , entry_type : str) -> enm : 
        #entry_type : Startup , quit ,login , new , show_log , show_cred ,  show_persons_data
        Log.incCntr()
        cls.pc_name = getpass.getuser()
        cls.time_stamp = datetime.datetime.now()
        instance = [str(cls.time_stamp) , str(state) ,\
                    str(entry_type) , str(cls.pc_name) , cls.crnt_user_id ]
        cls.tmp_logs.append(instance)
class Credentials:
    """Handled account sensitive data"""
    tmp_creds = dict() 
    file_creds_dict = dict()
    @classmethod
    def dump_cred(cls, cred_state: enm) -> enm:
        cred_file = open (r"cred.txt" , 'a')
        for id , hashed  in cls.tmp_creds.items() : # write line size here : 30 each line 
                cred_file.writelines( id + ' ' + hashed + '\n')
        cred_file.close()

    @classmethod
    def set_crnt_user(cls) :
        Log.crnt_user_id = cls._user_id

    @classmethod
    def new_cred (cls , _pass : str , is_prof : bool , speciality : str) : #assume passwords gets here are validated before
        #TODO :if new menue to choose  prof or stu  and mech or elec 
        #TODO : (append 2 digits to user id  ==> prof = 1  or stu = 0 then elec= 1 or mech= 0) userid total length 10 chars
        #TODO : appends two digits at end of ID to identfy prof or no and speciality
        _pass = hash(_pass) # make sure hash seed is set to 0 !
        cls._user_id = str(random.randint(10000000,99999999))
        cls.tmp_creds[cls._user_id] = _pass
        cls.set_crnt_user()
        return enm.CRED_OK, cls._user_id 

    @classmethod
    def comp_cred(cls , _user: str , _hashed_pass : str) -> enm : 
        read_file = open(r"cred.txt" , 'r') #check on users first 
        found = False
        tmp_id = None
        tmp_pass =None

        for line in read_file : #note : each id = 10 char , each line = 30 char , EOF = ''
            tmp_id , tmp_pass = line.split()
            if tmp_id.strip() == _user : 
                found = True
                if tmp_pass.strip() == tmp_pass :
                    return enm.CRED_ID_FOUND , enm.CRED_OK
                else :
                    return enm.CRED_ID_FOUND , enm.CRED_FAIL

        read_file.close() 
        if  not found :
            return enm.CRED_ID_NEW , enm.CON_NEW


    






# ------------------------------- GLOBAL  METHODS --------------------------------
#TODO : but all main funcs variation in one calss Elmainues and make them all static 

# def disable_rand_hash() -> None:
#     """WARNING THIS FUNCTION MAY CHANGE BUILT-IN 'hash()' *permenentally!!!*"""
#     hashseed = os.getenv('PYTHONHASHSEED')
#     if not hashseed:
#         os.environ['PYTHONHASHSEED'] = '0'
#         os.execv(sys.executable, [sys.executable] + sys.argv)


def connect(con_typ: int) -> enm:
    crnt_user = Log.crnt_user_id 
    con_state : enm = [] 
    if con_typ == enm.CON_LOG:
        tmp_user = input ("UserID :\n>> ").strip()
        tmp_pass = hash(getpass.getpass("Password : \n>> ").strip())
        con_state= Credentials.comp_cred(tmp_user , tmp_pass)
        if con_state[0] == enm.CRED_ID_FOUND and con_state[1] == enm.CRED_OK : #valid login
            print ("*Signed in Successfully!*\n\n")
            loged_menu(con_typ) 
        else : 
            print("*LOGIN FAIL!*\n")
            if con_state[0] == enm.CRED_ID_NEW :
                print ("THIS ID is *not used* . please retry ...\n\n")
                main_menu()
            elif con_state[1] == enm.CRED_FAIL :
                print ("*WRONG PASSWORD*. please retry...\n\n")
                main_menu()

    elif con_typ == enm.CON_NEW:
        print("*User-ID Will Be Generated Auto*\n")
        #TODO : set password restrictions -> start with atleast 8 chars/numbers
        tmp_pass = hash(getpass.getpass("Password : \n>> ").strip())
        is_prof = False
        speciality = None

        #TODO : ask him about if prof or no then the speciality 

        con_state = Credentials.new_cred(tmp_pass , is_prof , speciality )
        print (f"*New Account = ( {con_state[1]} ) has been made Successfully!*\n\n")
        print ("sending login data via gmail service is down ..\n")
        print("Please save your ID and Password somewhere safe...\n\n")
        print (f"---- (USER ID = {con_state[1]} ) ----\n\n")
        loged_menu(con_typ)



def main_menu() -> enm:
    Log.new_log(enm.MAIN_MEN_OK , "Startup")
    print("Main Menu : \n")
    op = input(" 1) Log in\n\n 2) Create Account\n\n 3) Quit\n\n>> ")

    if int(op) == 3:
        Log.new_log(enm.MAIN_MEN_QUIT , "Quit") #type : Startup , quit ,login , new , show_log , show_cred ,  show_persons_data
        Log.dump_log(enm.MAIN_MEN_OK)
        Credentials.dump_cred(enm.MAIN_MEN_OK)
        return enm.MAIN_MEN_QUIT
    elif int(op) == 2:
        Log.new_log(enm.MAIN_MEN_QUIT , "New")
        connect(enm.CON_NEW)
    elif int(op) == 1:
        Log.new_log(enm.MAIN_MEN_QUIT , "Login")
        connect(enm.CON_LOG)
    else:
        Log.new_log(enm.MAIN_MEN_ER , "Other" ) 
        Log.dump_log(enm.MAIN_MEN_ER)
        print("                              ***** ERROR : Invalid input *****\n")
        time.sleep(2)
        for i in range(2 , -1 , -1):
            os.system(r"clear")
            print(f"                         \nRestarting System in {i}...")
            time.sleep(0.5)
        os.system(r"clear")
        main_menu()

def loged_menu ( log_type :  enm ) : ...

        #TODO : if not new go to sys_menu : show (log and cred and all prof and student objects only if prof ) 
        #TODO : if stud only can view his object (add fees and mails to his object later)

def sys_menu(id_type : enm) : ...