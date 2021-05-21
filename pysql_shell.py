import mysql.connector
from pyfiglet import Figlet
from tqdm import tqdm
from cmd import Cmd
import sys
from time import ctime
import os
import platform
import wget
import getpass
import subprocess




usr_accnt = getpass.getuser()
mysql_def_url = "https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.25.0.msi"

class PySQL(Cmd):
    prompt = "PySQL>"
    f = Figlet(font="straight")
    print(f.renderText("PySQL"))
    intro = f"PySQL 1.1.2 [{ctime()}].Type ? or help for help on commands."
    print(f"Detected Python version : {platform.python_version()}")
    print(f"OS: {platform.platform()} on {platform.machine()}")

    def do_exit(self,inp):
        '''exit: Exits the application'''
        print("Goodbye!")
        print("--------------------------------")
        return True
        sys.exit()

    def do_start(self,inp):
            '''connects to the mysql database using provided credentials and host ip.")'''
            try:
                print("--------------------------------")
                usr = input("Enter username: ")
                pwd = getpass.getpass("Enter password: ")
                server = input("Enter host (e.g Localhost/127.0.0.1/ip address of the server): ")
                print("Connecting to Mysql Server..")
                print("Logging in using provided credentials..")
                for i in tqdm(range(int(100)),ascii=True,desc="Progress"):
                    mydb = mysql.connector.connect(
                        host=server,
                        user=usr, #Secondary user account, not root.
                        password=pwd,
                        auth_plugin="mysql_native_password"
                        )
            
                print("Connected to mysql server.")
                print("Login successful")
                print("You can now execute mysql commands by typing the commands here.")
                #Initializing a cursor for the database. Basically it implements subprocess for executing sql queries
                mycursor = mydb.cursor(buffered=True)
                while True:
                    try:
                        command = input("mysql>")
                        mycursor.execute(f"{command};")
                        print(f"Successfully executed command: {command}")
                        #Using the Cursor to execute mysql commands.
                        if command == "show databases" or command == "SHOW DATABASES":
                            for x in mycursor:
                                print(x)
                        elif command == "show tables" or command == "SHOW TABLES":
                            for x in mycursor:
                                print(x)
                        elif command == "quit" or command == "QUIT":
                            sys.exit()
                        elif command.startswith("use") or command.startswith("USE"):
                            for x in mycursor:
                                print(x)
                        elif command.startswith("insert") or command.startswith("INSERT"):
                            mydb.commit()
                            for x in mycursor:
                                print(x)
                        elif command.startswith("select") or command.startswith("SELECT"):
                            mycursor.execute(f"{command};")
                            mycursor.fetchall()
                            for x in mycursor:
                                print(x)
                        elif command.startswith("create table") or command.startswith("CREATE TABLE"):
                            for x in mycursor:
                                print(x)
                        elif command.startswith("create database") or command.startswith("CREATE DATABASE"):
                            for x in mycursor:
                                print(x)
                        elif command.startswith("drop table") or command.startswith("DROP TABLE"):
                            for x in mycursor:
                                print(x)
                        else:
                            for x in mycursor:
                                print(x)

                    except:
                        print(f'ERROR: Failed to execute command, "{command}", most likely wrong command entered.')
                        print("                                  ^(wrong command)")
                    print("")
            except:
                print("Connection Failed. You can do the following:")
                print("1>Check if MySQL service is running")
                print("2>Check your credentials")
                print("3>Check the server ip address")
                print("4>If mysql is not installed run install_mysql command to download and install mysql. This will install the MySQL installer \n msi version 8.0")
                print("6>Go to bed and try again tomorrow(lol)")


    def do_version(self,inp):
        '''displays shell version'''
        print("PySQL shell v1.1.2")
        print("Python version used at time of writing script : Python 3.9.0 AMD64 on win32")
        print("MySQL version used at time of writing scirpt : MySQL server 8.0")

    def do_clear(self,inp):
        '''clears the unwanted junk from your screen :)'''
        os.system("cls")
        print(f"PySQL 1.1.2 [{ctime()}].Type ? or help for help on commands.")

    def do_date(self,inp):
        '''displays current date and time as per ctime'''
        print(ctime())

    def do_install_mysql(self,inp):
        '''downloads and executes the mysql installer for windows. It download version 8.0 by default'''
        os.chdir(r"c:\users\{}\Downloads\ ".format(usr_accnt))
        try:
            file = "mysql-installer-community-8.0.25.0.msi"
            print("Checking existence of installer file.....")
            if os.path.exists(file):
                print("Existing installer found, removing......")
                os.remove(file)
                print("Downloading MySql 8.0 installer for Windows (32 bit)")
                wget.download(mysql_def_url, bar=wget.bar_adaptive)
                print("Download successful.\n")
            else:
                print("Downloading MySql 8.0 installer for Windows (32 bit)")
                wget.download(mysql_def_url, bar=wget.bar_adaptive)
                print("\nDownload successful.")
                os.chdir(r"c:\users\{}\Downloads\ ".format(usr_accnt))
                subprocess.call("msiexec /i mysql-installer-community-8.0.25.0.msi")
                print("Running MySQl installer")
                print("Run Successful.")
                
        except:
            print("Download failed. Please check code.")

    def do_banner(self,inp):
        '''displays the banner'''
        q = Figlet(font="straight")
        print(q.renderText("PySQL"))

    def do_get_sys_info(self,inp):
        '''gets system info and python version'''
        print(f"Detected Python version : {platform.python_version()}")
        print(f"OS: {platform.platform()} on {platform.machine()}")

    def do_license(self,inp):
        '''displays the license of the project and its author info'''
        print("GNU Public License(GPL) v3.0")
        print("Author : github.com/shasankp000")

PySQL().cmdloop()
