
##########################################################################################
#                                                                                        #
#                                                                                        #
#                                                                                        #
#                          Programmer : Omar Rashad                                      #
#                          Version : 0.1 Beta                                            #
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
#TODO :make porj Tutorial (maybe take your session presentation and summarize it)
#TODO : comment and annotate the rest of non clear code blocks + each file info box like main

from spr import *

def main() :
    print(" \n \n ---------------------( Welcome to Omar's Engineering College System )----------------------\n\n")
    while  RUN :
        exit_state = main_menu() 
        if exit_state == enm.MAIN_MEN_QUIT : sys.exit(enm.MAIN_MEN_OK) 
        else : 
            Log.new_log(enm.UNKNOWN , "Other" ) 
            Log.dump_log(enm.UNKNOWN)
            print("**SYSTEM TERMINATED UNEXPECTEDLY**")
            sys.exit(enm.MAIN_MEN_ER)
    
if __name__ == "__main__":
    main()