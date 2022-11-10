from inspect import getmembers , isfunction ,isclass , ismethod
import os ,signal

pid = 14044
os.kill(pid, signal.SIGTERM)##terminate

# print ( getmembers(os,isfunction))
# os.system("cls")
# print(type(os.name))
# print(os.error)
# os.rmdir("testforshell")
# print(os.getcwd())
# cwd = os.getcwd()
# os.chdir("../")
# print ( cwd )
# for dirpath,dirnames,filenames in  os.walk(cwd) :
#     print (dirpath)
#     print ( dirnames) 
#     print (filenames)    


