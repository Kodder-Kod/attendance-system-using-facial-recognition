from homepage import *
from tkinter import *
from tkinter import messagebox
import mysql.connector as sa
import re

class Create():
    def __init__(self,root):
        root.title('Create Acc')
        root.geometry('1000x550')
        root.configure(bg="#fff")
        root.resizable(0, 0)

        frame2 = Frame(root, bg='slate blue').place(x=550, y=0, width=1000, height=1000)

        Label(frame2, text="Already have An ", font=("Times", 25), bg='slate blue', fg='white').place(x=650, y=70)
        Label(frame2, text="Account", font=("Times", 25), bg='slate blue', fg='white').place(x=700, y=105)
        Label(frame2, text="Sign In", font=("Times", 30), bg='slate blue', fg='white').place(x=700, y=140)

        btn = Button(root, text="Sign In ", font=20, width=11, height=1).place(x=720, y=400)

        Label(root, text="Create Account", font=("Times", 25), bg='white').place(x=150, y=30)

        Label(root, text='Name', font=23, bg='white').place(x=105, y=100)
        Label(root, text="Email", font=23, bg='white').place(x=105, y=160)
        Label(root, text="Phone ", font=23, bg='white').place(x=105, y=220)
        Label(root, text="Password ", font=23, bg='white').place(x=105, y=280)
        Label(root, text="Confirm Password", font=23, bg='white').place(x=105, y=340)

        nameValue = StringVar()
        emailValue = StringVar()
        phoneValue = StringVar()
        passValue = StringVar()
        conpassValue = StringVar()

        nameEntry = Entry(root, textvariable=nameValue, width=30, bd=0, font=20).place(x=110, y=125)
        Canvas(root, width=250, height=2.0, bg='#000000').place(x=110, y=145)
        emailEntry = Entry(root, textvariable=emailValue, width=30, bd=0, font=20).place(x=110, y=185)
        Canvas(root, width=250, height=2.0, bg='#000000').place(x=110, y=205)
        phoneEntry = Entry(root, textvariable=phoneValue, width=30, bd=0, font=20).place(x=110, y=245)
        Canvas(root, width=250, height=2.0, bg='#000000').place(x=110, y=265)
        passEntry = Entry(root, textvariable=passValue, width=30, bd=0, font=20, show='*').place(x=110, y=305)
        Canvas(root, width=250, height=2.0, bg='#000000').place(x=110, y=325)
        conpassEntry = Entry(root, textvariable=conpassValue, width=30, bd=0, font=20, show='*').place(x=110, y=365)
        Canvas(root, width=250, height=2.0, bg='#000000').place(x=110, y=385)

        def submit():
            return submit1()

        btn = Button(root, text="register ", font=20, width=11, height=1, command=submit).place(x=180, y=420)

        def submit1():
            name = nameValue.get()
            email = emailValue.get()
            phone = phoneValue.get()
            pas = passValue.get()
            con = conpassValue.get()

            mailform = re.findall('@', email)
            phoneform = re.findall('[^0-9]', phone)
            pasformsmall = re.findall('[a-z]', pas)
            d = pasformsmall
            passformbig = re.findall('[A-Z]', pas)
            e = passformbig
            passformnum = re.findall('[0-9]', pas)
            f = passformnum

            if (name and email and phone and pas):
                try:
                    conn = sa.connect(host="localhost", user="root", password="", database="Recon")
                    cur = conn.cursor()  # assign cursor
                    sql = "CREATE TABLE IF NOT EXISTS test( Name varchar(100) not null,Email  varchar(100) not null,Phone int(15) not null,Password  varchar(40) not null ) "
                    cur.execute(sql)  # execute the query

                    pin = "INSERT INTO  Admin (Name,Email,Phone,Password) Values(%s,%s,%s,%s)"
                    nip = ((name), (email), (phone), (pas))
                    print('lol')
                    cur.execute(pin, nip)
                    conn.commit()

                    Home()

                    conn.close()
                except:
                    print('Can not connect to the Database')

            else:
                messagebox.showerror('ALL FIELDS MUST BE FILLED', parent=root)


class Form:
    #aasign tk to root

    def __init__(self,root):
        root.title('Login')# add title
        root.geometry('1000x550') # geometry

        root.configure(bg="#fff") # color of background
        root.resizable(0,0) # don`t  change size

        # label title

        frame1=Frame(root, bg='slate blue').place(x=0 ,y=0 , width=500,height=1000)
        frame2=Frame(root, bg='#ffffff').place(x=400, y=0 ,width=1000 ,height=1000)


        Label(root, text="Create Account", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=90, y=50)
        Label(frame1, text="And ", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=150, y=80)
        Label(frame1, text=" Explore", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=125, y=110)
        Label(frame1, text="E-AT APP", bg='slate blue', fg='#ffffff', font=('Times', 30)).place(x=90, y=140)

        Label(frame2,text='E-AT APP',font=('Times',40),bg='#ffffff').place(x=560,y=30)
        Label(root, text='Sign In', font=('Times', 20), bg='#ffffff').place(x=640, y=140)

        #text in form
        Label(frame2,text='Email',font =23 ,bg= '#ffffff').place(x=550,y= 200)
        Label(frame2,text="Password",font =23 ,bg= '#ffffff').place(x=550 ,y= 280)

        #assign string  variable to tkinter
        nameValue=StringVar()
        passValue=StringVar()


        #Input
        nameEntry= Entry(frame2,textvariable =nameValue, width=28 ,bd =0 ,font=20).place(x=550,y=225,height=30)
        Canvas(root,width=250,height=2.0,bg='#000000').place(x=550,y=250)
        passEntry= Entry(frame2,textvariable =passValue, width=28 ,bd =0 ,font=20, show='*').place(x=550,y=305,height=30)
        Canvas(root, width=250, height=2.0, bg='#000000').place(x=550, y=330)

        #assign int variable to tkinter
        checkValue =IntVar()
        #checkbox
        checkbtn=Checkbutton(frame2,text='remember me ?',variable= checkValue, cursor='hand2',bg="#ffffff").place (x=550,y=350)#
        # label in forgot
        Label(root,text= 'Forgot Password', font=('Times', 10, "underline"), fg='blue', bg= '#ffffff', cursor='hand2').place(x=800,y=480)

        def submit():
            name = nameValue.get()
            pas = passValue.get()

            # connect to mysql
            if (name and pas):
                conn = sa.connect(host='localhost', user='root', password='', database='Recon')
                cur = conn.cursor() #  assign cursor
                lol = "select name from Admin where Name =%s and Password=%s"
                cur.execute(lol,[(name),(pas)])
                result = cur.fetchall()

                if result:

                    Home()

                else:
                    messagebox.showerror('Username or Password  are invaild',parent=root)
                    conn.close()
            else:
                messagebox.showerror("All Fields must be Filled", parent=root)


        #button of sign in
        def create1():
            return Create(root)

        Button(text="Log In ", font=20, width=10, height=1, cursor='hand2', command=submit).place(x=630, y=400)
        Button(text="Create", font=20, width=10, height=1, cursor='hand2', command=create1).place(x=130, y=400)


def daro(root):
    Form(root)

def create1():
    root=Tk()
    daro(root)

    root.mainloop()


if __name__=='__main__':
    create1()

