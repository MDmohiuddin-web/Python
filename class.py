import email
from re import U
from unicodedata import name


class ussesr:
    name=''
    email=''
    passward=''
    login = False

    def login(self):
        email=imput("enter email: ")
        passward = imput ("enter your passward:  ")
        if email== self.email and passward == self.passward:
            loging = true 
            print ("login successful!")
        else:
            print("login faild!")

    def logout(self):
        login = False
        print("logged out!")
    def isloggedin(self):
        if self.login:
            return true
        else:
            return False

def profle(self):
    if salf.isloggedin():
     print(self.name,"\n",self.email)
    else:
        print("user is not logged in!")



user1 = user()

user1.name = "niamul"
user1.email = "niamulhasanbd@gmail.com"
user1.passward = "12345"

user1.login()
user1.profile( )

helo = input()  
