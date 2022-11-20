from tkinter import *

class pop:
    def __init__(self,root):
        self.root=root
        self.root.geometry("300x300")

        sting=StringVar()

        Label(self.root,text="name").place(x=10,y=10)
        Entry(self.root,textvariable=sting ).place(x=30,y=30)

        def kin1():

            sting1=sting.get()

            kin(sting1)


        Button(self.root,text='btn',command=kin1).place(x=60,y=60)

        def kin(sting):
            name = sting

            if (name):
                Label(self.root, text=name, fg='blue').place(x=150, y=30)
            else:
                Label(self.root, text="Enter name", fg="red").place(x=150, y=30)






def log():
    root=Tk()

    pop(root)

    root.mainloop()




if __name__=="__main__":
    log()