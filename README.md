# PySQL 1.1.4
This is actually a python interface to mysql/mariadb based on the CMD library. Installation options for mysql and mariadb on both windows and linux. Comes along with json config where autocommit can be configured to be true or false. Also comes with an embedded user manual.

# Features
 >Auto OS detection based installation options.
 
 >Decision based commits, configurable through settings file.
 
 
 >Good way to practice SQL without going through the complexities of opening the clients in windows/linux. Just requires a one time setup of a non root       |         account with admin priveleges.
 
 
 >Linux side has more features with decision based distro installation for both mariadb and mysql
 

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


# Note to all users 
 >Requirements.txt does not install mariadb connector by defualt as its installation varies on windows and linux. Use install_mariadb from within PySQL shell.
 
 >Json config file is auto-generated on first-time run
 
