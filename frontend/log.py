from create import *
from homepage import *
from tkinter import *
import mysql.connector as sa
from PIL import ImageTk, Image, ImageDraw


class form:
    # aasign tk to root

    def __init__(self, root):
        self.root = root
        self.root.title('Login')  # add title
        self.root.geometry('1000x550')  # geometry

        self.root.configure(bg="#ffffff")  # color of background
        self.root.resizable(0, 0)  # don`t  change size

        # label title

        self.frame1 = Frame(self.root)
        self.frame1.config(bg='slate blue')
        self.frame1.place(x=0, y=0, width=500, height=1000)

        self.frame2 = Frame(self.root)
        self.frame2.config(bg='#ffffff')
        self.frame2.place(x=400, y=0, width=600, height=1000)

        Label(self.frame1, text="Create Account", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=90, y=50)
        Label(self.frame1, text="And ", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=150, y=80)
        Label(self.frame1, text=" Explore", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=125, y=110)
        Label(self.frame1, text="E-AT APP", bg='slate blue', fg='#ffffff', font=('Times', 30)).place(x=90, y=140)

        Label(self.frame2, text='E-AT APP', font=('Times', 40), bg='#ffffff').place(x=170, y=30)
        Label(self.frame2 ,text='Sign In', font=('Times', 20), bg='#ffffff').place(x=250, y=140)

        # text in form
        Label(self.frame2, text='Email', font=23, bg='#ffffff').place(x=170, y=200)
        Label(self.frame2, text="Password", font=23, bg='#ffffff').place(x=170, y=280)

        # assign string  variable to tkinter
        nameValue = StringVar()
        passValue = StringVar()

        # Input
        nameEntry = Entry(self.frame2, textvariable=nameValue, width=32, bd=0, font=20).place(x=170, y=225, height=30)
        Canvas(self.frame2, width=250, height=2.0, bg='#000000').place(x=170, y=250)
        passEntry = Entry(self.frame2, textvariable=passValue, width=32, bd=0, font=20, show='*').place(x=170, y=305, height=30)
        Canvas(self.frame2, width=250, height=2.0, bg='#000000').place(x=170, y=330)

        # assign int variable to tkinter
        checkValue = IntVar()
        # checkbox
        checkbtn = Checkbutton(self.frame2, text='remember me ?', variable=checkValue, cursor='hand2', bg="#ffffff").place(x=170,y=350)  #
        # label in forgot
        Label(self.frame2, text='Forgot Password', font=('Times', 10, "underline"), fg='blue', bg='#ffffff',
              cursor='hand2').place(x=400, y=480)

        def submit():
            name = nameValue.get()
            pas = passValue.get()

            # connect to mysql
            if (name and pas):
                conn = sa.connect(host='localhost', user='root', password='', database='Recon')
                cur = conn.cursor()  # assign cursor
                lol = "select name from Admin where Name =%s and Password=%s"
                cur.execute(lol, [(name), (pas)])
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
            return create1()

        Button(self.frame2, text="Log In ", font=20, width=10, height=1, cursor='hand2', command=submit).place(x=250, y=400)
        Button(self.frame1, text="Create", font=20, width=10, height=1, cursor='hand2', command=create2).place(x=130, y=400)

    # close tkinter


def login():
    root = Tk()
    form(root)

    img4 = Image.open(r'C:\Users\D35KT0P\Downloads\user.png')
    resize = img4.resize((30, 30), Image.LANCZOS)
    pic4 = ImageTk.PhotoImage(resize)
    Label(root, image=pic4, bg='#ffffff').place(x=530, y=220)

    img5 = Image.open(r'C:\Users\D35KT0P\Downloads\padlock.png')
    resize = img5.resize((30, 30), Image.LANCZOS)
    pic5 = ImageTk.PhotoImage(resize)
    Label(root, image=pic5, bg='#ffffff').place(x=530, y=300)

    root.mainloop()


if __name__ == '__main__':
    login()



