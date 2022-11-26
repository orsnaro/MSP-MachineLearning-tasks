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
file = open ( 'test.txt' , 'a' )
# for i in range ( len(lis2)) :
#     for ls in lis2[i] :
#         file.writelines(ls + ' ')
#     file.writelines('\n')
# file.close()
file.write('1234')
file.close()
file = open ( 'test.txt', 'r')
file_red = file.read()
print ( file_red)

print(file.tell())
# tup = ("123123", "213233")
# file = open ("test.txt", 'a')
# file.writelines(str(lis))


# instance = [str(datetime.datetime.now()) , str(state) ,str(entry_type) , str(pc_name)]
# tmp_logs.append(str(instance)+'\n')
# for i in range(100):
#     print ( random.randint(10000,99999))

