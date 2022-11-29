##########################################################################################
#                                                                                        #
#                                                                                        #
#                                                                                        #
#                          Programmer : Omar Rashad                                      #
#                          Version : v0.4 Beta                                           #
#                          Date :  29 / 11 / 2022                                        #
#                          Code Type : api_gmai.py = > Mini_proj for MSP-ML Committe     #
#                          Title : Omar's Emgineering College System                     #
#                          Interpreter : cPython  v3.11.0 [Compiler : MSC v.1933 AMD64]  #
#                                                                                        #
#                                                                                        #
#                                                                                        #
##########################################################################################


from __future__ import print_function
from enm import enm

import getpass
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main_gmail():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'my_proj_gamil_creds.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        #uncomment next 2 lines to grant access using API_KEY 
        # API_KEY : str = ... #from your google cloud project
        # service = build ( 'gmail' , 'v1' , developerKey= API_KEY)

        #comment nextline if u used API_KEY
        service = build('gmail', 'v1', credentials=creds)
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        # if not labels:
        #     print('No labels found.')
        #     return 
        # print('Labels:')
        # for label in labels:
        #     print(label['name'])

    except HttpError as error:
        print(f'An error occurred: {error}')
        return enm.GMAIL_BAD

    return enm.GMAIL_OK


def enter_pass() :
    sys_gmail_password = getpass.getpass("ADMIN Please Enter Your college system gmail password : \n>> ").strip()
    print("  ", end = '')
    for i in range(len(sys_gmail_password)) :
        print ('*' ,  end ='')
    print ('\n')
    print (sys_gmail_password)#for test
    return sys_gmail_password

def gmail_connect() : 
    print ( "Starting  new Connection session with Gmail... \n\n")
    state = main_gmail() #validate that google auth your program through a saved carden file
    if  state == enm.GMAIL_OK : 
        print ("*SUCESSS: Gmail-Api Granted Access to System Succesfully!* \n\n")
    else :
        print("*FAIL: System might not Be  validated to Access  gmail!* \n please Auth. your system program  OR check your auth. certificate file... \n\n")

    try:
        # port = 465  # For SSL -> other SMTP serverports can be found in web
        port = 587
        from_sys_gmail ="system.python.web@gmail.com"
        sys_key = enter_pass()
        to_gmail_add = input("Please Enter you Gmail Address ex.: test@gmail.com \n>> ").strip()

        # Create a secure SSL context
        context = ssl.create_default_context()

        server = smtplib.SMTP("smtp.gmail.com",port)
        #establish smtp ssl gmail server session
        server.starttls(context = context)
        server.login(from_sys_gmail, sys_key)
        print("linking college system  Gmail to SMTP_SSL Gmail server...\n\n ")
        sys_key = hash (sys_key) #hash it for your own security
        # time.sleep(1)
        print ("*SUCESSS: college system is linked to SMTP_SSL server* \n\n")
        
        #try send Your message here using - > server.sendmail()
        message = """---------( *THIS IS TEST MESSAGE* )--------- \n\n\nYou Have Successfully created your College Account!\n\n 
        Please  note that you won't be able to retrieve your Login Data, \nSo keep Them somewhere  SAFE!\n\n
        USER ID: test_message\nPASSWORD : test_message \n\n -------*PLEASE DON'T REPLY TO THIS MESSAGE*-------"""
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

if __name__ == '__main__':
    gmail_connect()