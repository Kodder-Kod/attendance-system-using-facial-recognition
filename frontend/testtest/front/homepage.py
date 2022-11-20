from kok import *
from testclass import *
from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter.ttk import Treeview
from tkinter import messagebox
import mysql.connector as sa
import re
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

        ''' DASHBOARD''' ###################################################################################################################################

        self.pop = Frame(self.root)
        self.pop.config(bg='slate blue')
        self.pop.place(x=0, y=0, height=1000, width=186)

        '''HOME PAGE''' ##############################################################################################################################################

        self.home = Frame(self.root)
        self.home.config(bg='grey90')
        self.home.place(height=1000, width=1200, x=185, y=0)

        '''OVERALL UPPER DETAILS''' ##################################################################################################################################

        self.s=Frame(self.home)
        self.s.config( bg="#ffffff", cursor='hand2')
        self.s.place(x=10, y=50, height=100, width=200)
        Label(self.s,text='Students',font=('Times',12),bg='#ffffff').place(x=15,y=70)
        Label(self.s, text='Students', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        self.t=Frame(self.home)
        self.t.config( bg="#ffffff", cursor='hand2')
        self.t.place(x=220, y=50, height=100, width=200)
        Label(self.t, text='Lectures', font=('Times', 12),bg='#ffffff').place(x=15, y=70)
        Label(self.t, text='Lectures', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)
        Label(self.t, text='', font=('Times', 12, 'italic'), bg='#ffffff').place(x=80, y=40)

        self.u=Frame(self.home)
        self.u.config(bg="#ffffff", cursor='hand2')
        self.u.place(x=430, y=50, height=100, width=200)
        Label(self.u, text='Units', font=('Times', 12),bg='#ffffff').place(x=15, y=70)
        Label(self.u, text='Units', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        self.c=Frame(self.home)
        self.c.config(bg="#ffffff", cursor='hand2')
        self.c.place(x=640, y=50, height=100, width=200)
        Label(self.c, text='Courses', font=('Times', 12),bg='#ffffff').place(x=15, y=70)
        Label(self.c, text='Courses', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        '''RECENT CLASSES''' ##################################################################################################################################

        recent=Frame(self.home)
        recent.config(bg='#ffffff')
        recent.place(x=850, y=0, height=1000, width=200)
        Label(recent, text="Recent Classes",bg='#ffffff',font=('Times',13,'italic','underline')).place(x=20, y=20)

        '''START BUTTON''' #####################################################################################################################################

        load = Image.open("man.png")
        resize = load.resize((50, 50), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(self.home, image=render, cursor='hand2', text='Start Class',compound=TOP, height=100, width=210, font=('Times', 12),
                     command=lambda: face())
        img.image = render
        img.place(x=20, y=220)

        subject=StringVar()
        Label(self.home,text='Subject',bg='grey90',font=('Times',15)).place(x=250,y=220)
        Entry(self.home,textvariable=subject,bd=0,font=("Times",14),width=20).place(x=250,y=250,height=30)
        Canvas(self.home, width=182, height=2.0, bg='#000000').place(x=249,y=273)

        weeklyframe=Frame(self.home)
        weeklyframe.config(bg='#ffffff' )
        weeklyframe.place(x=450,y=220,height=300,width=350)
        Label(weeklyframe,text='Random weekly reports',bg='#ffffff').place(x=10,y=10)
        Frame(self.home, bg='#ffffff').place()

        '''SELECT THE PREFERED UNIT''' ###########################################################################################################################

        unit=StringVar()
        tarehe=IntVar()
        student=StringVar()

        Label(self.home, text='Unit', bg='grey90', font=('Times', 13)).place(x=20, y=350)
        Entry(self.home, textvariable=unit,font=('Times',14),width=20,bd=0 ).place(x=20,y=380,height=30)
        Canvas(self.home, width=180, height=2.0, bg='#000000').place(x=20, y=403)
        Label(self.home, text='Date', bg='grey90', font=('Times', 13)).place(x=20, y=420)
        Entry(self.home, textvariable=tarehe,font=('Times',14),width=20,bd=0 ).place(x=20,y=450,height=30)
        Canvas(self.home, width=180, height=2.0, bg='#000000').place(x=20, y=473)
        Label(self.home, text='Student(Optional)', bg='grey90', font=('Times', 13)).place(x=20, y=490)
        Entry(self.home, textvariable=student,font=('Times',14),width=20,bd=0 ).place(x=20,y=520,height=30)
        Canvas(self.home, width=180, height=2.0, bg='#000000').place(x=20, y=543)

        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(self.home, image=render, cursor='hand2', text='View',compound=RIGHT, height=25, width=140, font=('Times', 12),
                     command=lambda: show(view))
        img.image = render
        img.place(x=250, y=450)

        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(self.home, image=render, cursor='hand2', text='Download',compound=RIGHT, height=25, width=140, font=('Times', 12),
                     command=lambda: show(view))
        img.image = render
        img.place(x=250, y=515)

        ''' VIEW THE SELECTED DETAILS''' ##############################################################################################################################

        view=Frame(self.root)
        view.config(bg='grey90')
        view.place(x=195, y=200, height=390, width=830)

        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(view, image=render, cursor='hand2', text='Back',compound=LEFT, height=25, width=90, font=('Times', 12),
                     command=lambda: self.show(self.home))
        img.image = render
        img.place(x=0, y=0)

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
        sheet.config(bg='grey90')
        sheet.place(x=450,y=200,height=175,width=330)

        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(sheet, image=render, cursor='hand2', text='Spread Sheet',compound=RIGHT, height=50, width=150, font=('Times', 13),
                     command=lambda: self.show(spread))
        img.image = render
        img.place(x=60, y=50)

        '''SPREAD SHEET OF SELECTED DETAILS''' #########################################################################################################

        spread= Frame(self.root)
        spread.config(bg='grey90')
        spread.place(x=195, y=200, height=390, width=830)

        load = Image.open("man.png")
        resize = load.resize((10, 10), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(spread, image=render, text='Back',compound=LEFT, height=20, width=80, font=('Times', 12),
                     command=lambda: show(view))
        img.image = render
        img.place(x=0, y=0)

        Label(spread, text='Student Attendance', font=("Times", 22)).place(x=300, y=0)
        Label(spread, text='course code and course name', font=("Times", 14)).place(x=100, y=50)
        Label(spread, text='Lecturer', font=("Times", 14)).place(x=600, y=50)

        fullsheet = Frame(spread)
        fullsheet.config(bg='#ffffff')
        fullsheet.place(x=50, y=80, height=300, width=700)

        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(fullsheet, image=render, cursor='hand2', text='Back',compound=LEFT, height=25, width=90, font=('Times', 12),
                     command=lambda: self.show(view))
        img.image = render
        img.place(x=0, y=0)

        '''SPREAD SHEET TABLE''' ##################################################################################################################################

        scroll_x = Scrollbar(fullsheet, orient=HORIZONTAL)
        scroll_y = Scrollbar(fullsheet, orient=VERTICAL)

        self.sheettable = Treeview(fullsheet, column=('name', 'email', 'regno', 'course'), xscrollcommand=scroll_x,
                               yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.sheettable.heading('name', text="Name")
        self.sheettable.heading('email', text="Email")
        self.sheettable.heading('regno', text="Regno")
        self.sheettable.heading('course', text="Course")

        self.sheettable['show'] = 'headings'
        self.sheettable.column('name', width=100)
        self.sheettable.column('email', width=100)
        self.sheettable.column('regno', width=100)
        self.sheettable.column('course', width=100)

        self.sheettable.pack(fill=BOTH, expand=1)

        '''MANAGE PAGE''' ########################################################################################################################################33

        self.manage = Frame(self.root)
        self.manage.config(bg='grey90')
        self.manage.place(height=1000, width=1200, x=185, y=0)

        '''OVERALL  AVERAGE DETAILS''' ############################################################################################################################################

        self.s2=Frame(self.manage)
        self.s2.config( bg="#ffffff", cursor='hand2')
        self.s2.place(x=10, y=50, height=100, width=200)
        Label(self.s2,text='Students',font=('Times',12),bg='#ffffff').place(x=15, y=70)
        Label(self.s2, text='Students', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        self.t2=Frame(self.manage)
        self.t2.config( bg="#ffffff", cursor='hand2')
        self.t2.place(x=220, y=50, height=100, width=200)
        Label(self.t2, text='Lectures', font=('Times', 12),bg='#ffffff').place(x=15, y=70)
        Label(self.t2, text='Lectures', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        self.u2=Frame(self.manage)
        self.u2.config(bg="#ffffff", cursor='hand2')
        self.u2.place(x=430, y=50, height=100, width=200)
        Label(self.u2, text='Units', font=('Times', 12),bg='#ffffff').place(x=15, y=70)
        Label(self.u2, text='Units', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        self.c2=Frame(self.manage)
        self.c2.config(bg="#ffffff", cursor='hand2')
        self.c2.place(x=640, y=50, height=100, width=200)
        Label(self.c2, text='Courses', font=('Times', 12),bg='#ffffff').place(x=15, y=70)
        Label(self.c2, text='Courses', font=('Times', 12,'italic'), bg='#ffffff').place(x=140, y=40)

        recent = Frame(self.manage)
        recent.config(bg="#ffffff")
        recent.place(x=850, y=0, height=1000, width=200)
        Label(recent, text="Recent Classes",bg='#ffffff',font=('Times',13,'italic','underline')).place(x=20, y=20)

        '''MANAGEMENT DETAILS ''' ##############################################################################################################################

        managepro=Frame(self.manage)
        managepro.config(bg="grey90")
        managepro.place(x=0, y=200, height=390, width=840)

        Label(managepro,text='Choose One for Management',bg='grey90',font=('Times',25)).place(x=200,y=10)

        load = Image.open("Student.png")
        resize = load.resize((50, 50), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(managepro, image=render, text='Students',compound=TOP, height=105, width=210, cursor='hand2', bg='#ffffff', font=('Times', 12),
                     command=lambda:show(edit1))
        img.image = render
        img.place(x=100,y=100)

        load = Image.open("Presentation.png")
        resize = load.resize((50, 50), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(managepro, image=render, text='Lectures', bg='#ffffff', compound=TOP, cursor='hand2', height=105, width=210,
                    font=('Times', 12),command=lambda: show(edit2))
        img.image = render
        img.place(x=450, y=100)

        load = Image.open("books1.png")
        resize = load.resize((50, 50), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(managepro, image=render, text='Units', bg='#ffffff', compound=TOP, cursor='hand2', height=105,
                     width=210,font=('Times', 12), command=lambda: show(edit3))
        img.image = render
        img.place(x=100, y=250)

        load = Image.open("books (2).png")
        resize = load.resize((50, 50), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(managepro, image=render, text='Courses', bg='#ffffff', compound=TOP, cursor='hand2', height=105,
                     width=210,font=('Times', 12), command=lambda: show(edit4))
        img.image = render
        img.place(x=450, y=250)

        '''EDIT STUDENTS''' #################################################################################################################################33

        edit1 = Frame(self.root)
        edit1.config(bg="grey90")
        edit1.place(x=195, y=180, height=415, width=830)

        edit11 = Frame(edit1)
        edit11.config(bg="grey90")
        edit11.place(x=0,y=0,height=1000,width=400)

        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(edit11, image=render, cursor='hand2', text='Back', compound=LEFT, height=25, width=90, font=('Times', 12),
                     command=lambda: self.show(self.manage))
        img.image = render
        img.place(x=0, y=0)

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

        def add():
            return sadd()
        def update():
            return supdate()
        def delete():
            return sdelete
        def clear():
             return sclear()

        Button(edit11,text='Add',bg ='green', cursor='hand2',fg='white',width=10,command=lambda:add()).place(x=20,y=370)
        Button(edit11, text='Update',bg ='blue', cursor='hand2',fg='white',width=10,command=lambda:update()).place(x=110,y=370)
        Button(edit11, text='Delete',bg ='red', cursor='hand2',fg='white',width=10,command=lambda:delete()).place(x=200,y=370)
        Button(edit11, text='Clear',bg ='orange', cursor='hand2',fg='white',width=10,command=lambda:clear()).place(x=290,y=370)

        edit101 = Frame(edit1)
        edit101.config(bg="grey90")
        edit101.place(x=375,y=50,height=1000,width=500)

        searchvar1=StringVar()

        Label(edit101,text='Search By',bg='grey90',font=('times',15)).place(x=150,y=10)
        Entry(edit101,textvariable=searchvar1,bd=0 ).place(x=120,y=50 ,height=25)

        Button(edit101, text='Search', cursor='hand2').place(x=250,y=50)
        Button(edit101, text='Show All',command=lambda:self.stfetch_data()).place(x=300, y=50)

        edit1010=Frame(edit1)
        edit1010.config(bg='#ffffff')
        edit1010.place(x=385,y=140,height=280,width=450)

        '''STUDENTS EDIT TABLE ''' ###################################################################################################################################33

        scroll_x = Scrollbar(edit1010, orient=HORIZONTAL)
        scroll_y = Scrollbar(edit1010, orient=VERTICAL)

        self.stable= Treeview(edit1010,column=('name','email','regno','course'),xscrollcommand=scroll_x,yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        self.stable.heading('name',text="Name")
        self.stable.heading('email', text="Email")
        self.stable.heading('regno', text="Regno")
        self.stable.heading('course', text="Course")

        self.stable['show']='headings'
        self.stable.column('name', width=100)
        self.stable.column('email', width=100)
        self.stable.column('regno', width=100)
        self.stable.column ('course', width=100)

        self.stable.pack(fill=BOTH,expand=1)

        '''STUDENTS EDIT FUNCTIONS''' #######################################################################################################################3

        def sadd():
            name = sname.get()
            email = semail.get()
            regno = sregno.get()
            cou= scourse.get()

            mailform = re.findall('@', email)

            if not mailform:
                return messagebox.showerror('email formart', parent=root)

            if (name and email and regno and cou):
                try:
                    conn = sa.connect(host="localhost", user="root", password="", database="Recon")
                    cur = conn.cursor()
                    make="CREATE TABLE IF NOT EXISTS Students1( Name varchar(100) not null,Email varchar(100) not null,Regno varchar(100) not null, Course varchar(100) not null )"
                    cur.execute(make)
                    jin="INSERT INTO Students1(Name,Email,RegNo,Course) Values(%s,%s,%s,%s)"
                    kazama=(name ,email ,regno ,cou)
                    cur.execute(jin,kazama)
                    conn.commit()
                    self.countstudents()
                    self.stfetch_data()
                    conn.close()
                    messagebox.showinfo('waze', parent=root)
                except:
                    print('connect to database')

            else :
                messagebox.showerror('Student Not added' , parent=root)

        def supdate():
            return
        def sdelete():
            return
        def sclear():
             return

        '''EDIT LECTURERS '''

        edit2 = Frame(self.root)
        edit2.config(bg='grey90')
        edit2.place(x=195, y=180, height=415, width=830)

        edit22 = Frame(edit2)
        edit22.config(bg="grey90")
        edit22.place(x=0,y=0,height=1000,width=400)

        Label(edit2, text='Edit Lectures', bg='grey90', font=('Times', 18)).place(x=300, y=20)

        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(edit22, image=render, text='Back', cursor='hand2', compound=LEFT, height=25, width=90, font=('Times', 12),
                     command=lambda: self.show(self.manage))
        img.image = render
        img.place(x=0, y=0)

        lname=StringVar()
        lemail = StringVar()
        lregno = StringVar()
        lcourse = StringVar()

        Label(edit22, text='Name', font=('Times', 12), bg='grey90').place(x=25, y=110)
        Entry(edit22, textvariable=lname, font=('Times', 14), width=20, bd=0).place(x=40, y=140, height=30)
        Canvas(edit22, width=180, height=2.0, bg='#000000').place(x=40, y=163)
        Label(edit22, text='Email', font=('Times', 12), bg='grey90').place(x=25, y=170)
        Entry(edit22, textvariable=lemail, font=('Times', 14), width=20, bd=0).place(x=40, y=200, height=30)
        Canvas(edit22, width=180, height=2.0, bg='#000000').place(x=40, y=223)
        Label(edit22, text='Reg no', font=('Times', 12), bg='grey90').place(x=25, y=230)
        Entry(edit22, textvariable=lregno, font=('Times', 14), width=20, bd=0).place(x=40, y=260, height=30)
        Canvas(edit22, width=180, height=2.0, bg='#000000').place(x=40, y=283)
        Label(edit22, text='Course', font=('Times', 12), bg='grey90').place(x=25, y=290)
        Entry(edit22, textvariable=lcourse, font=('Times', 14), width=20, bd=0).place(x=40, y=320, height=30)
        Canvas(edit22, width=180, height=2.0, bg='#000000').place(x=40, y=343)

        def add2():
            return ladd2()

        def update2():
            return lupdate2()

        def delete2():
            return ldelete2()

        def clear2():
            return lclear2()

        Button(edit22,text='Add',bg ='green',fg='white', cursor='hand2',width=10,command=lambda:add2()).place(x=20,y=370)
        Button(edit22, text='Update',bg ='blue',fg='white', cursor='hand2',width=10,command=lambda:update2()).place(x=110,y=370)
        Button(edit22, text='Delete',bg ='red',fg='white', cursor='hand2',width=10,command=lambda:delete2()).place(x=200,y=370)
        Button(edit22, text='Clear',bg ='orange',fg='white', cursor='hand2',width=10,command=lambda:clear2()).place(x=290,y=370)

        edit202 = Frame(edit2)
        edit202.config(bg="grey90")
        edit202.place(x=375,y=50,height=1000,width=500)

        searchvar2=StringVar()

        Label(edit202,text='Search By',bg='grey90',font=('times',15)).place(x=150,y=10)
        Entry(edit202,textvariable=searchvar2,bd=0 ).place(x=120,y=50 ,height=25)

        Button(edit202, text='Search').place(x=250,y=50)
        Button(edit202, text='Show All',command=lambda:self.lecfetch_data()).place(x=300, y=50)

        edit2020=Frame(edit2)
        edit2020.config(bg='#ffffff')
        edit2020.place(x=385,y=140,height=280,width=450)

        '''LECTURERS TABLE''' ##################################################################################################################################

        scroll_x = Scrollbar(edit2020, orient=HORIZONTAL)
        scroll_y = Scrollbar(edit2020, orient=VERTICAL)

        self.ltable = Treeview(edit2020, column=('name','email','regno','course'), xscrollcommand=scroll_x,
                          yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.ltable.heading('name', text="Name")
        self.ltable.heading('email', text="Email")
        self.ltable.heading('regno', text="Regno")
        self.ltable.heading('course', text="Course")

        self.ltable['show'] = 'headings'
        self.ltable.column('name', width=100)
        self.ltable.column('email', width=100)
        self.ltable.column('regno', width=100)
        self.ltable.column('course', width=100)

        self.ltable.pack(fill=BOTH, expand=1)

        '''EDIT LECTURERS FUNCTIONS''' ##########################################################################################################################

        def ladd2():
            name = lname.get()
            email = lemail.get()
            regno = lregno.get()
            cou = lcourse.get()

            mailform = re.findall('@', email)

            if not mailform:
                return messagebox.showerror('email formart', parent=root)

            if (name and email and regno and cou):
                try:
                    conn = sa.connect(host="localhost", user="root", password="", database="Recon")
                    cur = conn.cursor()
                    make = "CREATE TABLE IF NOT EXISTS Lectures1( Name varchar(100) not null,Email varchar(100) not null,Regno varchar(100) not null, Course varchar(100) not null )"
                    cur.execute(make)
                    jin = "INSERT INTO Lectures1(Name,Email,RegNo,Course) Values(%s,%s,%s,%s)"
                    kazama = (name, email, regno, cou)
                    cur.execute(jin, kazama)
                    conn.commit()
                    self.countlecturer()
                    self.lecfetch_data()
                    conn.close()
                    messagebox.showinfo('waze', parent=root)
                except:
                    print('Database error')
            else:
                messagebox.showerror('Lecturer not added', parent=root)

        def lupdate2():
            return

        def ldelete2():
            return

        def lclear2():
            return

        '''EDIT UNIT '''########################################################################################################################################3

        edit3 = Frame(self.root)
        edit3.config(bg="grey90")
        edit3.place(x=195, y=200, height=390, width=830)

        edit33 = Frame(edit3)
        edit33.config(bg="grey90")
        edit33.place(x=0,y=0,height=1000,width=400)

        Label(edit33, text='Edit Units', bg='grey90', font=('Times', 18)).place(x=300, y=20)

        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(edit33, image=render, text='Back', cursor='hand2', compound=LEFT, height=25, width=90, font=('Times', 12),
                     command=lambda: self.show(self.manage))
        img.image = render
        img.place(x=0, y=0)

        ucode=StringVar()
        uname = StringVar()
        ulecture = StringVar()
        ucourse = StringVar()

        Label(edit33, text='Course Code', font=('Times', 12), bg='grey90').place(x=25, y=110)
        Entry(edit33, textvariable=ucode, font=('Times', 14), width=20, bd=0).place(x=40, y=140, height=30)
        Canvas(edit33, width=180, height=2.0, bg='#000000').place(x=40, y=163)
        Label(edit33, text='Name', font=('Times', 12), bg='grey90').place(x=25, y=170)
        Entry(edit33, textvariable=uname, font=('Times', 14), width=20, bd=0).place(x=40, y=200, height=30)
        Canvas(edit33, width=180, height=2.0, bg='#000000').place(x=40, y=223)
        Label(edit33, text='Lecturer', font=('Times', 12), bg='grey90').place(x=25, y=230)
        Entry(edit33, textvariable=ulecture, font=('Times', 14), width=20, bd=0).place(x=40, y=260, height=30)
        Canvas(edit33, width=180, height=2.0, bg='#000000').place(x=40, y=283)
        Label(edit33, text='Course', font=('Times', 12), bg='grey90').place(x=25, y=290)
        Entry(edit33, textvariable=ucourse, font=('Times', 14), width=20, bd=0).place(x=40, y=320, height=30)
        Canvas(edit33, width=180, height=2.0, bg='#000000').place(x=40, y=343)

        def add3():
            return uadd3()

        def update3():
            return uupdate3()

        def delete3():
            return udelete3()

        def clear3():
            return uclear3()

        Button(edit33,text='Add',bg ='green',fg='white',width=10, cursor='hand2',command=lambda:add3()).place(x=20,y=362)
        Button(edit33, text='Update',bg ='blue',fg='white',width=10, cursor='hand2',command=lambda:update3()).place(x=110,y=362)
        Button(edit33, text='Delete',bg ='red',fg='white',width=10, cursor='hand2',command=lambda:delete3()).place(x=200,y=362)
        Button(edit33, text='Clear',bg ='orange',fg='white',width=10, cursor='hand2',command=lambda:clear3()).place(x=290,y=362)

        edit303 = Frame(edit3)
        edit303.config(bg="grey90")
        edit303.place(x=375,y=50,height=1000,width=500)

        searchvar3=StringVar()

        Label(edit303,text='Search By',bg='grey90',font=('times',15)).place(x=150,y=10)
        Entry(edit303,textvariable=searchvar3,bd=0 ).place(x=120,y=50 ,height=25)

        Button(edit303, text='Search').place(x=250,y=50)
        Button(edit303, text='Show All',command=lambda:self.unfetch_data()).place(x=300, y=50)

        edit3030=Frame(edit3)
        edit3030.config(bg='#ffffff')
        edit3030.place(x=385,y=140,height=255,width=450)

        '''UNITS EDIT TABLE''' ################################################################################################################################

        scroll_x = Scrollbar(edit3030, orient=HORIZONTAL)
        scroll_y = Scrollbar(edit3030, orient=VERTICAL)

        self.utable = Treeview(edit3030, column=('code', 'name', 'lecturer', 'school'), xscrollcommand=scroll_x,
                          yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.utable.heading('code', text="Code")
        self.utable.heading('name', text="Name")
        self.utable.heading('lecturer', text="Lecturer")
        self.utable.heading('school', text="Course")

        self.utable['show'] = 'headings'
        self.utable.column('code', width=100)
        self.utable.column('name', width=100)
        self.utable.column('lecturer', width=100)
        self.utable.column('school', width=100)

        self.utable.pack(fill=BOTH, expand=1)

        '''UNIT EDIT FUNCTIONS ''' ########################################################################################################################################################

        def uadd3():
            code = ucode.get()
            name = uname.get()
            lec = ulecture.get()
            cou = ucourse.get()

            if (name and code and lec and cou):
                try:
                    conn = sa.connect(host="localhost", user="root", password="", database="Recon")
                    cur = conn.cursor()
                    make = "CREATE TABLE IF NOT EXISTS Units1( Code varchar(100) not null,Name varchar(100) not null,Lectures varchar(100) not null, Course varchar(100) not null )"
                    cur.execute(make)
                    jin = "INSERT INTO Units1(code,name,lectures,Course) Values(%s,%s,%s,%s)"
                    kazama = (code, name, lec, cou)
                    cur.execute(jin, kazama)
                    conn.commit()
                    self.countunits()
                    self.unfetch_data()
                    conn.close()
                    messagebox.showinfo('waze', parent=root)
                except:
                    print('Database error')

            else:
                messagebox.showerror('password formart', parent=root)

        def uupdate3():
            return

        def udelete3():
            return

        def uclear3():
            return

        '''COURSES  EDIT''' #########################################################################################################################################

        edit4 = Frame(self.root)
        edit4.config(bg="grey90")
        edit4.place(x=195, y=200, height=390, width=830)

        edit44 = Frame(edit4)
        edit44.config(bg="grey90")
        edit44.place(x=0,y=0,height=1000,width=400)

        Label(edit44, text='Edit Units', bg='grey90', font=('Times', 18)).place(x=300, y=20)

        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(edit44, image=render, text='Back', cursor='hand2', compound=LEFT, height=25, width=90, font=('Times', 12),
                     command=lambda: self.show(self.manage))
        img.image = render
        img.place(x=0, y=0)

        cname=StringVar()

        Label(edit44, text='Name', font=('Times', 12), bg='grey90').place(x=25, y=170)
        Entry(edit44, textvariable=cname, font=('Times', 14), width=20, bd=0).place(x=40, y=200, height=30)
        Canvas(edit44, width=180, height=2.0, bg='#000000').place(x=40, y=223)

        def add4():
            return cadd4()
        def update4():
            return cupdate4()

        def delete4():
            return cdelete4()

        def clear4():
            return cclear4()

        Button(edit44, text='Add',bg ='green',fg='white', width=10, cursor='hand2',command=lambda:add4()).place(x=20, y=300)
        Button(edit44, text='Update',bg ='blue',fg='white', width=10, cursor='hand2',command=lambda:update4()).place(x=110, y=300)
        Button(edit44, text='Delete',bg ='red',fg='white', width=10, cursor='hand2',command=lambda:delete4()).place(x=200, y=300)
        Button(edit44, text='Clear',bg ='orange',fg='white', width=10, cursor='hand2',command=lambda:clear4()).place(x=290, y=300)

        edit404 = Frame(edit4)
        edit404.config(bg="grey90")
        edit404.place(x=375,y=50,height=1000,width=500)

        searchvar4=StringVar()

        Label(edit404,text='Search By',bg='grey90',font=('times',15)).place(x=150,y=10)
        Entry(edit404,textvariable=searchvar4,bd=0 ).place(x=120,y=50, height=25)

        Button(edit404, text='Search').place(x=250,y=50)
        Button(edit404, text='Show All',command=lambda:self.cofetch_data()).place(x=300, y=50)

        edit4040=Frame(edit4)
        edit4040.config(bg='#ffffff')
        edit4040.place(x=385,y=140,height=255,width=450)

        '''COURSE EDIT TABLE''' ######################################################################################################################################

        scroll_x = Scrollbar(edit4040, orient=HORIZONTAL)
        scroll_y = Scrollbar(edit4040, orient=VERTICAL)

        self.ctable = Treeview(edit4040, column=('name'), xscrollcommand=scroll_x , yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.ctable.heading('name', text="Name")

        self.ctable['show'] = 'headings'
        self.ctable.column('name', width=200)

        self.ctable.pack(fill=BOTH, expand=1)
        self.ctable.bind("<ButtonRelease-1>",get_cursor())


        '''COURSE EDIT FUNCTIONS''' #######################################################################################################################################

        def cadd4():
            name = cname.get()

            if name:
                try:
                    conn = sa.connect(host="localhost", user="root", password="", database="Recon")
                    cur = conn.cursor()
                    make = "CREATE TABLE IF NOT EXISTS course1(Name varchar(100) not null )"
                    cur.execute(make)
                    jin = "INSERT INTO course1(Name) Values(%s)"
                    kazama = (name,)
                    cur.execute(jin,kazama)
                    conn.commit()
                    self.countcourse()
                    self.cofetch_data()
                    cclear4()
                    conn.close()

                    messagebox.showinfo('waze', parent=root)
                except:
                    print('Database error')
            else:
                messagebox.showerror('database error', parent=root)

        def get_cursor():
            c_row = self.ctable.focus()
            contents = self.ctable.items(c_row)
            row = contents['values']
            cname.set(row[0])

        def cupdate4():
            return update()

        def cdelete4():
            return delete()

        def cclear4():
            name=cname
            name.set('')




        '''HELP PAGE''' ###########################################################################################################################################

        self.helpp = Frame(self.root)
        self.helpp.config(bg='grey90', cursor='hand2')
        self.helpp.place(height=1000, width=1200, x=185, y=0)

        Label(self.helpp,text='').place()

        '''SETTINGS PAGE''' #####################################################################################################################################

        self.settings = Frame(self.root)
        self.settings.config(bg='grey90', cursor='hand2')
        self.settings.place(height=1000, width=1200, x=185, y=0)

        '''OVERALL AVERAGE DETAILS'''  ##########################################################################################################################

        self.s3 = Frame(self.settings)
        self.s3.config(bg="#ffffff", cursor='hand2')
        self.s3.place(x=10, y=50, height=100, width=200)
        Label(self.s3, text='Students', font=('Times', 12), bg='#ffffff').place(x=15, y=70)
        Label(self.s3, text='Students', font=('Times', 12, 'italic'), bg='#ffffff').place(x=140, y=40)

        self.t3 = Frame(self.settings)
        self.t3.config(bg="#ffffff", cursor='hand2')
        self.t3.place(x=220, y=50, height=100, width=200)
        Label(self.t3, text='Lectures', font=('Times', 12), bg='#ffffff').place(x=15, y=70)
        Label(self.t3, text='Lectures', font=('Times', 12, 'italic'), bg='#ffffff').place(x=140, y=40)

        self.u3 = Frame(self.settings)
        self.u3.config(bg="#ffffff", cursor='hand2')
        self.u3.place(x=430, y=50, height=100, width=200)
        Label(self.u3, text='Units', font=('Times', 12), bg='#ffffff').place(x=15, y=70)
        Label(self.u3, text='Units', font=('Times', 12, 'italic'), bg='#ffffff').place(x=140, y=40)

        self.c3 = Frame(self.settings)
        self.c3.config(bg="#ffffff", cursor='hand2')
        self.c3.place(x=640, y=50, height=100, width=200)
        Label(self.c3, text='Courses', font=('Times', 12), bg='#ffffff').place(x=15, y=70)
        Label(self.c3, text='Courses', font=('Times', 12, 'italic'), bg='#ffffff').place(x=140, y=40)

        Label(self.settings, text='Change Your Profile',font=('Times',20),bg='grey90').place(x=200,y=250)

        Button(self.settings, text='Change Name',height=2,width=15,font=("times",12), command=lambda: show(nameframe)).place(x=50, y=330)
        Button(self.settings, text='Change Email',height=2,width=15,font=("times",12), command=lambda: show(emailframe)).place(x=50, y=410)
        Button(self.settings,text='Change Password',height=2,width=15,font=("times",12), command=lambda:show(passwordframe)).place(x=50,y=480)

        ok=Frame(self.root)
        ok.config(bg='grey90')
        ok.place (x=500,y=300,height=250,width=400)

        nameset = StringVar()
        emailset = StringVar()
        newpas = StringVar()
        conpas = StringVar()

        def setname():
            setname2()

        def setemail():
            setemail2()

        def setpass():
            setpass2()

        nameframe=Frame(self.root)
        nameframe.config(bg='#ffffff')
        nameframe.place (x=500,y=300,height=250,width=400)

        Label(nameframe, text='Enter new Name', font=('Times', 12), bg='#ffffff').place(x=25, y=50)
        Entry( nameframe, textvariable=nameset, font=('Times', 14), width=20, bd=0).place(x=40, y=70, height=30)
        Canvas( nameframe, width=180, height=2.0, bg='#000000').place(x=40, y=93)
        Button(nameframe, text='Change', height=1, width=10, font=("times", 12),
               command=lambda: setname()).place(x=150, y=130)

        emailframe=Frame(self.root)
        emailframe.config(bg='#ffffff')
        emailframe.place (x=500,y=300,height=250,width=400)

        Label(emailframe, text='Enter new Email', font=('Times', 12), bg='#ffffff').place(x=25, y=50)
        Entry( emailframe, textvariable=emailset, font=('Times', 14), width=20, bd=0).place(x=40, y=70, height=30)
        Canvas( emailframe, width=180, height=2.0, bg='#000000').place(x=40, y=93)
        Button(emailframe, text='Change', height=1, width=10, font=("times",12 ),
               command=lambda: setemail()).place(x=150, y=130)

        passwordframe=Frame(self.root)
        passwordframe.config(bg='#ffffff')
        passwordframe.place (x=500,y=300,height=250,width=400)
        Button(passwordframe, text='Change', height=1, width=10, font=("times",12 ),
               command=lambda: setpass()).place(x=150, y=200)

        Label(passwordframe, text='Enter New Password', font=('Times', 12), bg='#ffffff').place(x=35, y=80)
        Entry( passwordframe, textvariable=newpas, font=('Times', 14), width=20, bd=0,show="*").place(x=40, y=100, height=30)
        Canvas( passwordframe, width=180, height=2.0, bg='#000000').place(x=40, y=123)

        Label(passwordframe, text='Confirm New Password', font=('Times', 12), bg='#ffffff').place(x=35, y=140)
        Entry( passwordframe, textvariable=conpas, font=('Times', 14), width=20, bd=0,show="*").place(x=40, y=160, height=30)
        Canvas( passwordframe, width=180, height=2.0, bg='#000000').place(x=40, y=183)

        '''SETTINGS EDIT FUNCTIONS '''###################################################################################################################################

        def setname2():
            name=nameset.get()
            if name:
                try:
                    conn = sa.connect(host='localhost', user='root', password='', database='recon')
                    cur = conn.cursor()
                    das="UPDATE admin SET name= %s WHERE phone='90'"
                    kumi=(name,)
                    cur.execute(das,kumi)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('New Name Set', parent=root)
                    self.show(ok)
                except:
                    print('Database Error')

            else :
                messagebox.showerror('no blank name ', parent=root)

        def setemail2():
            email=emailset.get()
            if email:
                try:
                    conn = sa.connect(host='localhost', user='root', password='', database='recon')
                    cur = conn.cursor()
                    das = "UPDATE admin SET email=%s WHERE phone ='90'"
                    kumi = (email,)
                    cur.execute(das, kumi)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('New Email Set', parent=root)
                    self.show(ok)
                except:
                    print('Database error')

            else:
                messagebox.showerror('no blank name ', parent=root)

        def setpass2():

            new=newpas.get()
            con=conpas.get()

            if new and con:
                if new != con:
                    return messagebox.showerror('password is not the same', parent=root)

                try:
                    conn = sa.connect(host='localhost', user='root', password='', database='recon')
                    cur = conn.cursor()
                    das = "UPDATE admin SET password=%s WHERE phone ='90'"
                    kumi = (new,)
                    cur.execute(das, kumi)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo('New Password Set', parent=root)
                    self.show(ok)
                except:
                    messagebox.showerror('no database connection ', parent=root)
            else:
                messagebox.showerror('no blank name ', parent=root)

        '''CALLING OTHER FUNCTIONS''' #############################################################################################################################

        self.show(self.home)
        self.countstudents()
        self.countlecturer()
        self.countunits()
        self.countcourse()
        self.fin()
        self.button()

    '''DASHBOARD IMAGES AND BUTTONS ''' #########################################################################################################################

    def button(self):
        Button(self.pop, activebackground='grey90', text='Dashboard', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0,
               font=('Times', 13), width=20, height=3, command=lambda: self.show(self.home)).place(x=0, y=200)
        Button(self.pop, activebackground='grey90', text='Manage', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0,
               font=('Times', 13), width=20, height=3, command=lambda: self.show(self.manage)).place(x=0, y=269)
        Button(self.pop, activebackground='grey90', text='Help', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0,
               font=('Times', 13), width=20, height=3, command=lambda: self.show(self.helpp)).place(x=0, y=337)
        Button(self.pop, activebackground='grey90', text='Settings', bg='slate blue', fg='#ffffff', cursor='hand2',
               bd=0, font=('Times', 13), width=20, height=3, command=lambda: self.show(self.settings)).place(x=0, y=404)
        Button(self.pop, activebackground='grey90', text='Log Out', bg='slate blue', fg='#ffffff', cursor='hand2', bd=0,
               font=('Times', 13),width=20, height=3,command=lambda :login()).place(x=0, y=470)

        load001h = Image.open("../../../../../Desktop/rnn/frontend/home.png")
        resize001h = load001h.resize((20, 20), Image.LANCZOS)
        render001h = ImageTk.PhotoImage(resize001h)
        img001h = Label(self.pop, image=render001h, bg='slate blue')
        img001h.image = render001h
        img001h.place(x=30, y=220)

        load001m = Image.open("../../../../../Desktop/rnn/frontend/add-contact.png")
        resize001m = load001m.resize((30, 30), Image.LANCZOS)
        render001m = ImageTk.PhotoImage(resize001m)
        img001m = Label(self.pop, image=render001m, bg='slate blue')
        img001m.image = render001m
        img001m.place(x=30, y=289)

        load001p = Image.open("../../../../../Desktop/rnn/frontend/help.png")
        resize001p = load001p.resize((20, 20), Image.LANCZOS)
        render001p = ImageTk.PhotoImage(resize001p)
        img001p = Label(self.pop, image=render001p, bg='slate blue')
        img001p.image = render001p
        img001p.place(x=45, y=357)

        load001s = Image.open("../../../../../Desktop/rnn/frontend/settings-free-icon-font.png")
        resize001s = load001s.resize((20, 20), Image.LANCZOS)
        render001s = ImageTk.PhotoImage(resize001s)
        img001s = Label(self.pop, image=render001s, bg='slate blue')
        img001s.image = render001s
        img001s.place(x=35, y=424)

        load001o = Image.open("../../../../../Desktop/rnn/frontend/exit.png")
        resize001o = load001o.resize((20, 20), Image.LANCZOS)
        render001o = ImageTk.PhotoImage(resize001o)
        img001o = Label(self.pop, image=render001o, bg='slate blue')
        img001o.image = render001o
        img001o.place(x=30, y=490)


    '''FETCH DATA TO EDIT PAGES ''' #######################################################################################################################

    def stfetch_data(self):
        table = self.stable
        conn = sa.connect(host="localhost", user="root", password="", database="Recon")
        cur = conn.cursor()
        cur.execute('SELECT * FROM Students1')
        rows = cur.fetchall()
        conn.commit()
        if len(rows) != 0:
            self.stable.delete(*self.stable.get_children())
            for row in rows:
                table.insert("", 'end', values=(row[0], row[1], row[2], row[3]))
        conn.close()




    def lecfetch_data(self):
        table = self.ltable
        conn = sa.connect(host="localhost", user="root", password="", database="Recon")
        cur = conn.cursor()
        cur.execute('SELECT * FROM Lectures1')
        rows = cur.fetchall()
        conn.commit()
        if len(rows) != 0:
            self.ltable.delete(*self.ltable.get_children())
            for row in rows:
                table.insert("", 'end', values=(row[0], row[1], row[2], row[3]))
        conn.close()

    def unfetch_data(self):
        table = self.utable
        conn = sa.connect(host="localhost", user="root", password="", database="Recon")
        cur = conn.cursor()
        cur.execute('SELECT * FROM Units1')
        rows = cur.fetchall()
        conn.commit()
        if len(rows) != 0:
            self.utable.delete(*self.utable.get_children())
            for row in rows:
                table.insert("", 'end', values=(row[0], row[1], row[2], row[3]))
        conn.close()

    def cofetch_data(self):
        table = self.ctable
        conn = sa.connect(host="localhost", user="root", password="", database="Recon")
        cur = conn.cursor()
        cur.execute('SELECT * FROM Course1')
        rows = cur.fetchall()
        conn.commit()
        if len(rows) != 0:
            self.ctable.delete(*self.ctable.get_children())
            for row in rows:
                table.insert("", 'end', values=(row[0],))
        conn.close()

    '''COUNT OVERALL AVERAGE DETAILS''' #################################################################################################################################

    def countstudents(self):
        conn = sa.connect(host="localhost", user="root", password="", database="Recon")
        cur = conn.cursor()
        cur.execute('SELECT count(name) FROM Students1')
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        Label(self.s,text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)
        Label(self.s2, text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)
        Label(self.s3, text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)

    def countlecturer(self):
        conn = sa.connect(host="localhost", user="root", password="", database="Recon")
        cur = conn.cursor()
        cur.execute('SELECT count(name) FROM Lectures1')
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        Label(self.t,text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)
        Label(self.t2, text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)
        Label(self.t3, text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)

    def countunits(self):
        conn = sa.connect(host="localhost", user="root", password="", database="Recon")
        cur = conn.cursor()
        cur.execute('SELECT count(name) FROM units1')
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        Label(self.u,text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)
        Label(self.u2, text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)
        Label(self.u3, text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)

    def countcourse(self):
        conn = sa.connect(host="localhost", user="root", password="", database="Recon")
        cur = conn.cursor()
        cur.execute('SELECT count(name) FROM course1')
        rows = cur.fetchall()
        conn.commit()
        conn.close()
        Label(self.c,text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)
        Label(self.c2, text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)
        Label(self.c3, text=rows, font=('Times', 20, 'italic'), bg='#ffffff').place(x=100, y=30)


    '''IMAGES IN THE SYSTEM'''#######################################################################################################################################################
    def fin(self):
        load = Image.open("man.png")
        resize = load.resize((150, 150), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Label(self.pop, image=render ,bg='slate blue')
        img.image = render
        img.place(x=15, y=40)

        load001s = Image.open("student.png")
        resize001s = load001s.resize((60, 60), Image.LANCZOS)
        render001s = ImageTk.PhotoImage(resize001s)
        img001s = Label(self.s, image=render001s, bg='#ffffff')
        img002s = Label(self.s2, image=render001s, bg='#ffffff')
        img003s = Label(self.s3, image=render001s, bg='#ffffff')
        img001s.image = render001s
        img002s.image = render001s
        img003s.image = render001s
        img001s.place(x=15, y=10)
        img002s.place(x=15, y=10)
        img003s.place(x=15, y=10)

        load001t = Image.open("presentation.png")
        resize001t = load001t.resize((60, 60), Image.LANCZOS)
        render001t = ImageTk.PhotoImage(resize001t)
        img001t = Label(self.t, image=render001t, bg='#ffffff')
        img002t = Label(self.t2, image=render001t, bg='#ffffff')
        img003t = Label(self.t3, image=render001t, bg='#ffffff')
        img001t.image = render001t
        img002t.image = render001t
        img003t.image = render001t
        img001t.place(x=15, y=13)
        img002t.place(x=15, y=13)
        img003t.place(x=15, y=13)

        load001u = Image.open("books1.png")
        resize001u = load001u.resize((60, 60), Image.LANCZOS)
        render001u = ImageTk.PhotoImage(resize001u)
        img001u = Label(self.u, image=render001u, bg='#ffffff')
        img002u = Label(self.u2, image=render001u, bg='#ffffff')
        img003u = Label(self.u3, image=render001u, bg='#ffffff')
        img001u.image = render001u
        img002u.image = render001u
        img003u.image = render001u
        img001u.place(x=15, y=13)
        img002u.place(x=15, y=13)
        img003u.place(x=15, y=13)

        load001c = Image.open("books (2).png")
        resize001c = load001c.resize((60, 60), Image.LANCZOS)
        render001c = ImageTk.PhotoImage(resize001c)
        img001c = Label(self.c, image=render001c, bg='#ffffff')
        img002c = Label(self.c2, image=render001c, bg='#ffffff')
        img003c = Label(self.c3, image=render001c, bg='#ffffff')
        img001c.image = render001c
        img002c.image = render001c
        img003c.image = render001c
        img001c.place(x=15, y=10)
        img002c.place(x=15, y=10)
        img003c.place(x=15, y=10)

    def show(self,fram):
        return fram.tkraise(aboveThis=None)

def board():
    root=Tk()
    Home(root)
    root.mainloop()

if __name__=='__main__':
     board()
