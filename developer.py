from tkinter import *
from tkinter import ttk        #for stylish toolkit
from PIL import Image,ImageTk    # for importing images
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):   #for constructor call
        self.root=root   # root intialization
        self.root.geometry("1530x790+0+0")   #0,0 for starting from x=0,y=0
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        title_lbl=Label(self.root,text="DEVELOPERS",font=("times new roman",35,"bold"),bg="white",fg="blue") 
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        img_top=Image.open(r"College Imges\wp1904069.jpg")   # r for backslash forwarded into frontslash
        img_top=img_top.resize((1530,900),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)

        # frames

        main_frame=Frame(f_lbl,bd=2,bg="white")  
        main_frame.place(x=520,y=50,width=500,height=600)

        img_top1=Image.open(r"College Imges\group.jpeg")   # r for backslash forwarded into frontslash
        img_top1=img_top1.resize((200,200),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=150,y=10,width=200,height=200)

        #developer info
        dev_label=Label(main_frame,text="Hello ! Our Names are ",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=115,y=210)

        dev_label=Label(main_frame,text="SK ABDUL AYUSH",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=150,y=250)

        dev_label=Label(main_frame,text="ROHIT GUPTA",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=170,y=280)

        dev_label=Label(main_frame,text="SOUVIK SHAW",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=170,y=310)

        dev_label=Label(main_frame,text="SAUMYAJYOTI MONDAL",font=("times new roman",16,"bold"),bg="white")
        dev_label.place(x=130,y=340)
        
        dev_label=Label(main_frame,text="We are Computer Science Engineers",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=35,y=380)
 
        dev_label=Label(main_frame,text="Who Created this Project",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=105,y=420)
        
        dev_label=Label(main_frame,text="As a Team",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=190,y=460)

        dev_label=Label(main_frame,text="Thank You",font=("times new roman",22,"bold"),fg="red",bg="white")
        dev_label.place(x=185,y=500)

if __name__=="__main__":   
    root=Tk()
    obj=Developer(root)
    root.mainloop()
   