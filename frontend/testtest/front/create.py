from kok import *
from homepage import *
from tkinter import *
from tkinter import messagebox
import mysql.connector as sa
from PIL import ImageTk, Image
import re

class create():
    def __init__(self,root):
        self.root = root
        self.root.title('Create Acc')
        self.root.geometry('1200x600')
        self.root.configure(bg="#ffffff")

        self.frame5 = Frame(self.root)
        self.frame5.config(bg='#ffffff')
        self.frame5.place(x=0, y=0, width=1000, height=1000)

        self.frame4 = Frame(self.root)
        self.frame4.config( bg='slate blue')
        self.frame4.place(x=750, y=0, width=1000, height=1000)

        Label(self.frame4, text="Already have An ", font=("Times", 25), bg='slate blue', fg='white').place(x=100, y=70)
        Label(self.frame4, text="Account", font=("Times", 25), bg='slate blue',fg='white').place(x=150, y=105)
        Label(self.frame4, text="Sign In", font=("Times", 30), bg='slate blue',fg='white').place(x=150, y=140)

        def login1():
            return login()

        Button(self.frame4, text="Sign In ", font=20, width=11, height=1,command=login1).place(x=170, y=400)

        Label(self.frame5,text="Create Account", font=("Times",25),bg= 'white').place(x=250,y=30)

        Label(self.frame5,text='Name',font =23 ,bg='white').place(x=195 ,y= 100)
        Label(self.frame5,text="Email",font =23 ,bg= 'white').place(x=195 ,y= 170)
        Label(self.frame5,text="Phone ",font =23 ,bg= 'white').place(x=195 ,y= 240)
        Label(self.frame5,text="Password ",font =23 ,bg= 'white').place(x=195 ,y= 310)
        Label(self.frame5,text="Confirm Password",font =23 ,bg= 'white').place(x=195, y=380)

        nameValue = StringVar()
        emailValue = StringVar()
        phoneValue = StringVar()
        passValue = StringVar()
        conpassValue = StringVar()

        nameEntry= Entry(self.frame5,textvariable =nameValue, width=30 ,bd =0,font=20 ).place(x=200,y=125)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=145)

        emailEntry= Entry(self.frame5,textvariable =emailValue, width=30 ,bd =0 ,font=20).place(x=200,y=195)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=215)

        phoneEntry= Entry(self.frame5,textvariable =phoneValue, width=30 ,bd =0 ,font=20).place(x=200,y=265)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=285)

        passEntry= Entry(self.frame5,textvariable =passValue, width=30 ,bd =0 ,font=20 ,show='*').place(x=200,y=335)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=355)

        conpassEntry= Entry(self.frame5,textvariable =conpassValue, width=30 ,bd =0 ,font=20, show='*').place(x=200,y=405)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=425)

        def submit():
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

                if pas != con:
                    return messagebox.showerror('password is not the same', parent=root)

                if phoneform:
                    return messagebox.showerror('only numbers', parent=root)

                if not mailform:
                    return messagebox.showerror('email formart', parent=root)

                if not f and not e or not d:
                    return messagebox.showerror('password formart', parent=root)


                try:
                    conn = sa.connect(host="localhost", user="root", password="", database="Recon")
                    cur = conn.cursor()  # assign cursor
                    sql = "CREATE TABLE IF NOT EXISTS admin( name varchar(100) not null,email  varchar(100) not null,phone int(11) not null,password  varchar(40) not null ) "
                    cur.execute(sql)  # execute the query
                    pin = "INSERT INTO  Admin (Name,Email,Phone,Password) Values(%s,%s,%s,%s)"
                    nip = ((name), (email), (phone), (pas))
                    print('lol')
                    cur.execute(pin, nip)
                    conn.commit()

                    board()

                    conn.close()
                except:
                    print('Can not connect to the Database')

            else:
                messagebox.showerror('All fields must be filled', parent=root)

        Button(self.frame5, text="register ", font=20, width=11, height=1, command=submit).place(x=270, y=450)

        self.pic()

    def pic(self):

        load001h = Image.open("user.png")
        resize001h = load001h.resize((25, 25), Image.LANCZOS)
        render001h = ImageTk.PhotoImage(resize001h)
        img001h = Label(self.frame5, image=render001h, bg='#ffffff')
        img001h.image = render001h
        img001h.place(x=170, y=120)

        load001p = Image.open("padlock.png")
        resize001p = load001p.resize((25, 25), Image.LANCZOS)
        render001p = ImageTk.PhotoImage(resize001p)
        img001p = Label(self.frame5, image=render001p, bg='#ffffff')
        img001p.image = render001p
        img001p.place(x=170, y=190)

        load001p = Image.open("padlock.png")
        resize001p = load001p.resize((25, 25), Image.LANCZOS)
        render001p = ImageTk.PhotoImage(resize001p)
        img001p = Label(self.frame5, image=render001p, bg='#ffffff')
        img001p.image = render001p
        img001p.place(x=170, y=260)

        load001p = Image.open("padlock.png")
        resize001p = load001p.resize((25, 25), Image.LANCZOS)
        render001p = ImageTk.PhotoImage(resize001p)
        img001p = Label(self.frame5, image=render001p, bg='#ffffff')
        img001p.image = render001p
        img001p.place(x=170, y=330)

        load001p = Image.open("padlock.png")
        resize001p = load001p.resize((25, 25), Image.LANCZOS)
        render001p = ImageTk.PhotoImage(resize001p)
        img001p = Label(self.frame5, image=render001p, bg='#ffffff')
        img001p.image = render001p
        img001p.place(x=170, y=400)

        load001p = Image.open("padlock.png")
        resize001p = load001p.resize((200, 200), Image.LANCZOS)
        render001p = ImageTk.PhotoImage(resize001p)
        img001p = Label(self.frame4, image=render001p, bg='#ffffff')
        img001p.image = render001p
        img001p.place(x=120, y=190)


def create1():
    root1=Tk()
    create(root1)
    root1.mainloop()

if __name__=='__main__':
    create1()

