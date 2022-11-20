from tkinter import *
from PIL import ImageTk, Image

class test:
    def __init__(self,root):
        self.root=root


        self.root.geometry("600x500")



        load = Image.open("man.png")
        resize = load.resize((20, 20), Image.LANCZOS)
        render = ImageTk.PhotoImage(resize)
        img = Button(self.root, image=render)
        img.image = render
        img.place(x=0, y=0)

def pop():
    root=Tk()
    test(root)
    root.mainloop()

if __name__=='__main__':
    pop()

