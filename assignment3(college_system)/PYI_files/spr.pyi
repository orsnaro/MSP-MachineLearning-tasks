##########################################################################################
#                                                                                        #
#                                                                                        #
#                                                                                        #
#                          Programmer : Omar Rashad                                      #
#                          Version : v0.4 Beta                                           #
#                          Date :  29 / 11 / 2022                                        #
#                          Code Type : spr.pyi => Mini_proj for MSP-ML Committe        #
#                          Title : Omar's Emgineering College System                     #
#                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]  #
#                                                                                        #
#                                                                                        #
#                                                                                        #
##########################################################################################
       ## this is more clear and abstract view on spr.pyi file methods and classes ##
import time
import datetime
import math
import os
import random
import sys
import getpass
import smtplib , ssl
import numpy as np

     #----------------------------------USER DEFINED MODULES----------------------------------#
import api_gmail
from  enm import enm
RUN : bool = True

       # ------------------------------PARENT & UNINHIRITED CLASSES --------------------------#
class Person:
    ids_student : 'list[dict]' = ...
    ids_prof : 'list[dict]' = ...

    def __init__(self, id : 'str' , name : 'str' , age : 'int' , is_prof : 'bool' , speciality : 'str' ) -> None: ...

    def get_id  (_id : 'str') : ...
    def get_name (_fname : 'str' ) : ...

class Building :
        def __init__(self) -> None: ...
    
class Speciality :
        def __init__(self) -> None: ...

class Log :
        session_counter : 'int' = ...
        tmp_logs : 'list[str]' = ...
        crnt_user_id :'str' = ...
         
        @classmethod
        def dump_log(cls, log_state : 'enm') -> None : ...

        @classmethod 
        def new_log(cls,state : 'enm' , entry_type :'str') -> None : ...

class Credentials : 
    tmp_creds :'dict' = ...
    file_creds_dict : 'dict' = ...

    @classmethod
    def __set_crnt_user(cls) : ...

    @classmethod 
    def set_crnt_user(cls, _final_id) : ...

    @classmethod 
    def new_cred(cls , _pass : 'str' , is_prof : 'str' , _speciality : 'str') -> 'list' : ...

    @classmethod
    def comp_cred (cls, _user : 'str' , _hashed_pass : 'str' ) -> 'tuple' : ...

class Elmenues :

    @staticmethod 
    def main_menu() -> 'enm' : ...

    @staticmethod 
    def new_ac_menu (_hashed_pass : 'str' ) -> 'tuple' : ...

    @staticmethod 
    def loged_menu( log_type : 'enm' , speciality : 'str') : ...

    @staticmethod 
    def sys_menu (id_type : 'enm') : ...


           # ------------------------------- GLOBAL  METHODS --------------------------------#

def main() : ...
def disable_rand_hash_seed() -> 'str' : ...
def get_extra_data ( _final_id : 'str' ) -> None : ...
def connect ( con_typ : 'enm') -> 'enm' : ...




    