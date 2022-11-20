from create import *
from homepage import *
from tkinter import *
import mysql.connector as sa
from PIL import ImageTk, Image, ImageDraw


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

        Label(frame1, text="Create Account", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=90, y=50)
        Label(frame1, text="And ", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=150, y=80)
        Label(frame1, text=" Explore", bg='slate blue', fg='#ffffff', font=('Times', 20)).place(x=125, y=110)
        Label(frame1, text="E-AT APP", bg='slate blue', fg='#ffffff', font=('Times', 30)).place(x=90, y=140)

        Label(frame1,text='E-AT APP',font=('Times',40),bg='#ffffff').place(x=560,y=30)
        Label(root, text='Sign In', font=('Times', 20), bg='#ffffff').place(x=640, y=140)

        #text in form
        Label(frame2,text='Email',font =23 ,bg= '#ffffff').place(x=550,y= 200)
        Label(frame2,text="Password",font =23 ,bg= '#ffffff').place(x=550 ,y= 280)

        #assign string  variable to tkinter
        nameValue=StringVar()
        passValue=StringVar()
        img4 = Image.open(r'C:\Users\D35KT0P\Downloads\user.png')
        resize = img4.resize((30, 30), Image.LANCZOS)
        pic4 = ImageTk.PhotoImage(resize)
        Label(frame2, image=pic4, bg='#ffffff').place(x=510, y=220)

        img5 = Image.open(r'C:\Users\D35KT0P\Downloads\padlock.png')
        resize = img5.resize((30, 30), Image.LANCZOS)
        pic5 = ImageTk.PhotoImage(resize)
        Label(frame2, image=pic5, bg='#ffffff').place(x=510, y=300)

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
            return create()

        Button(text="Log In ", font=20, width=10, height=1, cursor='hand2', command=submit).place(x=630, y=400)
        Button(text="Create", font=20, width=10, height=1, cursor='hand2', command=create1).place(x=130, y=400)

    #close tkinter

def login():
    root = Tk()
    Form(root)

    root.mainloop()


if __name__=='__main__':
    login()




