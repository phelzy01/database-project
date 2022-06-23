
# import email
import re
import mysql.connector
mycon = mysql.connector.connect(host = '127.0.0.1', user= 'root', passwd='', database='project')
mycursor = mycon.cursor()



class myy():
    def __init__(self,nu):
        self.nu = nu
    
    def register():
        print('    REGISTER HERE  ')
        a = input('Enter your Name: ')
        b = input('Enter your EMAIL here: ')
        c = input('Enter your PASSWORD here: ')
        mm = re.findall(r"[@gmail.com,@yahoo.com,@email.com]$",b)
        if mm:
            print('''You have successfully registered 
            YOU can proceed to Login now''')
            # myy.login()
        else:
            print('invalid input')
            myy.register()
        myquery = "INSERT INTO user (Full_Name, Email, Password) VALUES(%s,%s,%s)"
        value=(a,b,c)
        mycursor.execute(myquery,value)
        mycon.commit()     
        
    
    def login():
        print('    LOGIN PAGE ')
        email = input('Enter your mail here: ')
        password = input('Enter your password here: ')
        # res = re.search(r"[@gmail.com,@yahoo.com,@email.com]$",email)
        # try:
        # try:   # res = re.findall(r"[@gmail.com,@yahoo.com,@email.com]$",email)
        if email:
            query = "SELECT S_N,Full_Name,Email FROM user WHERE Email=%s AND Password=%s"
            value = (email,password)
            mycursor.execute(query, value)
            myreg = mycursor.fetchone()
            print(myreg)
            try:
                if myreg[2] == email:
                    myy.quest()
                # else:
                #     print('invalid email...')
            except:
                print("invalid login details")
                # myy.login()
        else:
            print('invalid email')
            # myy.login()
        # except:
        #     print('invalid details..')


        # except:
        #        print('invalid email', email)

    
    def quest():
        # try:
            select = int(input("SELECT a question from 1-10:  "))
            query = "SELECT * FROM questions WHERE S_N= %s "
            value = (select,)
            mycursor.execute(query,value)
            com = mycursor.fetchone()
            if com:
                print(com[1])
                print('(a)',com[2])
                print('(b)',com[3])
                print('(c)',com[4])
            ans= input("Enter your answer(option) here: ")
            query1= "SELECT Answer FROM questions WHERE Answer= %s"
            value = (ans,)
            mycursor.execute(query1,value)
            nm = mycursor.fetchone()
            # try:
            if ans == nm[-1]:
                print('correct')
                myy.quest()
                # print('select "1" to CONTINUE to another question or "2"mto End questions')
                # select1= int(input(">>>"))
                # if select1 == '1':
                #     myy.quest()
                # elif select1 =='2':
                #     print('one')
                #     quit()
                                    
            else:
                print('incorrect answer')
        # except:
        #     print('incorrect')
        # except:
        #     print('invalid input')
        #     myy.quest()
        
    
    # def questc():
    #     print('')

        




            
