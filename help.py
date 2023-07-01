from tkinter import *
from tkinter import ttk        #for stylish toolkit
from PIL import Image,ImageTk    # for importing images
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):   #for constructor call
        self.root=root   # root intialization
        self.root.geometry("1530x790+0+0")   #0,0 for starting from x=0,y=0
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue") 
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        img_top=Image.open(r"College Imges\help_desk.webp")   # r for backslash forwarded into frontslash
        img_top=img_top.resize((1530,900),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(f_lbl,text="Contact Us by The Given Email Address Below",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=580,y=50)

        dev_label=Label(f_lbl,text="Email : finalyearproject772@gmail.com",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=605,y=100)

        dev_label=Label(f_lbl,text="Thank You",font=("times new roman",16,"bold"),bg="white",fg='red')
        dev_label.place(x=720,y=150)






if __name__=="__main__":   
    root=Tk()
    obj=Help(root)
    root.mainloop()
   