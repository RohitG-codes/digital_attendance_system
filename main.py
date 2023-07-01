from tkinter import *
from tkinter import ttk        #for stylish toolkit
from PIL import Image,ImageTk    # for importing images
from student import Student
import os
import tkinter
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime
from chatbot import chatbot



class Face_Recognition_System:
    def __init__(self,root):   #for constructor call
        self.root=root   # root intialization
        self.root.geometry("1530x790+0+0")   #0,0 for starting from x=0,y=0
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        # First Image
        img=Image.open(r"College Imges\gate.png")   # r for backslash forwarded into frontslash
        img=img.resize((500,130),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)      #for apply it into window

        
        # Second Image
        img1=Image.open(r"College Imges\nitmas.jpeg")   # r for backslash forwarded into frontslash
        img1=img1.resize((500,130),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)    

 
        # Third Image
        img2=Image.open(r"College Imges\Tnu.jpg")   # r for backslash forwarded into frontslash
        img2=img2.resize((500,130),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)   


        # Background Image
        img3=Image.open(r"College Imges\bg_image.jpg")   # r for backslash forwarded into frontslash
        img3=img3.resize((1530,710),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710) 


        # Title
        title_lbl=Label(bg_img,text="DIGITAL ATTENDENCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red") 
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        # time

        def time():
            stringsa=strftime('%H:%M:%S %p')
            lbll.config(text= stringsa)
            lbll.after(1000,time)

        lbll=Label(title_lbl,font=("times new roman",14,"bold"),background='white',foreground='black')
        lbll.place(x=100,y=0,width=110,height=50)
        time()

        # date
        def dates():
            now = datetime.now() # current date and time
            stringsas = now.strftime("%d/%m/%Y")
            lbl.config(text= stringsas)
            lbl.after(1000,dates)
            
        lbl=Label(title_lbl,font=("times new roman",14,"bold"),background='white',foreground='black')
        lbl.place(x=1300,y=0,width=110,height=50)
        dates()

        # Student Button
        img4=Image.open(r"College Imges\stud.jpg")   # r for backslash forwarded into frontslash
        img4=img4.resize((220,220),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        # Detect Face Button
        img5=Image.open(r"College Imges\fare.jpg")   # r for backslash forwarded into frontslash
        img5=img5.resize((220,220),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        # Attendence Button
        img6=Image.open(r"College Imges\attendence.jpg")   # r for backslash forwarded into frontslash
        img6=img6.resize((220,220),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        # # Help Desk Button
        # img7=Image.open(r"College Imges\help.jpg")   # r for backslash forwarded into frontslash
        # img7=img7.resize((220,220),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        # self.photoimg7=ImageTk.PhotoImage(img7)

        # b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        # b1.place(x=1100,y=100,width=220,height=220)

        # b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        # b1_1.place(x=1100,y=300,width=220,height=40)

        # chatbot Button
        img7=Image.open(r"College Imges\bot1.jpg")   # r for backslash forwarded into frontslash
        img7=img7.resize((220,220),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chat_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Chatbot",cursor="hand2",command=self.chat_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        # Train face button
        img8=Image.open(r"College Imges\train.png")   # r for backslash forwarded into frontslash
        img8=img8.resize((220,220),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        # Photos Button
        img9=Image.open(r"College Imges\photos.jpg")   # r for backslash forwarded into frontslash
        img9=img9.resize((220,220),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        # Developer button
        img10=Image.open(r"College Imges\download (2).jpg")   # r for backslash forwarded into frontslash
        img10=img10.resize((220,220),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data,)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        # Exit button
        img11=Image.open(r"College Imges\exit.jpg")   # r for backslash forwarded into frontslash
        img11=img11.resize((220,220),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Iexit,)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.Iexit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def Iexit(self):
        self.Iexit=tkinter.messagebox.askyesno("Face recognition","Are you Sure You Want to Exit ?",parent=self.root)
        if self.Iexit>0:
            self.root.destroy()
        else:
            return

        #============================Functions buttons==============================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
 
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    # def help_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Help(self.new_window)

    def chat_data(self):
        self.new_window=Toplevel(self.root)
        self.app=chatbot(self.new_window)


    



if __name__=="__main__":   
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()


        