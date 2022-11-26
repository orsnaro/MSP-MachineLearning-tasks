from spr import *

def main() :
    print(" \n \n ---------------------( Welcome to Omar's Engineering College System )----------------------\n\n")
    while  RUN :
        exit_state = main_menu() 
        if not exit_state  : sys.exit(enm.MAIN_MEN_OK)
        else : 
            print("**SYSTEM TERMINATED UNEXPECTEDLY**")
            sys.exit(enm.MAIN_MEN_ER)

    
if __name__ == "__main__":
    main()


# class test :
   