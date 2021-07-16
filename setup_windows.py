import getpass
import os

usr_accnt = getpass.getuser()
os.system(r'pyinstaller --onefile --add-data "C:\Users\{}\AppData\Local\Programs\Python\Python38\Lib\site-packages\pyfiglet;./pyfiglet" pysql_shell.py'.format(usr_accnt))

