import os
from datetime import datetime

file = input("Insert Full Path with file name: ")
dateExpire = input("Insert Date do Expires\n(or click ENTER with you don't whant use it)\n(Example: YY/MM/DD):")
#verify if date is correct

FILE = '"'+file+'"'

if dateExpire == "":
    os.system("pyinstaller --onefile --noconsole "+FILE)
else:
    licensePath = FILE.split('/')
    licensePath = licensePath[0:-1]
    licensePath = '\\'.join(licensePath)+'\\licenses"' #licenses storage path
    
    os.system("pyarmor licenses --expired "+expireDate+" "+licensePath)       
    os.system('pyarmor pack -e " --onedir --onefile --noconsole" --with-license '+licensePath+'\\license.lic '+FILE)   