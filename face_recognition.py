from tkinter import *
from tkinter import ttk        #for stylish toolkit
from PIL import Image,ImageTk    # for importing images
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np

dt=''

class Face_Recognition:
    def __init__(self,root):   #for constructor call
        self.root=root   # root intialization
        self.root.geometry("1530x790+0+0")   #0,0 for starting from x=0,y=0
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # self.var_atten_subject=StringVar()


        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green") 
        title_lbl.place(x=0,y=0,width=1530,height=45) 

        # 1st image
        img_top=Image.open(r"College Imges\fare.jpg")   # r for backslash forwarded into frontslash
        img_top=img_top.resize((650,700),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        # 2nd image
        img_bottom=Image.open(r"College Imges\reg.webp")   # r for backslash forwarded into frontslash
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)

        # button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=365,y=615,width=200,height=40)

        #subject
        self.subject_status1=ttk.Combobox(f_lbl,width=22,font="comicsansns 11 bold",state="readonly")
        self.subject_status1["values"]=('choose subject','PYTHON',"JAVA","AI/ML","MYSQL","HTML","JAVASCRIPT","ANGULAR","TIDAL","WEBRTC")
        self.subject_status1.current(0)
        self.subject_status1.place(x=365,y=655,width=200,height=40)
    
    #=====================attendance=========================
    def mark_attendance(self,r,n,d):
        global dt
        with open("attendance_report/attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((','))
                name_list.append(entry[0])
            if((r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime('%d/%m/%Y')
                dtString=now.strftime("%H:%M:%S")
                dt=dtString                
                f.writelines(f"\n{r},{n},{d},{dtString},{d1},Present,{self.subject_status1.get()}")
                
                
    #=====================face recognition===================

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                    
                conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dept from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)





                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img


        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml") 

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__=="__main__":   
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()