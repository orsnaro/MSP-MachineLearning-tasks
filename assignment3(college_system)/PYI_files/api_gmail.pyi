##########################################################################################
#                                                                                        #
#                                                                                        #
#                                                                                        #
#                          Programmer : Omar Rashad                                      #
#                          Version : v0.4 Beta                                           #
#                          Date :  29 / 11 / 2022                                        #
#                          Code Type : api_gmail.pyi => Mini_proj for MSP-ML Committe    #
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

SCOPES : ...

def main_gmail () : ...
def enter_pass() : ...
def gmail_connect () : ...

