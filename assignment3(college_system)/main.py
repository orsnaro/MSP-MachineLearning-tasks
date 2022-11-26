from sub import *
from spr import *

# def main() :
#     print(" \n \n ---------------------( Welcome to Omar's Engineering College System )----------------------\n\n")
#     while  RUN :
#         exit_state = main_menu() 
#         if not exit_state  : sys.exit(enm.MAIN_MEN_OK)
#         else : 
#             print("**SYSTEM TERMINATED UNEXPECTEDLY**")
#             sys.exit(enm.MAIN_MEN_ER)
def enter_pass() :
    sys_gmail_password = getpass.getpass("ADMIN Please Enter Your college system gmail password : \n>> ").strip()
    print("  ", end = '')
    for i in range(len(sys_gmail_password)) :
        print ('*' ,  end ='')
    print ('\n')
    print (sys_gmail_password)
    return sys_gmail_password

def gmail_connect() : 
    print ( "Starting  new Connection session with Gmail... \n\n")
    state = api_gmail.main_gmail() #validate that google auth your program through a saved carden file
    if  state == enm.GMAIL_OK : 
        print ("*SUCESSS: Gmail-Api Granted Access to System Succesfully!* \n\n")
    else :
        print("*FAIL: System might not Be  validated to Access  gmail!* \n please Auth. your system program  OR check your auth. certificate file... \n\n")

    try:
        port = 465  # For SSL -> other SMTP serverports can be found in web
        from_sys_gmail ="omar1xd@gmail.com"
        sys_key = enter_pass()
        to_gmail_add = input("Please Enter you Gmail Address ex.: test@gmail.com \n>> ").strip()

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            #establish smtp ssl gmail server session
            print("linking college system  Gmail to SMTP_SSL Gmail server...\n\n ")
            time.sleep(1)
            server.login(from_sys_gmail, sys_key)
        sys_key = hash (sys_key) #hash it for your own security
        print ("*SUCESSS: college system is linked to SMTP_SSL server* \n\n")
        
        #try send Your message here using - > server.sendmail()
        message = f"-------( *THIS IS TEST MESSAGE* )------- \n\n\n You Have Successfully created your College Account!\n\n " \
                "Please  note that you won't be able to retrieve your Login Data, \n So keep Them somewhere  SAFE!\n\n" \
                f" USER NAME : test_message\n PASSWORD : test_message \n\n -------*PLEASE DON'T REPLY TO THIS MESSAGE*-------"
        server.sendmail(from_sys_gmail , to_gmail_add , message)

    except Exception as gmail_con_err :
        os.system(r"clear")
        print("*ERROR CONNECTING TO YOUR GMAIL*")
        os.system(r"clear")
        print("***ERROR CONNECTING TO YOUR GMAIL***")
        print(gmail_con_err,"\n\n")
        gmail_connect()
    

    finally : 
        print (f"*SUCESSS: registration Email Has been sent to {to_gmail_add} * \n\n")
        to_gmail_add = None #clear for end user data security
        sys_key = None 
        from_sys_gmail = None
        print("*Gmail Session Ended* \n Deleting Cached User Data & Quiting session ...\n\n")
        server.quit()

    
gmail_connect()
# if __name__ == "__main__":
    # main()

    #simple email test
