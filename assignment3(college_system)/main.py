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

# # get credential from text sample code 
# from_txt_dict = {}
# f = open( r"cred.txt" , 'r')
# for i in range 
# red = f.read(28)
# red.strip()
# id , hashed = red.split(' ')
# print ( id ,hashed )
# print (type (red) , red)
    

# f = open( r"cred.txt" )

with open('cred.txt' ) as f :
    for line  in f :
        print (line )

# cntr = -1
# red = ''
# while True :
#     cntr += 1
#     char = f.read(1)
#     red = red + char
#     if ( char == '') : break

# cntr = 0
# dic = {}
# tmp ,tmp2 = str() , str()
# for i in  red.split() :
#     cntr += 1
#     if  cntr % 2 == 0  :
#         tmp2 = i.strip() 
#         dic[tmp] = tmp2
#     else :
#         tmp = i.strip()

# print (dic)
        

# line_off = cntr 
# print ( red )
# print ( line_off )
# test.new_cred ("12345678")
# test.new_cred ("12345678")
# test.new_cred ("12345678")
# test.new_cred ("12345678")
# test.new_cred ("12345678")

# test.dump_cred(enm.CON_BAD_DATA)