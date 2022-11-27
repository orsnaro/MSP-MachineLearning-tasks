
##########################################################################################
#                                Programmer : Omar Rashad                                #
#                                Version : 0.1 Beta                                      #
#                                Date :  27 / 11 / 2022                                  #
#                                Code Type : Mini_proj for MSP-ML Team                   #
#                                Title : Omar's Emgineering College System               #
#                                                                                        #
#                                                                                        #
#                                                                                        #
##########################################################################################



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