from tkinter import *
from tkinter import ttk        #for stylish toolkit
from PIL import Image,ImageTk    # for importing images
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]

class Attendance:
    def __init__(self,root):   #for constructor call
        self.root=root   # root intialization
        self.root.geometry("1530x790+0+0")   #0,0 for starting from x=0,y=0
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")


        # variables

        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        self.var_atten_subject=StringVar()

        # First Image
        img=Image.open(r"College Imges\student_fa.jpg")   # r for backslash forwarded into frontslash
        img=img.resize((800,200),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=800,height=200)      #for apply it into window

        
        # Second Image
        img1=Image.open(r"College Imges\student_f.jpg")   # r for backslash forwarded into frontslash
        img1=img1.resize((800,200),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg1=ImageTk.PhotoImage(img1)

        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=800,y=0,width=800,height=200) 
        
        # Background Image
        img3=Image.open(r"College Imges\bg_image.jpg")   # r for backslash forwarded into frontslash
        img3=img3.resize((1530,710),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1530,height=710) 

        # Title
        title_lbl=Label(bg_img,text=" ATTENDANCE SHEET",font=("times new roman",35,"bold"),bg="white",fg="darkblue") 
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2,bg="white")   # Frame creation with border 2, main is the frame name
        main_frame.place(x=10,y=55,width=1500,height=600)

        # Left side label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))   # relief for border style
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"College Imges\left_img.jpg")   # r for backslash forwarded into frontslash
        img_left=img_left.resize((720,130),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")   # Frame creation with border 2, main is the frame name
        left_inside_frame.place(x=3,y=135,width=720,height=370)

        # labels and entries

        # roll
        rollLabel=Label(left_inside_frame,text="Roll:",bg="white",font="comicsansns 11 bold")
        rollLabel.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_roll,font="comicsansns 11 bold")
        atten_roll.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #name
        nameLabel=Label(left_inside_frame,text="Name:",bg="white",font="comicsansns 11 bold")
        nameLabel.grid(row=0,column=2,padx=4,pady=8)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_name,font="comicsansns 11 bold")
        atten_name.grid(row=0,column=3,pady=8)

        #department
        depLabel=Label(left_inside_frame,text="Department:",bg="white",font="comicsansns 11 bold")
        depLabel.grid(row=1,column=0)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_dep,font="comicsansns 11 bold")
        atten_dep.grid(row=1,column=1,pady=8)

        #time
        timeLabel=Label(left_inside_frame,text="Time:",bg="white",font="comicsansns 11 bold")
        timeLabel.grid(row=1,column=2)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_time,font="comicsansns 11 bold")
        atten_time.grid(row=1,column=3,pady=8)

        #date
        dateLabel=Label(left_inside_frame,text="Date:",bg="white",font="comicsansns 11 bold")
        dateLabel.grid(row=2,column=0)

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_date,font="comicsansns 11 bold")
        atten_date.grid(row=2,column=1,pady=8)

        #attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",bg="white",font="comicsansns 11 bold")
        attendanceLabel.grid(row=2,column=2)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=('Status',"Present","Absent")
        self.atten_status.grid(row=2,column=3,pady=8)
        self.atten_status.current(0)

        #subject
        subjectLabel=Label(left_inside_frame,text="Subject:",bg="white",font="comicsansns 11 bold")
        subjectLabel.grid(row=3,column=0)

        atten_subject=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_subject,font="comicsansns 11 bold")
        atten_subject.grid(row=3,column=1,pady=8)


        #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=715,height=35)


        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=25,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCSV,width=26,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=25,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        # Right side label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))   # relief for border style
        Right_frame.place(x=750,y=10,width=720,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=700,height=455)

        # scroll bar and table

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("roll","name","department","time","date","attendance","subject"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")
        self.AttendanceReportTable.heading("subject",text="Subject")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        self.AttendanceReportTable.column("subject",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    # fetch data
    
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    
    # import csv

    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open (fln) as myfile :
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export csv

    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open (fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                dsd= messagebox.showinfo("data export","Your Data Expotrted to " + os.path.basename(fln)+ " Successfully",parent=self.root)
                if dsd == "ok" :
                    self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())              
                    f = open("attendance_report/attendance.csv","r+") 
                    # absolute file positioning
                    f.seek(0)        
                    # to erase all data 
                    f.truncate() 
                else:
                    pass
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_roll.set(rows[0])
        self.var_atten_name.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_attendance.set(rows[5])
        self.var_atten_subject.set(rows[6])



    def reset_data(self):
        self.var_atten_roll.set(" ")
        self.var_atten_name.set(" ")
        self.var_atten_dep.set(" ")
        self.var_atten_time.set(" ")
        self.var_atten_date.set(" ")
        self.var_atten_attendance.set(" ")       
        self.var_atten_subject.set(" ")
    

    

 




        







if __name__=="__main__":   
    root=Tk()
    obj=Attendance(root)
    root.mainloop()