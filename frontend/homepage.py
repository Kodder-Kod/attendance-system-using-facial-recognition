from kok import *
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import time
from datetime import *

class Home:
    def __init__(self, root):
        self.root = root
        self.root.title('Student Attendance')
        self.root.geometry('1200x600')
        self.root.config(bg='grey90')


        def show(fram):
            return fram.tkraise(aboveThis=None)


#####################################################################################
#################################################################################
#################################################################################
        self.pop = Frame(self.root)
        self.pop.config(bg='slate blue')
        self.pop.place(x=0, y=0, height=1000, width=186)
###################################################################################
##################################################################################
        home = Frame(self.root)
        home.config(bg='grey90')
        home.place(height=1000, width=1200, x=185, y=0)

        s=Frame(home)
        s.config( bg="#ffffff", cursor='hand2')
        s.place(x=10, y=50, height=100, width=200)
        Label(s,text='Students',font=('Times',12),bg='#ffffff').place(x=5,y=70)
        Label(s, text='Students', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        t=Frame(home)
        t.config( bg="#ffffff", cursor='hand2')
        t.place(x=220, y=50, height=100, width=200)
        Label(t, text='Lectures', font=('Times', 12),bg='#ffffff').place(x=5, y=70)
        Label(t, text='Lectures', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        u=Frame(home)
        u.config(bg="#ffffff", cursor='hand2')
        u.place(x=430, y=50, height=100, width=200)
        Label(u, text='Courses', font=('Times', 12),bg='#ffffff').place(x=5, y=70)
        Label(u, text='Courses', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        c=Frame(home)
        c.config(bg="#ffffff", cursor='hand2')
        c.place(x=640, y=50, height=100, width=200)
        Label(c, text='Units', font=('Times', 12),bg='#ffffff').place(x=5, y=70)
        Label(c, text='Units', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        recent=Frame(home)
        recent.config(bg='#ffffff')
        recent.place(x=850, y=0, height=1000, width=200)
        Label(recent, text="Recent Classes",bg='#ffffff',font=('Times',13,'italic')).place(x=20, y=20)


        Button(home,text='Start Class',height=6, width=30).place(x=20 ,y=220)


        subject=StringVar()
        Label(home,text='Subject',bg='grey90',font=('Times',15)).place(x=250,y=220)
        Entry(home,textvariable=subject,bd=0,font=("Times",14),width=20).place(x=250,y=250,height=30)
        Canvas(home, width=182, height=2.0, bg='#000000').place(x=249,y=273)

        weeklyframe=Frame(home)
        weeklyframe.config(bg='#ffffff' )
        weeklyframe.place(x=450,y=220,height=300,width=350)
        Label(weeklyframe,text='Random weekly reports',bg='#ffffff').place(x=10,y=10)
        Frame(home, bg='#ffffff').place()

        unit=StringVar()
        tarehe=IntVar()
        student=StringVar()
        Label(home, text='Unit', bg='grey90', font=('Times', 13)).place(x=20, y=350)
        Entry(home, textvariable=unit,font=('Times',14),width=20,bd=0 ).place(x=20,y=380,height=30)
        Canvas(home, width=180, height=2.0, bg='#000000').place(x=20, y=403)
        Label(home, text='Date', bg='grey90', font=('Times', 13)).place(x=20, y=420)
        Entry(home, textvariable=tarehe,font=('Times',14),width=20,bd=0 ).place(x=20,y=450,height=30)
        Canvas(home, width=180, height=2.0, bg='#000000').place(x=20, y=473)
        Label(home, text='Student(Optional)', bg='grey90', font=('Times', 13)).place(x=20, y=490)
        Entry(home, textvariable=student,font=('Times',14),width=20,bd=0 ).place(x=20,y=520,height=30)
        Canvas(home, width=180, height=2.0, bg='#000000').place(x=20, y=543)

        Button(home, text='View',height=1,width=15,font=('Times',12),command=lambda:show(view)).place(x=250,y=450)
        Button(home,text='Print',height=1,width=15,font=('Times',12)).place(x=250,y=515)

  ###########################################
        view=Frame(self.root)
        view.config(bg='grey90')
        view.place(x=195, y=200, height=390, width=830)

        Button(view, text='Back', height=1, width=10, font=('Times', 12),command=lambda:show(home)).place(x=0, y=0)

        day=Frame(view)
        day.config(bg='#ffffff')
        day.place(x=100,y=20,height=175,width=330)
        Label(day,text='Day',font=("Times",15,'italic'),bg='#ffffff').place(x=5,y=5)

        week=Frame(view)
        week.config(bg='#ffffff')
        week.place(x=100,y=200,height=175,width=330)
        Label(week, text='Month', font=("Times", 15, 'italic'),bg='#ffffff').place(x=5, y=5)

        month=Frame(view)
        month.config(bg='#ffffff')
        month.place(x=450,y=20,height=175,width=330)
        Label(month, text='Week', font=("Times", 15, 'italic'),bg='#ffffff').place(x=5, y=5)

        sheet=Frame(view)
        sheet.config(bg='#ffffff')
        sheet.place(x=450,y=200,height=175,width=330)
        Label(sheet, text='Spread Sheet', font=("Times", 15, 'italic'),bg='#ffffff').place(x=5, y=5)

       # fullsheet=Frame(view)
        #fullsheet.config(bg='#ffffff')
       # fullsheet.place(x=450,y=200,height=175,width=330)

###################################################################################
#########################################################################################
        manage = Frame(self.root)
        manage.config(bg='grey90')
        manage.place(height=1000, width=1200, x=185, y=0)

        s=Frame(manage)
        s.config( bg="#ffffff", cursor='hand2')
        s.place(x=10, y=50, height=100, width=200)
        Label(s,text='Students',font=('Times',12),bg='#ffffff').place(x=5,y=70)
        Label(s, text='Students', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        t=Frame(manage)
        t.config( bg="#ffffff", cursor='hand2')
        t.place(x=220, y=50, height=100, width=200)
        Label(t, text='Lectures', font=('Times', 12),bg='#ffffff').place(x=5, y=70)
        Label(t, text='Lectures', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        u=Frame(manage)
        u.config(bg="#ffffff", cursor='hand2')
        u.place(x=430, y=50, height=100, width=200)
        Label(u, text='Courses', font=('Times', 12),bg='#ffffff').place(x=5, y=70)
        Label(u, text='Courses', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        c=Frame(manage)
        c.config(bg="#ffffff", cursor='hand2')
        c.place(x=640, y=50, height=100, width=200)
        Label(c, text='Units', font=('Times', 12),bg='#ffffff').place(x=5, y=70)
        Label(c, text='Units', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        recent = Frame(manage)
        recent.config(bg="#ffffff")
        recent.place(x=850, y=0, height=1000, width=200)
        Label(recent, text="Recent Classes",bg='#ffffff',font=('Times',13,'italic')).place(x=20, y=20)

        managepro=Frame(manage)
        managepro.config(bg="grey90")
        managepro.place(x=0, y=200, height=390, width=840)


        Label(managepro,text='Choose One for Management',bg='grey90',font=('Times',25)).place(x=200,y=10)
        Button(managepro,text='Students', bg='#ffffff',font=('Times',10),height=7,width=30, cursor='hand2',command=lambda:show(edit1)).place(x=100,y=100)
        Button(managepro,text='Lectures', bg='#ffffff',font=('Times',10),height=7,width=30, cursor='hand2',command=lambda:show(edit2)).place(x=450,y=100)
        Button(managepro,text='Units', bg='#ffffff',font=('Times',10),height=7,width=30, cursor='hand2',command=lambda:show(edit3)).place(x=100,y=250)
        Button(managepro,text='Courses', bg='#ffffff',font=('Times',10),height=7,width=30, cursor='hand2',command=lambda:show(edit4)).place(x=450,y=250)

######################################################################################################################
        edit1 = Frame(self.root)
        edit1.config(bg="grey90")
        edit1.place(x=195, y=180, height=415, width=830)

        edit11 = Frame(edit1)
        edit11.config(bg="grey90")
        edit11.place(x=0,y=0,height=1000,width=400)
        Button(edit11, text='Back', height=1, width=10, font=('Times', 12), command=lambda: show(manage)).place(x=0, y=0)

        sname=StringVar()
        semail = StringVar()
        sregno = StringVar()
        sface = StringVar()
        scourse = StringVar()

        Label(edit1,text='Edit Student',bg='grey90',font=('Times',18)).place(x=300,y=20)

        Label(edit11, text='Name', font=('Times', 12), bg='grey90').place(x=25, y=50)
        Entry(edit11, textvariable=sname, font=('Times', 14), width=20, bd=0).place(x=40, y=80, height=30)
        Canvas(edit11, width=180, height=2.0, bg='#000000').place(x=38, y=103)
        Label(edit11, text='Email', font=('Times', 12), bg='grey90').place(x=25, y=110)
        Entry(edit11, textvariable=semail, font=('Times', 14), width=20, bd=0).place(x=40, y=140, height=30)
        Canvas(edit11, width=180, height=2.0, bg='#000000').place(x=40, y=163)
        Label(edit11, text='Reg No.', font=('Times', 12), bg='grey90').place(x=25, y=170)
        Entry(edit11, textvariable=sregno, font=('Times', 14), width=20, bd=0).place(x=40, y=200, height=30)
        Canvas(edit11, width=180, height=2.0, bg='#000000').place(x=40, y=223)
        Label(edit11, text='Add face or take a Picture', font=('Times', 12), bg='grey90').place(x=25, y=230)
        Entry(edit11, textvariable=sface, font=('Times', 14), width=20, bd=0).place(x=40, y=260, height=30)
        Canvas(edit11, width=180, height=2.0, bg='#000000').place(x=40, y=283)
        Label(edit11, text='Course', font=('Times', 12), bg='grey90').place(x=25, y=290)
        Entry(edit11, textvariable=scourse, font=('Times', 14), width=20, bd=0).place(x=40, y=320, height=30)
        Canvas(edit11, width=180, height=2.0, bg='#000000').place(x=40, y=343)



        Button(edit11,text='Add',width=10).place(x=20,y=370)
        Button(edit11, text='Update',width=10).place(x=110,y=370)
        Button(edit11, text='Delete',width=10).place(x=200,y=370)
        Button(edit11, text='Clear',width=10).place(x=290,y=370)

        edit101 = Frame(edit1)
        edit101.config(bg="#ffffff")
        edit101.place()

        Label(edit101,text='Search BY').place()
        Entry(edit101,textvariable='').place()

        Button(edit101, text='Search').place()
        Button(edit101, text='Show All').place()

        edit1010=Frame(edit1)
        edit1010.config(bg='#ffffff')
        edit1010.place()

        scroll_x = Scrollbar(edit1010, orient=HORIZONTAL)
        scroll_Y = Scrollbar(edit1010, orient=VERTICAL)

############################################ ###############
        edit2 = Frame(self.root)
        edit2.config(bg='grey90')
        edit2.place(x=195, y=180, height=415, width=830)

        edit22 = Frame(edit2)
        edit22.config(bg="grey90")
        edit22.place(x=0,y=0,height=1000,width=400)

        Label(edit2, text='Edit Lectures', bg='grey90', font=('Times', 18)).place(x=300, y=20)

        Button(edit22, text='Back', height=1, width=10, font=('Times', 12), command=lambda: show(manage)).place(x=0, y=0)

        lname=StringVar()
        lemail = StringVar()
        lregno = StringVar()
        lcourse = StringVar()

        Label(edit22, text='Name', font=('Times', 12), bg='grey90').place(x=25, y=50)
        Entry(edit22, textvariable=lname, font=('Times', 14), width=20, bd=0).place(x=40, y=80, height=30)
        Canvas(edit22, width=180, height=2.0, bg='#000000').place(x=38, y=103)
        Label(edit22, text='Email', font=('Times', 12), bg='grey90').place(x=25, y=110)
        Entry(edit22, textvariable=lemail, font=('Times', 14), width=20, bd=0).place(x=40, y=140, height=30)
        Canvas(edit22, width=180, height=2.0, bg='#000000').place(x=40, y=163)
        Label(edit22, text='Reg No.', font=('Times', 12), bg='grey90').place(x=25, y=170)
        Entry(edit22, textvariable=lregno, font=('Times', 14), width=20, bd=0).place(x=40, y=200, height=30)
        Canvas(edit22, width=180, height=2.0, bg='#000000').place(x=40, y=223)
        Label(edit22, text='Course', font=('Times', 12), bg='grey90').place(x=25, y=230)
        Entry(edit22, textvariable=lcourse, font=('Times', 14), width=20, bd=0).place(x=40, y=260, height=30)
        Canvas(edit22, width=180, height=2.0, bg='#000000').place(x=40, y=283)

        Button(edit22,text='Add',width=10).place(x=20,y=310)
        Button(edit22, text='Update',width=10).place(x=110,y=310)
        Button(edit22, text='Delete',width=10).place(x=200,y=310)
        Button(edit22, text='Clear',width=10).place(x=290,y=310)

        edit202 = Frame(edit2)
        edit202.config(bg="#ffffff")
        edit202.place()

        Label(edit202,text='Search BY').place()
        Entry(edit202,textvariable='').place()

        Button(edit202, text='Search').place()
        Button(edit202, text='Show All').place()

        edit2020=Frame(edit2)
        edit2020.config(bg='#ffffff')
        edit2020.place()

        scroll_x = Scrollbar(edit2020, orient=HORIZONTAL)
        scroll_Y = Scrollbar(edit2020, orient=VERTICAL)

        ########################################################
        edit3 = Frame(self.root)
        edit3.config(bg="grey90")
        edit3.place(x=195, y=200, height=390, width=830)

        edit33 = Frame(edit3)
        edit33.config(bg="grey90")
        edit33.place(x=0,y=0,height=1000,width=400)

        Label(edit33, text='Edit Units', bg='grey90', font=('Times', 18)).place(x=300, y=20)

        Button(edit33, text='Back', height=1, width=10, font=('Times', 12), command=lambda: show(manage)).place(x=0, y=0)

        ucode=StringVar()
        uname = StringVar()
        ulecture = StringVar()
        ucourse = StringVar()

        Label(edit33, text='Course code', font=('Times', 12), bg='grey90').place(x=25, y=50)
        Entry(edit33, textvariable=ucode, font=('Times', 14), width=20, bd=0).place(x=40, y=80, height=30)
        Canvas(edit33, width=180, height=2.0, bg='#000000').place(x=38, y=103)
        Label(edit33, text='Name', font=('Times', 12), bg='grey90').place(x=25, y=110)
        Entry(edit33, textvariable=uname, font=('Times', 14), width=20, bd=0).place(x=40, y=140, height=30)
        Canvas(edit33, width=180, height=2.0, bg='#000000').place(x=40, y=163)
        Label(edit33, text='Lecture', font=('Times', 12), bg='grey90').place(x=25, y=170)
        Entry(edit33, textvariable=ulecture, font=('Times', 14), width=20, bd=0).place(x=40, y=200, height=30)
        Canvas(edit33, width=180, height=2.0, bg='#000000').place(x=40, y=223)
        Label(edit33, text='Faculty', font=('Times', 12), bg='grey90').place(x=25, y=230)
        Entry(edit33, textvariable=ucourse, font=('Times', 14), width=20, bd=0).place(x=40, y=260, height=30)
        Canvas(edit33, width=180, height=2.0, bg='#000000').place(x=40, y=283)

        Button(edit33,text='Add',width=10).place(x=20,y=310)
        Button(edit33, text='Update',width=10).place(x=110,y=310)
        Button(edit33, text='Delete',width=10).place(x=200,y=310)
        Button(edit33, text='Clear',width=10).place(x=290,y=310)


        edit303 = Frame(edit3)
        edit303.config(bg="#ffffff")
        edit303.place()

        Label(edit303,text='Search BY').place()
        Entry(edit303,textvariable='').place()

        Button(edit303, text='Search').place()
        Button(edit303, text='Show All').place()

        edit3030=Frame(edit3)
        edit3030.config(bg='#ffffff')
        edit3030.place()

        scroll_x = Scrollbar(edit3030, orient=HORIZONTAL)
        scroll_Y = Scrollbar(edit3030, orient=VERTICAL)


        ########################################################
        edit4 = Frame(self.root)
        edit4.config(bg="grey90")
        edit4.place(x=195, y=200, height=390, width=830)



        edit44 = Frame(edit4)
        edit44.config(bg="grey90")
        edit44.place(x=0,y=0,height=1000,width=400)

        Label(edit44, text='Edit Units', bg='grey90', font=('Times', 18)).place(x=300, y=20)

        Button(edit44, text='Back', height=1, width=10, font=('Times', 12), command=lambda: show(manage)).place(x=0,
                                                                                                                y=0)
        cname=StringVar()

        Label(edit44, text='Name', font=('Times', 12), bg='grey90').place(x=25, y=110)
        Entry(edit44, textvariable=cname, font=('Times', 14), width=20, bd=0).place(x=40, y=140, height=30)
        Canvas(edit44, width=180, height=2.0, bg='#000000').place(x=40, y=163)

        Button(edit44, text='Add', width=10).place(x=20, y=250)
        Button(edit44, text='Update', width=10).place(x=110, y=250)
        Button(edit44, text='Delete', width=10).place(x=200, y=250)
        Button(edit44, text='Clear', width=10).place(x=290, y=250)

        edit404 = Frame(edit4)
        edit404.config(bg="#ffffff")
        edit404.place()

        Label(edit404,text='Search BY').place()
        Entry(edit404,textvariable='').place()

        Button(edit404, text='Search').place()
        Button(edit404, text='Show All').place()

        edit4040=Frame(edit1)
        edit4040.config(bg='#ffffff')
        edit4040.place()

        scroll_x = Scrollbar(edit4040, orient=HORIZONTAL)
        scroll_Y = Scrollbar(edit4040, orient=VERTICAL)

        ###########################################################

        ###########################################################


###########################################################################################################################################################








##############################################################################################################################################
        help = Frame(self.root)
        help.config(bg='grey90', cursor='hand2')
        help.place(height=1000, width=1200, x=185, y=0)

        Label(help,text='').place()
############################################################################################################################################################################################
        settings = Frame(self.root)
        settings.config(bg='grey90', cursor='hand2')
        settings.place(height=1000, width=1200, x=185, y=0)

        s = Frame(settings)
        s.config(bg="#ffffff", cursor='hand2')
        s.place(x=10, y=50, height=100, width=200)
        Label(s, text='Students', font=('Times', 12), bg='#ffffff').place(x=5, y=70)
        Label(s, text='Students', font=('Times', 12, 'italic'), bg='#ffffff').place(x=140, y=40)

        t = Frame(settings)
        t.config(bg="#ffffff", cursor='hand2')
        t.place(x=220, y=50, height=100, width=200)
        Label(t, text='Lectures', font=('Times', 12), bg='#ffffff').place(x=5, y=70)
        Label(t, text='Lectures', font=('Times', 12, 'italic'), bg='#ffffff').place(x=140, y=40)

        u = Frame(settings)
        u.config(bg="#ffffff", cursor='hand2')
        u.place(x=430, y=50, height=100, width=200)
        Label(u, text='Courses', font=('Times', 12), bg='#ffffff').place(x=5, y=70)
        Label(u, text='Courses', font=('Times', 12, 'italic'), bg='#ffffff').place(x=140, y=40)

        c = Frame(settings)
        c.config(bg="#ffffff", cursor='hand2')
        c.place(x=640, y=50, height=100, width=200)
        Label(c, text='Units', font=('Times', 12), bg='#ffffff').place(x=5, y=70)
        Label(c, text='Units', font=('Times', 12, 'italic'), bg='#ffffff').place(x=140, y=40)


        Label(settings,text='Change Email').place()
        Label(settings, text='Change password').place()
        Label(settings, text='Change profile pic').place()


        ########################################################################################################################################################################################################################################



#############################################################################################################################################################################################################################

        show(home)


        Button(self.pop, activebackground='grey90', text='DashBoard', bg='slate blue', fg='#ffffff', cursor='hand2',
               bd=0, font=('Times', 13), width=20, height=3, command=lambda: show(home)).place(x=0, y=200)
        Button(self.pop, activebackground='grey90', text='Manage', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0,
               font=('Times', 13), width=20, height=3, command=lambda: show(manage)).place(x=0, y=269)
        Button(self.pop, activebackground='grey90', text='Help', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0,
               font=('Times', 13), width=20, height=3, command=lambda: show(help)).place(x=0, y=337)
        Button(self.pop, activebackground='grey90', text='Settings', bg='slate blue', fg='#ffffff', cursor='hand2',
               bd=0, font=('Times', 13), width=20, height=3, command=lambda: show(settings)).place(x=0, y=404)
        Button(self.pop, activebackground='grey90', text='Log Out', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0,
               font=('Times', 13),width=20, height=3,command=lambda :login()).place(x=0, y=470)
################################################################################################################################################################################################################################################
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
    Label(root, image=pic1, bg='slate blue' ).place(x=25, y=220)

    img2 = Image.open(r'C:\Users\D35KT0P\Downloads\add-contact.png')
    resize = img2.resize((30, 30), Image.LANCZOS)
    pic2 = ImageTk.PhotoImage(resize)
    Label(root, image=pic2, bg='slate blue' ).place(x=25, y=285)

    img3 = Image.open(r'C:\Users\D35KT0P\Downloads\interrogation-free-icon-font.png')
    resize = img3.resize((20, 20), Image.LANCZOS)
    pic3 = ImageTk.PhotoImage(resize)
    Label(root, image=pic3, bg='slate blue' ).place(x=45, y=358)


    img4 = Image.open(r'C:\Users\D35KT0P\Downloads\settings-free-icon-font.png')
    resize = img4.resize((20, 20), Image.LANCZOS)
    pic4 = ImageTk.PhotoImage(resize)
    Label(root, image=pic4, bg='slate blue').place(x=35, y=425)

    root.mainloop()

if __name__=='__main__':
     board()
