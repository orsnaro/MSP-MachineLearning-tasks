import time
import datetime
import math
import os
import random
import sys
import getpass
import smtplib , ssl
import numpy as np

     #-------------------------------USER DEFINED MODULES----------------------------------#
# import sub 
import api_gmail
from  enm import enm
RUN : bool = True



       # ----------------------------- PARENT & UNINHIRITED CLASSES -----------------------#
class Person:
    ids_student = [] #2 lists of dicts each dict  (objects names is id number) (only strings of ids for now)
    ids_prof = [] 

    def __init__(self ,  id : str , name : str , age : int  , is_prof : bool , speciality : str) -> None:
        self.id = id #could make em in one line i know
        self.name = name
        self.age = age 
        self.is_prof = is_prof
        self.speciality = speciality
        
    def get_id( _id : str) : ...
    def get_name( _fname : str )  : ...
        


class Building: ... #TODO #number  #capacity #schedule(no names only time that it's occubied through week dict())

class Speciality: ...#TODO


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
                cred_file.writelines( str(id) + ' ' + str(hashed) + '\n')
        cred_file.close()

    @classmethod
    def __set_crnt_user(cls) :
        Log.crnt_user_id = cls._user_id
    @classmethod
    def set_crnt_user(cls , _final_id) :
        Log.crnt_user_id = _final_id

    @classmethod
    def new_cred (cls , _pass : str , _is_prof : str , _speciality : str) -> 'list': #assume passwords gets here are validated before
        #TODO :if new menue to choose  prof or stu  and mech or elec 
        #TODO : (append 2 digits to user id  ==> prof = 1  or stu = 0 then elec= 1 or mech= 0) userid total length 10 chars
        _pass = hash(_pass) # make sure hash seed is set to 0 !

        cls._user_id = str(random.randint(10000000,99999999))
        cls._user_id = cls._user_id + _is_prof + _speciality
        cls.tmp_creds[cls._user_id] = _pass
        cls.__set_crnt_user()
        return [enm.CRED_OK, cls._user_id ]
        

    @classmethod
    def comp_cred(cls , _user: str , _hashed_pass : str) -> 'tuple': 
        read_file = open(r"cred.txt" , 'r') #check on users first 
        found = False
        tmp_id = None
        tmp_pass =None

        for line in read_file : #note : each id = 10 char , each line = 30 char , EOF = ''
            tmp_id , tmp_pass = line.split()
            # print (tmp_id , tmp_pass) #for test
            if tmp_id.strip() == _user : 
                found = True
                if tmp_pass.strip() == _hashed_pass:
                    cls._user_id = _user 
                    cls.set_crnt_user()
                    return enm.CRED_ID_FOUND , enm.CRED_OK 
                else :
                    return enm.CRED_ID_FOUND , enm.CRED_FAIL 

        read_file.close() 
        if  not found :
            return enm.CRED_ID_NEW , enm.CON_NEW , _user

class Elmenues :
    @staticmethod
    def main_menu() -> enm:
        main_men_state = None
        Log.new_log(enm.MAIN_MEN_OK , "Startup")
        print("Main Menu : \n")
        op = input(" 1) Log in\n\n 2) Create Account\n\n 3) Quit and save \n\n>> ")

        if not op.isnumeric() :
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

        elif int(op) == 3:
            Log.new_log(enm.MAIN_MEN_QUIT , "Quit") #type : Startup , quit ,login , new , show_log , show_cred ,  show_persons_data
            return enm.MAIN_MEN_QUIT

        elif int(op) == 2:
            Log.new_log(enm.MAIN_MEN_QUIT , "New")
            main_men_state = connect(enm.CON_NEW)

        elif int(op) == 1:
            Log.new_log(enm.MAIN_MEN_QUIT , "Login")
            Credentials.dump_cred(enm.MAIN_MEN_OK)
            main_men_state = connect(enm.CON_LOG)

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
        #TODO : if student he  only can view his object (add fees and mails and shedule to his object later)
    
    @staticmethod
    def new_ac_menu( hashed_pass : str ) -> 'tuple' : 
        tmp_is_prof = None
        tmp_speciality = None

        print (" NEW Account menu : \nplease complete registration...\n\n")
        tmp_is_prof = input("1) If You're a Professor\n\n0) If You're a Student\n>> ").strip()
        print("\n\nChoose Department : \n\n")
        tmp_speciality = input("1) Electrical Department \n\n0) Mechanics Department\n>> ").strip()

        if (tmp_speciality == '1' or tmp_speciality == '0') and (tmp_is_prof == '1' or tmp_is_prof == '0'):
            final_iD =  Credentials.new_cred(hashed_pass ,tmp_is_prof , tmp_speciality )
            return enm.CRED_DONE ,  final_iD , tmp_speciality , tmp_is_prof

        else : 
            print ("*Invalid Input*\n plsease retry...\n\n")
            #TODO : test if this recursion method works if not make while loop until input has been met
            return Elmenues.new_ac_menu(hashed_pass) #recursion magic 
       
    @staticmethod
    def sys_menu(id_type : enm) : ...
    #TODO : if prof .show log  , show cred , show student odjects (later m add to shedule)
    #TODO : if student show shedule  and show only object with same user_id (optional show fees ) each one start with 780Le fees




           # ------------------------------- GLOBAL  METHODS --------------------------------#

def main() :
    print(" \n \n ---------------------( Welcome to Omar's Engineering College System )----------------------\n\n")
    while  RUN : 
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

def get_extra_data ( _final_id : str ) : # id : str , name : str , age : int  , is_prof : bool , speciality : str
    name  = input (f"Please fill Your Personal Info :\nName:\n>> ")
    age = int(input ("\nAge:\n >> "))#could get it from birthday 

    if _final_id[-2]  is '1' :
        is_prof = True
        rank = input("\nAcademic Rank :\n>> ")
        salary = input("\nSalary :\n>> ")
    else : 
        is_prof = False
        year = input ("\nStudy Year:\n>>  ")
        last_gpa = input("\nLast GPA:\n>> ")
    if _final_id[-1] is '1' :
        _speciality = "Electrical"
    else : 
        _speciality = "Mechanical"
    if is_prof :
      #TODO TODO : find way to make this file see chils in sub.py  
        Person.ids_prof.append([_final_id] = [f"name : {name}" , f"age : {age}" , f"Previlage : {'Professor' if is_prof == True else 'Student' }" , f"Department: {_speciality}" , ] 

    
      

def connect(con_typ: int) -> enm:
    # crnt_user = Log.crnt_user_id  #isha will use it XD
    con_state = None

    if con_typ == enm.CON_LOG:
        tmp_user = input ("UserID :\n>> ").strip()
        tmp_pass = hash(getpass.getpass("Password : \n>> ").strip())
        con_state= list(Credentials.comp_cred(tmp_user , tmp_pass))

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
                return con_state[0]

    elif con_typ == enm.CON_NEW:
        print("*User-ID Will Be Auto Generated*\n")
        #TODO : set password restrictions -> start with atleast 8 chars/numbers
        tmp_pass = hash(getpass.getpass("Password : \n>> ").strip())
        con_state = list(Elmenues.new_ac_menu(tmp_pass))

        if con_state[0] == enm.CRED_DONE : con_state[0] = enm.CON_OK # no very imp.

        else : con_state[0] = enm.CON_BAD_DATA

        if con_state[0] == enm.CON_OK :
            print (f"*New Account = ( {con_state[1]} ) has been made Successfully!*\n\n")
            get_extra_data(con_state[1])#return final_id
            print ("sending login data via gmail service is down ..\n")#TODO remove it if didn't work before presentation
            print("Please save your ID and Password somewhere safe...\n\n")
            print (f"---- (USER ID = {con_state[1]} ) ----\n\n")
            Elmenues.loged_menu(con_typ)
        else :
            return con_state[0] #exit UNEXEPECTEDLY and dont dump_cred() might be fetal error in creadentials



