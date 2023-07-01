from tkinter import *
from tkinter import ttk        #for stylish toolkit
from PIL import Image,ImageTk    # for importing images
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):   #for constructor call
        self.root=root   # root intialization
        self.root.geometry("1530x790+0+0")   #0,0 for starting from x=0,y=0
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")



        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red") 
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        img_top=Image.open(r"College Imges\riya.webp")   # r for backslash forwarded into frontslash
        img_top=img_top.resize((1530,325),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)

        #button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",35,"bold"),bg="Red",fg="white")
        b1_1.place(x=0,y=380,width=1530,height=60)


        img_bottom=Image.open(r"College Imges\riju.jpg")   # r for backslash forwarded into frontslash
        img_bottom=img_bottom.resize((1530,325),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)


    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]  # list comprehensing

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')  # Gray scale image
            imageNp=np.array(img,'uint8')  #uint is a datatype
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13   # after press enter window will close
        ids=np.array(ids)   # use numpy because of RMA conversion

        #=====================Train the classifier and save=========================
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Datasets Completed!!!",parent=self.root)
        

if __name__=="__main__":   
    root=Tk()
    obj=Train(root)
    root.mainloop()