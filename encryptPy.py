import os
from datetime import datetime

file = input("Insert Full Path with file name: ")
dateExpire = input("Insert Date do Expires\n(or click ENTER with you don't whant use it)\n(Example: YY/MM/DD):")
#verify if date is correct

FILE = '"'+file+'"'

if dateExpire == "":
    os.system("pyarmor obfuscate --exact "+FILE)
else:
    licensePath = FILE.split('/')
    licensePath = licensePath[0:-1]
    licensePath = '/'.join(licensePath)+'/licenses"' #licenses storage path
    
    os.system("pyarmor licenses --expired "+dateExpire+" "+licensePath)       
    os.system("pyarmor obfuscate --exact --with-license "+licensePath+"\\license.lic "+FILE)    