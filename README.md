# PySQL 1.1.4
This is actually a python interface to mysql/mariadb based on the CMD library. It is intended to be a user-friendly interface to mysql and mariadb. Installation options for mysql and mariadb on both windows and linux. Comes along with json config where autocommit can be configured to be true or false. Also comes with an embedded user manual. This project comes under the FOSS(Free and open source software) category.

# "AUTOMATE THE BORING STUFF"

# Features
 >Auto OS detection based installation options.
 
 >Decision based commits, configurable through settings file.
 
 
 >Good way to practice SQL without going through the complexities of opening the clients in windows/linux. Just requires a one time setup of a non root       |         account with admin priveleges.
 
 
 >Linux side has more features with decision based distro installation for both mariadb and mysql
 
 >Added install support for Android(Termux). This feature is still experimental. (I just designed it today! 11/8/21) (Would really appreciate, if someone gave   
   feedback on the Android side.)

# Commands
 >start : This will create the connection using the mysql/mariadb connector(depends on choice) and ask for the username, password, host etc. The connection is       
          devoid of any particular database, so allowing to connect to any database.
          
 
 >clear : In case the screen gets messy, simple terminal command to clear screen(irrespective of os)
 
 
 >install_mysql : Installs mysql(auto os detection)
 
 >install_mariadb : Installs mariadb(along with it's connector) (auto os detection)

 >exit : Exits the program(usable in the mysql/mariadb prompt as well)



# Installation 
 >Just do pip install -r requirements.txt or python3 -m pip install -r requirements.txt(on linux)
 
 >Then run pysql_shell.py

# On Termux
 > apt update && apt upgrade && pkg install git python3
 
 Once done, do these :
 > git clone https://github.com/shasankp000/PySQL
 
 >cd PySQL && pip3 install -r requirements.txt --upgrade pip
 
 Lastly,
 
 >python3 pysql_shell.py (to run it do this)

 Inside PySQL, use the install_mariadb_termux command
 
 If you are newcomer to Termux and Linux systems, please learn a quick lesson on changing directories and basic essentials.
 More info on https://wiki.termux.com/ about Termux.


# Note to all users 
 >Requirements.txt does not install mariadb connector by defualt as its installation varies on windows and linux. Use install_mariadb from within PySQL shell.
 
 >Json config file is auto-generated on first-time run.

 >After installation of mariadb on termux, just run mariadb and do CREATE USER "username"@"localhost" IDENTIFIED BY "PASSWORD"; (on a different session, by swiping 
   left and tapping on new session) (works on mysql as well, all platforms)

 >Commands are available in the embedded user manual as well

 >For more info on changing sessions in Termux and general usage go to https://wiki.termux.com/wiki/User_Interface
 
 >Termux is downloadable via https://www.f-droid.org/ . Download the F-droid app and then search termux. Install it from there.
 
 >The Google Play version of Termux doesn't receive updates any more. Consider donating to the Termux Project as well(your choice!).

# In case, you were wondering :

 >I am well aware that another project of the same name exists, however, that PySQL is a framework for sql, it does exactly the same job as this PySQL. However that    being said, this PySQL is an automation of all those manual tasks in the other framework, and deployment is much easier. Only the MySQL/Mariadb service requires    to be started, then PySQL will handle the rest. I am not saying that the original PySQL is not good, i only created this project initially with the intention of    helping my friends, who didn't have a computer at their home, I had no idea that another project with the same name existed. However now I do not intend to      
 > change the name of this project. It's upto you guys, which PySQL you wanna use. 
