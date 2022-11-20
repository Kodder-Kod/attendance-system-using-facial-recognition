from kok import *
from homepage import *
from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

class create():
    def __init__(self,root):
        self.root = root
        self.root.title('Create Acc')
        self.root.geometry('1000x550')
        self.root.configure(bg="#ffffff")

        self.frame5 = Frame(self.root)
        self.frame5.config(bg='#ffffff')
        self.frame5.place(x=0, y=0, width=1000, height=1000)

        self.frame4 = Frame(self.root)
        self.frame4.config( bg='slate blue')
        self.frame4.place(x=550, y=0, width=1000, height=1000)

        Label(self.frame4, text="Already have An ", font=("Times", 25), bg='slate blue', fg='white').place(x=100, y=70)
        Label(self.frame4, text="Account", font=("Times", 25), bg='slate blue',fg='white').place(x=150, y=105)
        Label(self.frame4, text="Sign In", font=("Times", 30), bg='slate blue',fg='white').place(x=150, y=140)

        def login1():
            return login()

        Button(self.frame4, text="Sign In ", font=20, width=11, height=1,command=login1).place(x=170, y=400)

        Label(self.frame5,text="Create Account", font=("Times",25),bg= 'white').place(x=150,y=30)

        Label(self.frame5,text='Name',font =23 ,bg='white').place(x=105 ,y= 100)
        Label(self.frame5,text="Email",font =23 ,bg= 'white').place(x=105 ,y= 160)
        Label(self.frame5,text="Phone ",font =23 ,bg= 'white').place(x=105 ,y= 220)
        Label(self.frame5,text="Password ",font =23 ,bg= 'white').place(x=105 ,y= 280)
        Label(self.frame5,text="Confirm Password",font =23 ,bg= 'white').place(x=105, y=340)

        nameValue = StringVar()
        emailValue = StringVar()
        phoneValue = StringVar()
        passValue = StringVar()
        conpassValue = StringVar()

        nameEntry= Entry(self.frame5,textvariable =nameValue, width=30 ,bd =0,font=20 ).place(x=110,y=125)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=110, y=145)
        emailEntry= Entry(self.frame5,textvariable =emailValue, width=30 ,bd =0 ,font=20).place(x=110,y=185)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=110, y=205)
        phoneEntry= Entry(self.frame5,textvariable =phoneValue, width=30 ,bd =0 ,font=20).place(x=110,y=245)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=110, y=265)
        passEntry= Entry(self.frame5,textvariable =passValue, width=30 ,bd =0 ,font=20 ,show='*').place(x=110,y=305)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=110, y=325)
        conpassEntry= Entry(self.frame5,textvariable =conpassValue, width=30 ,bd =0 ,font=20, show='*').place(x=110,y=365)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=110, y=385)

        def submit():
            return board()

        btn = Button(self.frame5, text="register ", font=20, width=11, height=1, command=submit).place(x=180, y=420)


def create1():
    root1=Tk()
    create(root1)
    root1.mainloop()

if __name__=='__main__':
    create1()

