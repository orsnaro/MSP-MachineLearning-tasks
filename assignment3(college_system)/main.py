from spr import *

# def main() :
#     print(" \n \n ---------------------( Welcome to Omar's Engineering College System )----------------------\n\n")
#     while  RUN :
#         exit_state = main_menu() 
#         if not exit_state  : sys.exit(enm.MAIN_MEN_OK)
#         else : 
#             print("**SYSTEM TERMINATED UNEXPECTEDLY**")
#             sys.exit(enm.MAIN_MEN_ER)


    
# if __name__ == "__main__":
#     main()

# lis = ["123123", "123123" ,  "213233"]
# lis2= []
# lis2.append(lis)
# lis2.append(lis)
# file = open ( 'test.txt' , 'a' )
# for i in range ( len(lis2)) :
#     for ls in lis2[i] :
#         file.writelines(ls + ' ')
#     file.writelines('\n')
# file.close()
# file.write('1234')
# file.close()
# file = open ( 'test.txt', 'r')
# file_red = file.read()
# print ( file_red)

# print(file.seek(1))
# print(file.tell())
# file_red = file.read(1)
# print ( file_red)
# print(file.tell())
# file_red = file.read(1)
# print ( file_red)
# file_red = file.read(1)
# print ( file_red)
# file.close()
# file = open ( 'test.txt', 'a')
# file.write('omar')
tmp_logs = []

#TODO : later add acc_id = crnt_session_user_id to new_entry()
def new_log (state : enm , entry_type = -1 , pc_name = getpass.getuser()) -> enm :
    Log.incCntr()
    instance = [str(datetime.datetime.now()) , str(state) ,str(entry_type) , str(pc_name)]
    tmp_logs.append(instance)

new_log( "ok" , '-1')
new_log( "ok" , '-1')
new_log( "ok" , '-1')

log_file = open (r"log.txt", 'a')
for i in range ( len(tmp_logs)) :
    for log in tmp_logs[i] :
        log_file.writelines(log + ' ')
    log_file.writelines('\n')
log_file.close()
# tup = ("123123", "213233")
# file = open ("test.txt", 'a')
# file.writelines(str(lis))


# instance = [str(datetime.datetime.now()) , str(state) ,str(entry_type) , str(pc_name)]
# tmp_logs.append(str(instance)+'\n')
# for i in range(100):
#     print ( random.randint(10000,99999))

