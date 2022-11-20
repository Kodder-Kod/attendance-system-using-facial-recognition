from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import time
from datetime import *


class Home:
    def __init__(self,root):
        self.root=root
        self.root.title('Student Attendance')
        self.root.geometry('1200x600')
        self.root.config (bg='grey90')

        icon = PhotoImage(file=r'C:\Users\D35KT0P\Desktop\kok.png')

        root.iconphoto(True, icon)
        but1=Button(root ,text='Log Out', fg="#ffffff",bd=0 ,bg='dark slate blue', cursor='hand2', width=10, height=1).place(x=1250,y=50)

        pop=Frame(root, bg='slate blue').place(x=0, y=0, height=1000, width=186)

        head=Label(root,text=" Dashboard",font=50 ,bg='grey90').place(x=230,y=100)

        frame1=Frame(root, bg='red', cursor='hand2').place(height= 200, width=330 ,x=1000, y=495)
        frame2=Frame(root,bg='green',cursor='hand2').place(height=200, width=330,x=240, y=495)
        frame3=Frame(root,bg='blue',).place(height=200,width=330 ,x=620, y=495)
        frame4 = Frame(self.root,bg='pink' ,cursor='hand2').place(height=330, width=530,x=240, y=130)
        frame5 = Frame(self.root, bg='#ffffff').place(height=330, width=530, x=240, y=130)

        def show(frame):
            print(frame)

        btn=Label(frame4,text='frame 4' ,font=20).place(x=250,y=150)
        nyh=Label(frame5,text="frame 5",font=20).place(x=250,y=170)

        Button(pop, text='DashBoard', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0, font=15, width=20, height=4).place(x=0, y=200)
        Button(pop, text='Manage', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0, font=15, width=20, height=4,command=show(frame4)).place(x=0, y=280)
        Button(pop, text='Help', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0, font=15, width=20, height=4).place(x=0, y=360)
        Button(pop, text='Settings', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0, font=15, width=20, height=4).place(x=0, y=435)



    def show_time(self,das):
         form="%H:%M:%S"
         self.time = datetime.strftime(form)
         year="%y/%m/%d"
         self.date = datetime.strftime(year)
         set_text = f"{self.time}\n {self.date}"
         das.configure(text=set_text, font=('', 13, 'bold'), bd=0, bg="white", fg="black")



def board():
    root=Tk()
    Home(root)

    img = Image.open(r'C:\Users\D35KT0P\Downloads\man.png')
    resize = img.resize((150, 150), Image.LANCZOS)
    pic = ImageTk.PhotoImage(resize)
    Label(root, image=pic, bg='slate blue').place(x=15, y=25)

    img1 = Image.open(r'C:\Users\D35KT0P\Downloads\home.png')
    resize = img1.resize((20, 20), Image.LANCZOS)
    pic1 = ImageTk.PhotoImage(resize)
    Label(root, image=pic1, bg='slate blue' ).place(x=25, y=227)

    img2 = Image.open(r'C:\Users\D35KT0P\Downloads\add-contact.png')
    resize = img2.resize((30, 30), Image.LANCZOS)
    pic2 = ImageTk.PhotoImage(resize)
    Label(root, image=pic2, bg='slate blue' ).place(x=25, y=303)

    img3 = Image.open(r'C:\Users\D35KT0P\Downloads\interrogation-free-icon-font.png')
    resize = img3.resize((20, 20), Image.LANCZOS)
    pic3 = ImageTk.PhotoImage(resize)
    Label(root, image=pic3, bg='slate blue').place(x=47, y=388)

    img4 = Image.open(r'C:\Users\D35KT0P\Downloads\settings-free-icon-font.png')
    resize = img4.resize((20, 20), Image.LANCZOS)
    pic4 = ImageTk.PhotoImage(resize)
    Label(root, image=pic4, bg='slate blue').place(x=35, y=463)


    root.mainloop()

if __name__=='__main__':
     board()
