from ast import Try
import email
from multiprocessing.sharedctypes import Value
import re
import mysql.connector
mycon = mysql.connector.connect(host='127.0.0.1',user='root',passwd='',database='project')
mycursor= mycon.cursor()


class my():
    def __init__(self,nu):
        self.nu = nu 
    
    def register():
        print('    REGISTER HERE  ')
        a = input('Enter your Name: ')
        b = input('Enter your EMAIL here: ')
        c = input('Enter your PASSWORD here: ')
        mm = re.findall(r"[@gmail.com,@yahoo.com,@email.com]$",b)
        if mm:
            print('You have successfully registered')
            # my.login()
        else:
            print('invalid input')
        
        myquery= "INSERT INTO admin (Full_Name,Email,Password) VALUES(%s,%s,%s) "
        value=(a,b,c)
        mycursor.execute(myquery,value)
        mycon.commit()
        

    
    def login():
        print('    LOGIN PAGE ')
        email = input('Enter your mail here: ')
        password = input('Enter your password here: ')
        if email:
            query = "SELECT S_N,Full_Name,Email FROM admin WHERE Email=%s AND Password=%s"
            Value=(email,password)
            mycursor.execute(query,Value)
            myreg = mycursor.fetchone()
            print(myreg)
            if myreg[2] == email:
                my.quest()
            else:
                print('invalid email')
        else:
            print('invalid email')
    
    def quest():
        print("""    WELCOME """)
        a = input("Enter question: ")
        b = input("Enter option(a): ")
        c = input("Enter option(b): ")
        d = input("Enter option(c): ")
        e = input("Enter correct answer here: ")
        
        myquery1 ="INSERT INTO questions (Question,Option_a,Option_b,Option_c,Answer) VALUES(%s,%s,%s,%s,%s)"
        value =(a,b,c,d,e)
        mycursor.execute(myquery1, value)
        mycon.commit()
        print(mycursor.rowcount,'successful..')

        next = input('To set more questions ENTER "1",else ENTER "2" to STOP')
        if next == '1':
            my.quest()
        elif next == '2':
            quit()

        




    
