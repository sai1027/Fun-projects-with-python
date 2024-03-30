import random
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="pydb")
cursor=mydb.cursor()


def login():
    user_name=input("Username : ")
    password=input("Password : ")
    x="select * from guess where username=%s"
    cursor.execute(x,(user_name,))
    ans=cursor.fetchall()
    if ans[0][1]==password:
        print("login successfull..")
        game(user_name)

    else :
        print("login not successfull..")
        print("try again..")
        login()

def register():
    user_name=input("create user name : ")

    x="select * from guess where username=%s"

    cursor.execute(x,(user_name,))
    ans=cursor.fetchall()
    if ans:
        print("user name already exist. Try new..")
        register()
    password=input("create password : ")
    x="insert into guess values(%s,%s,100)"
    cursor.execute(x,(user_name,password,))
    mydb.commit()
    print("login to play..")
    login()

def score(name):
    x="select score from guess where username= %s "
    cursor.execute(x,(name,))
    s=cursor.fetchall()
    return s[0][0]


def game(name):
    number=random.randint(1,50)
    flag=0
    print("your score is : ",score(name))

    level=input("which level easy / hard : ").lower()

    if level=='easy':
        chance=10
    elif level=='hard':
        chance=5
    else :
        print('enter only easy / hard ..')

    print('guess the number 0 to 50 : ')
    for i in range(chance):
        guess=int(input(f"you have {chance-i} chances left : " ))

        if guess==number:
            print("hurray !.. you got it..")
            flag=1
            x="update guess set score=score+10 where username=%s"
            cursor.execute(x,(name,))
            mydb.commit()
            print("your score is : ",score(name))
            break

        elif guess>number:
            print('too high ')
        elif guess<number :
            print('too low ')

    if flag==0:
        print("dont worry... try again")
        cursor.execute("update guess set score=score-5 where username='name'")
        mydb.commit()
        print("your score is : ",score(name))

    responce=input("want to play again y / n : ")
    if responce=='y':
        game(name)
    else :
        print("Bye for now.. have a nice day :) ")


def verify():
    a=int(input("1.login\n2.register\n"))
    if a==1:
        login()
    elif a==2:
        register()
    else :
        print("enter 1 for old user, 2 for new user : ")
        verify()



# main menu

verify()
