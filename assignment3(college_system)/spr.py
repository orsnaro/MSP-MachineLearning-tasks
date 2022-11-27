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
RUN : bool = True



       # ----------------------------- PARENT CLASSES -------------------------------------#
class Person:
    ids = []

class Building: ...

class Speciality: ...


class Log:
    """History of all interactions with college system : 
       1)startup 2)quit 3) login 4) new_ac."""

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
    def new_cred (cls , _pass : str , _is_prof : bool , _speciality : str) -> 'list': #assume passwords gets here are validated before
        #TODO :if new menue to choose  prof or stu  and mech or elec 
        #TODO : (append 2 digits to user id  ==> prof = 1  or stu = 0 then elec= 1 or mech= 0) userid total length 10 chars
        _pass = hash(_pass) # make sure hash seed is set to 0 !
        cls._user_id = str(random.randint(10000000,99999999))
        #TODO : appends two digits at end of ID to identfy prof or no and speciality
        cls.tmp_creds[cls._user_id] = _pass
        cls.set_crnt_user()
        return enm.CRED_OK, cls._user_id 

    @classmethod
    def comp_cred(cls , _user: str , _hashed_pass : str) -> 'list': 
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

class Elmenues :
    @staticmethod
    def main_menu() -> enm:
        main_men_state = None
        Log.new_log(enm.MAIN_MEN_OK , "Startup")
        print("Main Menu : \n")
        op = input(" 1) Log in\n\n 2) Create Account\n\n 3) Quit and save \n\n>> ")

        if int(op) == 3:
            Log.new_log(enm.MAIN_MEN_QUIT , "Quit") #type : Startup , quit ,login , new , show_log , show_cred ,  show_persons_data
            return enm.MAIN_MEN_QUIT
        elif int(op) == 2:
            Log.new_log(enm.MAIN_MEN_QUIT , "New")
            main_men_state = connect(enm.CON_NEW)
        elif int(op) == 1:
            Log.new_log(enm.MAIN_MEN_QUIT , "Login")
            Credentials.dump_cred(enm.MAIN_MEN_OK)
            main_men_state = connect(enm.CON_LOG)
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
            Elmenues.main_menu()

        if main_men_state == enm.CON_ER :
            Elmenues.main_menu()
        elif main_men_state == enm.CON_BAD_DATA :
            return enm.MAIN_MEN_ER

        else : #all done correctly
            is_done = False
            is_done = bool(int(input("*Type :*\n  '1' : to Quit and save \n  '0' : to go to Main menu \n>> ")))
            if  is_done  : return enm.MAIN_MEN_QUIT
            else : return enm.MAIN_MEN_RES

    @staticmethod
    def loged_menu ( log_type :  enm ) : ...
        #TODO : if not new go to sys_menu : show (log and cred and all prof and student objects only if prof ) 
        #TODO : if stud only can view his object (add fees and mails to his object later)
    
    @staticmethod
    def new_ac_menu( hashed_pass : str ) -> 'list' : 
        tmp_is_prof = False
        tmp_speciality = None
        final_iD =  Credentials.new_cred(hashed_pass ,tmp_is_prof , tmp_speciality )
        return enm.CRED_DONE ,  final_iD
       
    @staticmethod
    def sys_menu(id_type : enm) : ...





           # ------------------------------- GLOBAL  METHODS --------------------------------#

def main() :
    print(" \n \n ---------------------( Welcome to Omar's Engineering College System )----------------------\n\n")
    while  RUN : #actually its not super loop it's for error
        exit_state = Elmenues.main_menu() 
        if exit_state == enm.MAIN_MEN_QUIT : 
            Log.dump_log(enm.MAIN_MEN_OK)
            Credentials.dump_cred(enm.MAIN_MEN_OK)
            sys.exit(enm.MAIN_MEN_OK) 
        elif exit_state == enm.MAIN_MEN_RES : continue
        else : 
            Log.new_log(enm.UNKNOWN , "Other" ) 
            Log.dump_log(enm.UNKNOWN)
            print("**SYSTEM TERMINATED UNEXPECTEDLY**")
            sys.exit(enm.MAIN_MEN_ER)

# def disable_rand_hash_seed() -> 'str': 
#     """
#     -> WARNING THIS FUNCTION MAY CHANGE BUILT-IN 'hash()' *permenentally!!!* \n
#     -> This function makes built-in hash() works as expected \n
#        i.e. ( for same input only = same hashed output ) at any session \n
#     -> so basically is makes PYTHONHASHSEDD = '0' to make it constant seed not random. \n
#     """
#     hashseed = os.getenv('PYTHONHASHSEED')
#     if not hashseed:
#         os.environ['PYTHONHASHSEED'] = '0'
#         os.execv(sys.executable, [sys.executable] + sys.argv)
#     return  hashseed


def connect(con_typ: int) -> enm:
    crnt_user = Log.crnt_user_id 
    con_state : enm = [] 
    if con_typ == enm.CON_LOG:
        tmp_user = input ("UserID :\n>> ").strip()
        tmp_pass = hash(getpass.getpass("Password : \n>> ").strip())
        con_state= Credentials.comp_cred(tmp_user , tmp_pass)
        if con_state[0] == enm.CRED_ID_FOUND and con_state[1] == enm.CRED_OK : #valid login
            print ("*Signed in Successfully!*\n\n")
            Elmenues.loged_menu(con_typ) 
        else : 
            print("*LOGIN FAIL!*\n")
            if con_state[0] == enm.CRED_ID_NEW :
                print ("THIS ID is *not used* . please retry ...\n\n")
                Elmenues.main_menu()
            elif con_state[1] == enm.CRED_FAIL :
                print ("*WRONG PASSWORD*. please retry...\n\n")
                con_state[0] = enm.CON_ER
                return (con_state[0])

    elif con_typ == enm.CON_NEW:
        print("*User-ID Will Be Auto Generated*\n")
        #TODO : set password restrictions -> start with atleast 8 chars/numbers
        tmp_pass = hash(getpass.getpass("Password : \n>> ").strip())
        con_state = Elmenues.new_ac_menu(tmp_pass)

        if con_state[0] == enm.CRED_DONE : con_state[0] = enm.CON_OK
        else : con_state[0] = enm.CON_BAD_DATA

        if con_state[0] == enm.CON_OK :
            print (f"*New Account = ( {con_state[1]} ) has been made Successfully!*\n\n")
            print ("sending login data via gmail service is down ..\n")
            print("Please save your ID and Password somewhere safe...\n\n")
            print (f"---- (USER ID = {con_state[1]} ) ----\n\n")
            Elmenues.loged_menu(con_typ)
        else :
            return con_state[0] #exit UNEXEPCTEDLY and dont dump_cred might be fetal error in creadentials



