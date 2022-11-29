##########################################################################################
#                                                                                        #
#                                                                                        #
#                                                                                        #
#                          Programmer : Omar Rashad                                      #
#                          Version : v0.4 Beta                                           #
#                          Date :  97 / 11 / 2022                                        #
#                          Code Type : sub.pyi => Mini_proj for MSP-ML Committe          #
#                          Title : Omar's Emgineering College System                     #
#                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]  #
#                                                                                        #
#                                                                                        #
#                                                                                        #
##########################################################################################

from spr import *

   #----------------------------------------CHILD CLASSES -----------------------------------------#

class Prof (Person) :
    def save_id (self) : ... 
    def __init__(self, id: str, name: str, age: int, is_prof: bool, speciality: str , rank : int , salary : float) -> None: ...
    def save_id(slef): ...

class Student (Person) : 
    def save_id (self) : ... 
    def __init__(self, id: str, name: str, age: int, is_prof: bool, speciality: str , year : int , GPA : float) -> None: ...
    def save_id(slef): ...

class Lab (Building) : ...  
class hall (Building) : ...  

class Mech (Speciality) : ... 
class Elec (Speciality) : ...


