from pyfiglet import Figlet
from tqdm import tqdm
from cmd import Cmd
import sys
from time import ctime
import time
import os
import platform
import wget
import getpass
import subprocess
import requests
import urllib
import json

usr_accnt = getpass.getuser()
mysql_def_url = "https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.25.0.msi"
plat_name = platform.platform()
cur_dir = os.getcwd()

settings = {
            "sys_info" : [
                {
                    "OS" : platform.platform(),
                    "Machine_Type" : platform.machine(),
                    "Python_Version" : platform.python_version(),
                    "Arch" : platform.architecture(),
                }
            ],
            "MariaDB-autocommit-enabled" : True,
            "MySQL-autocommit-enabled" : True
        }

if not os.path.exists(r"{}/pysql_settings.json".format(cur_dir)):
        print("Generating config file please wait......")
        with open("pysql_settings.json", "w") as js_set:
            json.dump(settings, js_set, indent = 2)
            js_set.close()
        print(r"Config file generated at {}/pysql_settings.json".format(cur_dir))
        print("Use the config file to alter the settings.")
        time.sleep(10)
        if plat_name.startswith("Linux"):
            os.system("clear")
        else:
            os.system("cls")

else:
	pass


with open("pysql_settings.json", "r") as js_read:
        data = json.load(js_read)

mariadb_autocommit_enabled = data["MariaDB-autocommit-enabled"]
mysql_autocommit_enabled = data["MySQL-autocommit-enabled"]
os_type = data["sys_info"][0]["OS"]
py_ver = data["sys_info"][0]["Python_Version"]
mac_type = data["sys_info"][0]["Machine_Type"]

class PySQL(Cmd):
    prompt = "PySQL>"
    f = Figlet(font="straight")
    print(f.renderText("PySQL"))
    intro = f"PySQL 1.1.4 [{ctime()}].Type ? or help for help on commands."
    print(f"Detected Python version : {py_ver}")
    print(f"OS: {os_type} on {mac_type}")
    
    
        
    def do_exit(self,inp):
        '''exit: Exits the application'''
        print("Goodbye!")
        print("--------------------------------")
        return True
        sys.exit(0)

    def do_start(self,inp):
            '''connects to the mysql/mariadb database using provided credentials and host ip.")'''
            q = int(input("MySQL or MariaDB connection? (1/2) : "))
            if q == 1:
                import mysql.connector
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
                    print("Inside MySql prompt now, use quit or QUIT to exit")
                    #Initializing a cursor for the database. Basically it implements subprocess for executing sql queries
                    mycursor = mydb.cursor(buffered=True)
                    while True:
                        try:
                            command = input("mysql>")
                            print(f"Successfully executed command: {command}")
                            #Using the Cursor to execute mysql commands.
                            if command == "show databases" or command == "SHOW DATABASES":
                                mycursor.execute(f"{command};")
                                for x in mycursor:
                                    print(x)
                            elif command == "show tables" or command == "SHOW TABLES":
                                mycursor.execute(f"{command};")
                                for x in mycursor:
                                    print(x)
                            elif command == "quit" or command == "QUIT" or command == "exit" or command == "EXIT":
                                break
                            elif command.startswith("use") or command.startswith("USE"):
                                mycursor.execute(f"{command};")
                                for x in mycursor:
                                    print(x)
                            elif command.startswith("insert") or command.startswith("INSERT"):
                                mycursor.execute(f"{command};")
                                if mysql_autocommit_enabled == True:
                                    mydb.commit()
                                else:
                                    print("Changes not yet committed")
                                print(mycursor.rowcount,"record(s) inserted")
                            elif command.startswith("select") or command.startswith("SELECT"):
                                mycursor.execute(f"{command};")
                                result = mycursor.fetchall()
                                for x in result:
                                    print(x)
                            elif command.startswith("create table") or command.startswith("CREATE TABLE"):
                                mycursor.execute(f"{command};")
                                for x in mycursor:
                                    print(x)
                            elif command.startswith("create database") or command.startswith("CREATE DATABASE"):
                                mycursor.execute(f"{command};")
                                for x in mycursor:
                                    print(x)
                            elif command.startswith("drop table") or command.startswith("DROP TABLE"):
                                mycursor.execute(f"{command};")
                                for x in mycursor:
                                    print(x)
                            elif command.startswith("delete") or command.startswith("DELETE"):
                                mycursor.execute(f"{command};")
                                if mysql_autocommit_enabled == True:
                                    mycursor.commit()
                                else:
                                    print("Changes not yet committed")
                                print(mycursor.rowcount,"record(s) deleted")
                            elif command.startswith("update") or command.startswith("UPDATE"):
                                mycursor.execute(f"{command};")
                                if mysql_autocommit_enabled == True:
                                    mycursor.commit()
                                else:
                                    print("Changes not yet committed")
                                print(mycursor.rowcount, "rows affected")
                            elif command == "commit" or command == "COMMIT":
                                mycursor.commit()
                                print("Changes committed")
                            elif command == "rollback" or command == "ROLLBACK":
                                mycursor.rollback()
                                print("Changes undone")
                            elif command == "clear":
                                if plat_name.startswith("Linux"):
                                    os.system("clear")
                                else:
                                    os.system("cls")
                            else:
                                mycursor.execute(f"{command};")
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
            
            elif q == 2:
                import mariadb
                try:
                    print("--------------------------------")
                    usr = input("Enter username: ")
                    pwd = getpass.getpass("Enter password: ")
                    server = input("Enter host (e.g Localhost/127.0.0.1/ip address of the server): ")
                    print("Connecting to MariaDB Server..")
                    print("Logging in using provided credentials..")
                    for i in tqdm(range(int(100)),ascii=True,desc="Progress"):
                        mrdb = mariadb.connect(
                            host=server,
                            user=usr, #Secondary user account, not root.
                            password=pwd,
                            #auth_plugin="mysql_native_password"
                            )

                    print("Connected to MariaDB server.")
                    print("Login successful")
                    print("You can now execute mariadb commands by typing the commands here.")
                    print("By defualt, autocommit is on. Disable it in settings if you wish to ")
                    print("Inside MariaDB prompt now, use quit or QUIT to exit")
                    mycursor = mrdb.cursor(buffered=True)
                    while True:
                        try:
                            command = input("mariadb>")
                            print(f"Successfully executed command: {command}")
                            #Using the Cursor to execute mysql commands.
                            if command == "show databases" or command == "SHOW DATABASES":
                                mycursor.execute(f"{command};")
                                for x in mycursor:
                                    print(x)
                            elif command == "show tables" or command == "SHOW TABLES":
                                mycursor.execute(f"{command};")
                                for x in mycursor:
                                    print(x)
                            elif command == "quit" or command == "QUIT" or command == "exit" or command == "EXIT":
                                break
                            elif command.startswith("use") or command.startswith("USE"):
                                mycursor.execute(f"{command};")
                                print("Database changed")
                            elif command.startswith("insert") or command.startswith("INSERT"):
                                mycursor.execute(f"{command};")
                                if mariadb_autocommit_enabled == True:
                                    mrdb.autocommit = True
                                elif mariadb_autocommit_enabled == False:
                                    print("Changes not yet committed")
                                    mrdb.autocommit = False
                                print(mycursor.rowcount,"record(s) inserted")
                            elif command.startswith("select") or command.startswith("SELECT"):
                                mycursor.execute(f"{command};")
                                result = mycursor.fetchall()
                                for x in result:
                                    print(x)
                            elif command.startswith("create table") or command.startswith("CREATE TABLE"):
                                mycursor.execute(f"{command};")
                                print("Table created.")
                            elif command == "commit" or command == "COMMIT":
                                mrdb.commit()
                                print("Changes committed")
                            elif command == "rollback" or command == "ROLLBACK":
                                mrdb.rollback()
                                print("Changes undone")
                            elif command.startswith("create database") or command.startswith("CREATE DATABASE"):
                                mycursor.execute(f"{command};")
                                print("Database changed.")
                            elif command.startswith("drop table") or command.startswith("DROP TABLE"):
                                mycursor.execute(f"{command};")
                                print("Table dropped.")
                            elif command.startswith("delete") or command.startswith("DELETE"):
                                mycursor.execute(f"{command};")
                                if mariadb_autocommit_enabled == True:
                                    mrdb.autocommit = True
                                elif mariadb_autocommit_enabled == False:
                                    print("Changes not yet committed")
                                    mrdb.autocommit = False
                                print(mycursor.rowcount,"record(s) deleted")
                            elif command.startswith("update") or command.startswith("UPDATE"):
                                mycursor.execute(f"{command};")
                                if mariadb_autocommit_enabled == True:
                                    mrdb.autocommit = True
                                elif mariadb_autocommit_enabled == False:
                                    print("Changes not yet committed")
                                    mrdb.autocommit = False
                                print(mycursor.rowcount, "rows affected")
                            elif command == "clear":
                                if plat_name.startswith("Linux"):
                                    os.system("clear")
                                else:
                                    os.system("cls")
                            else:
                                mycursor.execute(f"{command};")
                                for x in mycursor:
                                    print(x)
                        except mariadb.Error as e:
                            print(f"Error : {e}")
                            sys.exit(1)  
                  
                except mariadb.Error as p:
                    print(f"Error {p}")

                    print("Connection Failed. You can do the following:")
                    print("1>Check if MariaDB service is running")
                    print("2>Check your credentials")
                    print("3>Check the server ip address")
                    print("4>If mariadb is not installed run install_mariadb command to download and install mysql. This will install the MySQL installer \n msi version 8.0")
                    print("6>Go to bed and try again tomorrow(lol)")


    def do_version(self,inp):
        '''displays shell version'''
        print("PySQL shell v1.1.2")
        print("Python version used at time of writing script : Python 3.9.2 AMD64 on Linux")
        print("MySQL version used at time of writing scirpt : MySQL server 8.0")

    def do_clear(self,inp):
        '''clears the unwanted junk from your screen :)'''
        if plat_name.startswith("Linux"):
            os.system("clear")
            print(f"PySQL 1.1.4 [{ctime()}].Type ? or help for help on commands.")
        else:
            os.system("cls")
            print(f"PySQL 1.1.4 [{ctime()}].Type ? or help for help on commands.")

    def do_date(self,inp):
        '''displays current date and time as per ctime'''
        print(ctime())

    def do_install_mysql(self,inp):
        '''downloads and executes the mysql installer for windows. It download version 8.0 by default'''
        c10 = ""
        r = ""
        c11 = ""
        if plat_name.startswith("Linux"):
            os.system(f"cd /home/{usr_accnt}/Downloads ")
            print("Select your distro within the list options and select ok. If your distro isn't in the list PySQL will opt for alternatives......")
            time.sleep(15)
            os.system("wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.11-1_all.deb && sudo dpkg -i mysql-apt-config_0.8.11-1_all.deb && sudo apt-get update && sudo apt-get install mysql-server && sudo mysql_secure_installation")
            c10 = input("Did the installation succeed? (y/n) ")
            try:
                if c10 == "n":
                    print("Looking up mysql download links...")
                    print("Note this supports only debian and x64 based systems....")
                    print("For other options please visit this link and manually download the correct version : https://dev.mysql.com/downloads/mysql/ ")
                    print("Downloading MySQL server version 8.0 for debian-linux")
                    wget.download("https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-server_8.0.26-1debian10_amd64.deb-bundle.tar", bar=wget.bar_adaptive)
                    print("Running installer......")
                    os.system("tar xvf mysql-server_8.0.26-1debian10_amd64.deb-bundle.tar")
                    os.system(f"sudo apt-get install libaio1")
                    os.system("sudo dpkg -i mysql-{common,community-client,client,community-server,server}_*.deb && sudo apt-get -f install")
                elif c10 == "y":
                    print("MySQL server installation complete")
                    pass
            except:
                print("SSL certificate error detected....trying alternatives....")
                os.mkdir("mysql_server_8.0")
                os.chdir("mysql_server_8.0")
                print("Downloading......")
                r = requests.get("https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-server_8.0.26-1debian10_amd64.deb-bundle.tar", allow_redirects=True)
            
                with open("mysql_server_community_8-0-2.deb-bundle.tar", "wb") as msq:
                    msq.write(r.content)
                    msq.close()
                print("Download complete...installing now.....")
                os.system("tar xvf mysql_server_community_8-0-2.deb-bundle.tar ")
                os.system("sudo apt-get install libaio1")
                os.system("sudo dpkg -i mysql-{common,community-client,client,community-server,server}_*.deb && sudo apt-get -f install")
                c11 = input("Did the installation succeed? (y/n) ")
                if c11 == "y":
                    print("MySQL server installation complete")
                else:
                    print("Rerouting to mariadb server installation....")
                    print("Getting necessary dependencies.....")
                    os.system("cd -")
                    os.mkdir("mariadb")
                    os.chdir("mariadb")
                    os.system("sudo apt -y install git gcc openssl-devel make cmake")
                    os.system("git clone https://github.com/MariaDB/mariadb-connector-c.git")
                    os.system("mkdir build && cd build")
                    os.system("cmake ../mariadb/mariadb-connector-c/ -DCMAKE_INSTALL_PREFIX=/usr")
                    os.system("make")
                    os.system("sudo make install")
                    os.system("pip3 install mariadb")
                    print("Downloading.....")
                    os.system("sudo apt-get install mariadb-server")
                    print("MariaDB installation successful.")

			
			
        else:
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
                	os.chdir(r"c:\users\{}\Downloads\ ".format(usr_accnt))
                	subprocess.call("msiexec /i mysql-installer-community-8.0.25.0.msi")
                	print("Running MySQl installer")
                	print("Run Successful.")
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
        print(f"Detected Python version : {py_ver}")
        print(f"OS: {os_type} on {mac_type}")

    def do_license(self,inp):
        '''displays the license of the project and its author info'''
        print("GNU Public License(GPL) v3.0")
        print("Author : github.com/shasankp000")

    def do_user_manual(self,inp):
        '''This is related to installation of Mysql server and usage of the program'''
        print("--------------------------------")
        print("1>During installation of mysql/mariadb server, make sure to create a second user account as mysql/mariadb connector cannot connect to the root account.")
        print("2>To get started use the start command. Make sure that Mysql service is running(should be by default at startup, though it's recommended to disable startup")
        print("3>Enter your username and password of the second account created during server installation")
        print("4>Enter the server address, by default it's localhost")
        print("5>The program will attempt to connect to the server. If successful, the prompt will change to the default mysql one. Then you can run commands just like on the normal commandline client")
        print("6>The command for custom user creation is same in both mariadb and mysql : CREATE USER 'user1'@localhost IDENTIFIED BY 'password1';")
        print("where user1 is the username and password1 is the password")
        print("7>You might want to : GRANT ALL PRIVILEGES ON *.* TO 'user1'@localhost IDENTIFIED BY 'password1'; as well.")
        print("Any suggestions regarding bugs, errors and improvements/enhancements are welcome. You can drop 'em off at the github page. https://github.com/shasankp000/PySQL")
        print("Thank you for using PySQL :)")
        print("--------------------------------")

    def do_install_mariadb(self,inp):
        '''This installs mariadb and its python connector in your system'''
        file1 = "mariadb-10.6.4-winx64.msi"
        if plat_name.startswith("Windows"):
            os.chdir(r"c:\users\{}\Downloads\ ".format(usr_accnt))
            try:
                print("Checking existence of installer file.....")
                if os.path.exists(file1):
                    print("Existing installer found, removing......")
                    os.remove(file1)
                    print("Downloading MariaDB 10.6.4 installer for Windows (64 bit)")
                    wget.download("https://downloads.mariadb.org/f/mariadb-10.6.4/winx64-packages/mariadb-10.6.4-winx64.msi/from/https%3A//mirror.djvg.sg/mariadb/?serve", bar=wget.bar_adaptive)
                    print("Download successful.\n")
                    os.chdir(r"c:\users\{}\Downloads\ ".format(usr_accnt))
                    subprocess.call("msiexec /i mariadb-10.6.4-winx64.msi")
                    print("Running MySQl installer")
                    print("Run Successful.")
                    print("Getting dependencies........")
                    os.system("pip install mariadb")
                else:
                    print("Downloading MariaDB 10.6.4 installer for Windows (64 bit)")
                    wget.download("https://downloads.mariadb.org/f/mariadb-10.6.4/winx64-packages/mariadb-10.6.4-winx64.msi/from/https%3A//mirror.djvg.sg/mariadb/?serve", bar=wget.bar_adaptive)
                    print("\nDownload successful.")
                    os.chdir(r"c:\users\{}\Downloads\ ".format(usr_accnt))
                    subprocess.call("msiexec /i mariadb-10.6.4-winx64.msi")
                    print("Running MySQl installer")
                    print("Run Successful.")
                    print("Getting dependencies......")
                    os.system("pip install mariadb")
                
            except:
            	print("Download failed. Please check code.")
        
        elif plat_name.startswith("Linux"):
                print("Initializing mariadb server installation....")
                print("Getting necessary dependencies.....")
                os.system("cd -")
                os.mkdir("mariadb")
                os.chdir("mariadb")
                os.system("sudo apt -y install git gcc openssl-devel make cmake")
                os.system("git clone https://github.com/MariaDB/mariadb-connector-c.git")
                os.system("mkdir build && cd build")
                os.system("cmake ../mariadb/mariadb-connector-c/ -DCMAKE_INSTALL_PREFIX=/usr")
                os.system("make")
                os.system("sudo make install")
                os.system("pip3 install mariadb")
                print("Downloading.....")
                os.system("sudo apt-get install mariadb-server")
                print("MariaDB installation successful.")

    def do_install_mariadb_termux(self,inp):
        '''Mysql installation support for Android'''
        print("Updating packages.....")
        print("apt update && apt upgrade -y ")
        try:
            os.system("pkg install mariadb -y")
            os.system("mysql_secure_installation")
            print("Mariadb installation complete.")
            os.system("pip3 install mariadb")
            print("Starting mariadb daemon.......")
            os.system("mysqld_safe -u root &")
        except:
            print("Installation failed, applying fixes....")
            os.chdir("/data/data/com.termux.files/usr/etc")
            if not os.path.exists("/data/data/com.termux.files/usr/etc/my.cnf.d"):
                os.mkdir("my.cnf.d")
                os.system("cd --")
            os.system("pkg install mariadb -y")
            os.system("mysql_secure_installation")
            print("Mariadb installation complete.")
            os.system("pip3 install mariadb")
            print("Starting mariadb daemon.......")
            os.system("mysqld_safe -u root &")


    def do_show_settings(self,inp):
        '''shows the current settings of PySQL'''
        print("==========PySQL Settings==========")
        with open("pysql_settings.json", "r") as js_read:
            s = js_read.read()
            s = s.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
            s = s.replace('\n','')
            s = s.replace(',}','}')
            s = s.replace(',]',']')
            settings_data = json.loads(s)
            print(json.dumps(settings_data, indent=2,))
        print("==================================")
            

PySQL().cmdloop()
