from create import *
from homepage import *
from tkinter import *
import mysql.connector as sa
from PIL import ImageTk, Image, ImageDraw


class form:
    # asign tk to root

    def __init__(self, root):
        self.root = root
        self.root.title('Login')  # add title
        self.root.geometry('1200x600')  # geometry

        self.root.configure(bg="#ffffff")  # color of background
        self.root.resizable(0, 0)  # don`t  change size



        '''FRAME FUNCTION''' #############################################################################################################3

        def show(fram):
            return fram.tkraise(aboveThis=None)


        '''LOG IN PAGE''' #######################################################################################################################
        self.frame0 = Frame(self.root)
        self.frame0.config(bg='#ffffff')
        self.frame0.place(x=0, y=0, width=1200, height=1000)

        self.frame1 = Frame(self.frame0)
        self.frame1.config(bg='slate blue')
        self.frame1.place(x=0, y=0, width=500, height=1000)

        self.frame2 = Frame(self.frame0)
        self.frame2.config(bg='#ffffff')
        self.frame2.place(x=400, y=0, width=600, height=1000)

        '''RIGHT SIDE''' ##########################################################################################################

        Label(self.frame1, text="Create Account", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=90, y=50)
        Label(self.frame1, text="And ", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=150, y=80)
        Label(self.frame1, text=" Explore", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=125, y=110)
        Label(self.frame1, text="E-AT APP", bg='slate blue', fg='#ffffff', font=('Times', 30)).place(x=90, y=140)

        Label(self.frame2, text='E-AT APP', font=('Times', 40), bg='#ffffff').place(x=250, y=30)
        Label(self.frame2 ,text='Sign In', font=('Times', 20), bg='#ffffff').place(x=330, y=140)

        # text in form
        Label(self.frame2, text='Email', font=23, bg='#ffffff').place(x=250, y=200)
        Label(self.frame2, text="Password", font=23, bg='#ffffff').place(x=250, y=280)

        # assign string  variable to tkinter
        nameValue1 = StringVar()
        passValue1 = StringVar()

        # Input
        nameEntry = Entry(self.frame2, textvariable=nameValue1, width=32, bd=0, font=20).place(x=250, y=225, height=30)
        Canvas(self.frame2, width=250, height=2.0, bg='#000000').place(x=250, y=250)
        passEntry = Entry(self.frame2, textvariable=passValue1, width=32, bd=0, font=20, show='*').place(x=250, y=305, height=30)
        Canvas(self.frame2, width=250, height=2.0, bg='#000000').place(x=250, y=330)

        # assign int variable to tkinter
        checkValue = IntVar()
        # checkbox
        checkbtn = Checkbutton(self.frame2, text='remember me ?', variable=checkValue, cursor='hand2', bg="#ffffff").place(x=250,y=350)  #
        # label in forgot
        Label(self.frame2, text='Forgot Password', font=('Times', 10, "underline"), fg='blue', bg='#ffffff',
              cursor='hand2').place(x=480, y=480)

        def submit():
            name1 = nameValue1.get()

            pas1 = passValue1.get()

            # connect to mysql
            if (name1 and pas1):
                conn = sa.connect(host='localhost', user='root', password='', database='recon')
                cur = conn.cursor()  # assign cursor
                lol = "select email from Admin where email =%s and Password=%s"
                cur.execute(lol, [(name1), (pas1)])
                result = cur.fetchall()

                if result:

                    board()

                else:
                    messagebox.showerror('Username or Password  are invaild', parent=root)
                    conn.close()
            else:
                messagebox.showerror("All Fields must be Filled", parent=root)

        # button of sign in
        def create2():
            return show(self.frame3)

        Button(self.frame2, text="Log In ", font=20, width=10, height=1, cursor='hand2', command=submit).place(x=330, y=400)
        Button(self.frame1, text="Create", font=20, width=10, height=1, cursor='hand2', command=create2).place(x=130, y=400)






        '''CREATE PAGE''' ###########################################################################################################
        self.frame3 = Frame(self.root)
        self.frame3.config(bg='#ffffff')
        self.frame3.place(x=0, y=0, width=1200, height=1000)

        self.frame5 = Frame(self.frame3)
        self.frame5.config(bg='#ffffff')
        self.frame5.place(x=0, y=0, width=1000, height=1000)

        self.frame4 = Frame(self.frame3)
        self.frame4.config(bg='slate blue')
        self.frame4.place(x=750, y=0, width=1000, height=1000)

        Label(self.frame4, text="Already have An ", font=("Times", 25), bg='slate blue', fg='white').place(x=100, y=70)
        Label(self.frame4, text="Account", font=("Times", 25), bg='slate blue', fg='white').place(x=150, y=105)
        Label(self.frame4, text="Sign In", font=("Times", 30), bg='slate blue', fg='white').place(x=150, y=140)

        def login1():
            return show(self.frame0)

        Button(self.frame4, text="Sign In ", font=20, width=11, height=1, command=login1).place(x=170, y=400)

        Label(self.frame5, text="Create Account", font=("Times", 25), bg='white').place(x=250, y=30)

        Label(self.frame5, text='Name', font=23, bg='white').place(x=195, y=100)
        Label(self.frame5, text="Email", font=23, bg='white').place(x=195, y=170)
        Label(self.frame5, text="Phone ", font=23, bg='white').place(x=195, y=240)
        Label(self.frame5, text="Password ", font=23, bg='white').place(x=195, y=310)
        Label(self.frame5, text="Confirm Password", font=23, bg='white').place(x=195, y=380)

        nameValue = StringVar()
        emailValue = StringVar()
        phoneValue = StringVar()
        passValue = StringVar()
        conpassValue = StringVar()

        nameEntry = Entry(self.frame5, textvariable=nameValue, width=30, bd=0, font=20).place(x=200, y=125)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=145)

        emailEntry = Entry(self.frame5, textvariable=emailValue, width=30, bd=0, font=20).place(x=200, y=195)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=215)

        phoneEntry = Entry(self.frame5, textvariable=phoneValue, width=30, bd=0, font=20).place(x=200, y=265)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=285)

        passEntry = Entry(self.frame5, textvariable=passValue, width=30, bd=0, font=20, show='*').place(x=200, y=335)
        Canvas(self.frame5, width=250, height=2.0, bg='#000000').place(x=200, y=355)

        conpassEntry = Entry(self.frame5, textvariable=conpassValue, width=30, bd=0, font=20, show='*').place(x=200,
                                                                                                              y=405)
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


        show(self.frame0)
        self.pic()


    '''PIC FOR APP''' #######################################################################################################################################

    def pic(self):

        load001h = Image.open("user.png")
        resize001h = load001h.resize((25, 25), Image.LANCZOS)
        render001h = ImageTk.PhotoImage(resize001h)
        img001h = Label(self.frame2, image=render001h, bg='#ffffff')
        img001h.image = render001h
        img001h.place(x=220, y=225)


        load001p = Image.open("padlock.png")
        resize001p = load001p.resize((25, 25), Image.LANCZOS)
        render001p= ImageTk.PhotoImage(resize001p)
        img001p = Label(self.frame2, image=render001p, bg='#ffffff')
        img001p.image = render001p
        img001p.place(x=220, y=305)

        load001p = Image.open("padlock.png")
        resize001p = load001p.resize((200, 200), Image.LANCZOS)
        render001p = ImageTk.PhotoImage(resize001p)
        img001p = Label(self.frame1, image=render001p, bg='#ffffff')
        img001p.image = render001p
        img001p.place(x=80, y=190)


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





def login():
    root = Tk()

    form(root)
    root.mainloop()


if __name__ == '__main__':
    login()



