##########################################################################################
#                                                                                        #
#                                                                                        #
#                                                                                        #
#                          Programmer : Omar Rashad                                      #
#                          Version : v0.1 Beta                                           #
#                          Date :  27 / 11 / 2022                                        #
#                          Code Type : main.Mini_proj for MSP-ML Committe                #
#                          Title : Omar's Emgineering College System                     #
#                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]  #
#                                                                                        #
#                                                                                        #
#                                                                                        #
##########################################################################################
#TODO : make function signal flow diagram
#TODO : make README.md  and seperate the proj to it's own repo
#TODO : make porj Tutorial (maybe take your session presentation and summarize it)
#TODO : comment and annotate the rest of non clear code blocks + each file info box like main
#TODO : for later : make more robust exception handling + fix gmail feature +  upload cred.txt to cloud and make  cloud.py 

# from spr import main
    
# if __name__ == "__main__":
#     main()
lis = []
class Student :  #study_year  #current_GPA  #fees_must_pay

   def __init__(self, id: str, name: str, age: int, is_prof: bool, speciality: str , year : int ,  GPA : float ) -> None:
        self.id = id #could make em in one line i know
        self.name = name
        self.age = age 
        self.is_prof = is_prof
        self.speciality = speciality
        self.year = year
        self.GPA = GPA
        self.save_id()
   
   def make_tmp_dic (self) :
      self.tmp_dic[self.id] = [f"name : {self.name}" , f"age : {self.age}" , f"Previlage : {'Professor' if self.is_prof == True else 'Student' }" , f"Department : {self.speciality}" , f"Study Year : {self.year}" , f"Current GPA : {self.GPA}"  ]

   def save_id(self) : 
      lis.append(self.tmp_dic) 


s1 = Student("1313" , 'omar' , 21 , True , "elec" , 21 , 4.1 )
print (lis)