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

prof = False
lis = []
class test :

    def __init__(self , name) -> None:
        self.name = name
        self.save_id()
    def save_id (self) :
        lis.append(self.name)
        
a = test('omar')       
print (lis)



print (f"oamr :  { 'true' if prof is True else 'false'}")
