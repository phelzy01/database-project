from admin import my
from user1 import myy

import mysql.connector
mycon = mysql.connector.connect(host = '127.0.0.1', user='root', passwd = '', database='project')
mycursor = mycon.cursor()

# mycursor.execute('CREATE DATABASE Project')
# mycursor.execute("CREATE TABLE admin (S_N INT (4) PRIMARY KEY AUTO_INCREMENT, Full_Name VARCHAR (70), Email VARCHAR (50), Password VARCHAR(30))")
# mycursor.execute("CREATE TABLE user (S_N INT (4) PRIMARY KEY AUTO_INCREMENT, Full_Name VARCHAR (70), Email VARCHAR(50), Password VARCHAR (30))")
# mycursor.execute("CREATE TABLE questions (S_N INT (4) PRIMARY KEY AUTO_INCREMENT, Question VARCHAR (1000), Option_a VARCHAR (200), Option_b VARCHAR (200), Option_c VARCHAR (200), Answer VARCHAR(300))")
# sql = "DROP TABLE questions"
# mycursor.execute(sql)
# sql = "DROP TABLE user"
# mycursor.execute(sql)
# mycursor.execute('CREATE Table USER (S_N INT (4) PRIMARY KEY AUTO_INCREMENT, Full_Name VARCHAR (100), Email VARCHAR (50), Password VARCHAR (30))')




print("""    Enter 1 to login as Admin
    Enter 2 to login as User """)
choose = input('>>>')
# ADMIN LOGIN
if choose == '1':
    print("""   DO you have an account? 
    If yes Enter '1' If no Enter '2' """)
    choose = input('>>>')
    if choose == '1':
        my.login()
        if my.login == True:
            my.quest()
            # else:
            #     print('Enter a valid email')
    elif choose == '2':
        my.register()
        # my.login()
        # my.quest()

#  USER LOGIN
elif choose =='2':
    print("""    DO you have an account? 
    If yes Enter '1' If no Enter '2' """)
    choose = input('>>>')
    if choose == '1':
        myy.login()
        if myy.login == True:
            myy.quest()
    elif choose == '2':
        myy.register()
        # myy.login()
        
            
        

