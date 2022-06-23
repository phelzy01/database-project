from pickle import TRUE
import re
from tokenize import Number
import mysql.connector
mycon = mysql.connector.connect( host='127.0.0.1', user='root', passwd='', database='project')
mycursor = mycon.cursor()

# score = 0
class myy():
    def __init__(self,nu):
        self.nu = nu
    
    def register():
        print("      REGISTER HERE   ")
        a = input("Enter your name: ")
        b = input("Enter your Email: ")
        c = input("Enter your password: ")
        mm = re.search(r"[gmail.com,email.com,yahoo.com]$",b)
        if mm:
            print(""" You have successfully registered 
            you can proceed to login """)
            # myy.login()
        else:
            print("Enter a valid email")    
            myy.register()
        myreg = "INSERT INTO USER (Full_Name,Email,Password) VALUES (%s,%s,%s)"
        value = (a,b,c)
        mycursor.execute(myreg,value)
        mycon.commit()
    
    def login():
        print("""      LOGIN PAGE  """)
        email= input('Enter your email here: ')
        password = input('Enter your password here: ')
        try:
            if email:
                query = "SELECT S_N,Full_Name,Email FROM USER WHERE Email=%s AND Password=%s "
                value=(email,password)
                mycursor.execute(query,value)
                myreg = mycursor.fetchone()
                print('>>>',myreg)
                if myreg[2] == email:
                    myy.quest()
                    # [myy.quest for i in range(2)]
                else:
                    print('incorrect login')
        except:
            print("enter a valid login")
        
        
    def quest():
            select = int(input(""" >>> Select a number from 1-10: """))
            query = "SELECT * FROM questions WHERE S_N= %s"
            value = (select,)
            mycursor.execute(query,value)
            all =mycursor.fetchone()
            # print(all[0])
            try:
                if all[0] == select:
                    print(all[1])
                    print('(a)',all[2])
                    print('(b)',all[3])
                    print('(c)',all[4])
                    print("Enter your answer here: ")
                    ans=input(">>")
                    query1 = "SELECT Answer FROM questions WHERE Answer = %s"
                    value =(ans,)
                    mycursor.execute(query1,value)
                    dom = mycursor.fetchone()
                    # print(dom)
                    if ans == all[-1]:
                        print("correct")
                        # score += 2
                        myy.quest()
                    else:
                        print("incorrect")
                        # myy.quest()
            except:
                print("enter a valid question")
                # print(myy.quest())

        


        
        
            


