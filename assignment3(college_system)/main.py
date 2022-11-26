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

# def gmail_connect() : 
#     print ( "Starting Connection session with Gmail... \n\n")
#     state = api_gmail.main_gmail() #validate that google auth your program through a saved carden file
#     if  state == enm.GMAIL_OK : 
#         print ("*SUCESSS: Gmail-Api Granted Access to System Succesfully!* \n\n")
#     else :
#         raise Exception("*FAIL: System might not Be  validated to Access  gmail!* \n please Auth. your system program  OR check your auth. certificate file... \n\n")

#     port = 465  # For SSL -> other SMTP serverports can be found in web
#     from_sys_gmail ="system_python.web@gmail.com"
#     sys_gmail_password = getpass.getpass("Please Enter Your gmail sys_gamail_pass : \n>> ").strip()
#     to_gmail_add = input("Please Enter you Gmail Address ex.: test@gmail.com \n>> ").strip()
#     try:
#         # Create a secure SSL context
#         context = ssl.create_default_context()

#         with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#             #establish smtp ssl gmail server session
#             print("linking college system  Gmail to SMTP_SSL Gmail server...\n\n ")
#             server.login(from_sys_gmail, sys_gmail_pass)
#             raise Exception(f"*Fail: Couldn't Connect TO SMTP_SSL Server with PORT = {port}*\n\n")
#         sys_gamail_pass = hash (sys_gamail_pass) #hash it for your own security
#         print ("*SUCESSS: Gmail-Api Granted Access to System Succesfully!* \n\n")
        
#         #try send Your message here using - > server.sendmail()

#     except Exception as gmail_con_err :
#         os.system(r"clear")
#         print("*ERROR CONNECTING TO YOUR GMAIL*")
#         os.system(r"clear")
#         print("***ERROR CONNECTING TO YOUR GMAIL***")
#         print(gmail_con_err)
#         gmail_connect()
    

#     finally : 
#         to_gmail_add = None #clear for end user data security
#         sys_gmail_password = None 
#         from_sys_gmail = None
#         print("*Gmail Session Ended* \n Deleting Cached User Data & Quiting session ...\n\n")
#         server.quit()

    
    # gmail_connect()

x = int(5)
raise  Exception("test")
# if __name__ == "__main__":
    # main()

    #simple email test
