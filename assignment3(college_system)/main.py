from spr import *

def main() :
    print(" \n \n ---------------------( Welcome to Omar's Engineering College System )----------------------\n\n")
    while  RUN :
        exit_state = main_menu() 
        if not exit_state  : sys.exit(enm.MAIN_MEN_OK)
        else : 
            print("**SYSTEM TERMINATED UNEXPECTEDLY**")
            sys.exit(enm.MAIN_MEN_ER)

    
# if __name__ == "__main__":
#     main()


class test :
    tmp_creds = dict()
    @classmethod
    def dump_cred(cls, cred_state: enm) -> enm:

        cred_file = open (r"cred.txt" , 'a')
        for id , hashed  in cls.tmp_creds.items() :
                cred_file.writelines( id + ' ' + str(hashed) + '\n')
        cred_file.close()

    @classmethod
    def set_crnt_user(cls) :
        pass
        # Log.crnt_user_id = cls._user_id

    @classmethod
    def new_cred (cls , _pass : str) : #assume passwords gets here are validated before
        _pass = hash(_pass) # make sure hash seed is set to 0 !
        cls._user_id = str(random.randint(10000000,99999999))
        cls.tmp_creds[cls._user_id] = _pass
        cls.set_crnt_user()

test.new_cred ("12345678")
test.new_cred ("12345678")
test.new_cred ("12345678")
test.new_cred ("12345678")
test.new_cred ("12345678")

test.dump_cred(enm.CON_BAD_DATA)