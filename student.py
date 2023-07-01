from tkinter import *
from tkinter import ttk        #for stylish toolkit
from PIL import Image,ImageTk    # for importing images
from tkinter import messagebox
import mysql.connector
import cv2
import re
import pyttsx3


mydata=[]



class Student:
    def __init__(self,root):   #for constructor call
        self.root=root   # root intialization
        self.root.geometry("1530x790+0+0")   #0,0 for starting from x=0,y=0
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")



        # =============== variables ==============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        # Text To Speech

        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[0].id) #1 for female voice and 0 for male voice

        # First Image
        img=Image.open(r"College Imges\student_face.jpg")   # r for backslash forwarded into frontslash
        img=img.resize((500,130),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)      #for apply it into window

        
        # Second Image
        img1=Image.open(r"College Imges\student_f.jpg")   # r for backslash forwarded into frontslash
        img1=img1.resize((500,130),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=550,height=130)    

 
        # Third Image
        img2=Image.open(r"College Imges\student_fa.jpg")   # r for backslash forwarded into frontslash
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
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkblue") 
        title_lbl.place(x=0,y=0,width=1530,height=45) 


        main_frame=Frame(bg_img,bd=2,bg="white")   # Frame creation with border 2, main is the frame name
        main_frame.place(x=10,y=55,width=1500,height=600)

        # Left side label frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))   # relief for border style
        left_frame.place(x=10,y=10,width=730,height=580)


        img_left=Image.open(r"College Imges\left_img.jpg")   # r for backslash forwarded into frontslash
        img_left=img_left.resize((720,130),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg2)
        f_lbl.place(x=5,y=0,width=720,height=130)
    
        # Current Course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))   # relief for border style
        current_course_frame.place(x=5,y=135,width=720,height=120)
        
        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=25,state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechanical","ECE","Chemical","Pysics","Chemistry","Math")   # for dropdown list
        dep_combo.current(0)  # for showing current Department
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=25,state="readonly")
        course_combo["values"]=("Select Course","B.SC","BE","B.TECH","M.SC","ME","M.TECH")   # for dropdown list
        course_combo.current(0)  # for showing current Department
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=25,state="readonly")
        year_combo["values"]=("Select Year","2018-19","2019-20","2020-21","2021-22","2022-23","2023-24")   # for dropdown list
        year_combo.current(0)  # for showing current Department
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=25,state="readonly")
        semester_combo["values"]=("Select Semester","Semester-I","Semester-II","Semester-III","Semester-IV","Semester-V","Semester-VI","Semester-VII","Semester-VII")   # for dropdown list
        semester_combo.current(0)  # for showing current Department
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        # Class Student Information
        class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Student Information",font=("times new roman",12,"bold"))   # relief for border style
        class_Student_frame.place(x=5,y=260,width=720,height=295)

        # student id
        studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.va_std_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        
        validate_id=self.root.register(self.checkid)
        studentId_entry.config(validate='key',validatecommand=(validate_id,'%P'))

        # student name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        validate_name=self.root.register(self.checkname)
        studentName_entry.config(validate='key',validatecommand=(validate_name,'%P'))

        # class division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=18,state="readonly")
        div_combo["values"]=("Select Division","A","B","C","D")   # for dropdown list
        div_combo.current(0)  # for showing current value
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll no
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        validate_roll=self.root.register(self.checkroll)
        roll_no_entry.config(validate='key',validatecommand=(validate_roll,'%P'))

        # Gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")   # for dropdown list
        gender_combo.current(0)  # for showing current gender
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # DOB
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        dob_entry.insert(0,"yyyy-mm-dd")


        # Email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #  for Placeholder : email_entry.insert(0,"Enter any Text")

        # Phone No
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)


        validate_phoneno=self.root.register(self.checkcontact)
        phone_entry.config(validate='key',validatecommand=(validate_phoneno,'%P'))


        # Address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        # Teacher name
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        validate_namee=self.root.register(self.checkname)
        teacher_entry.config(validate='key',validatecommand=(validate_namee,'%P'))
            
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)



        #button frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)


        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text=" Take a Photo Sample ",width=78,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)


         # Right side label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))   # relief for border style
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"College Imges\stud.jpg")   # r for backslash forwarded into frontslash
        img_right=img_left.resize((720,130),Image.ANTIALIAS)   #ANTIALIAS->convert higher level image into lower level
        self.photoimg_left=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image=self.photoimg2)
        f_lbl.place(x=5,y=0,width=720,height=130)


        # ========== Search System ============

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))   # relief for border style
        Search_frame.place(x=5,y=135,width=705,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),width=15,state="readonly")
        search_combo["values"]=("Select","Roll_No","Phone_No")   # for dropdown list
        search_combo.current(0)  # for showing current Department
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)


        # =============== table frame ===============
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)   # relief for border style
        table_frame.place(x=5,y=210,width=705,height=350)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # validation check

    def checkname(self,name):
        for char in name:
            if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
                self.engine.say('Please Enter A Valid Name')
                self.engine.runAndWait()
                messagebox.showerror('Invalid Name','Please Enter A Valid Name' ,parent=self.root)
                return False
        return True
        

    def checkroll(self,roll):
        if roll.isdigit():
            return True
        if roll=='':
            return True
        else:
            self.engine.say('Please Enter A Valid Roll Number')
            self.engine.runAndWait()
            messagebox.showerror("Invalid Roll Number","Please Enter A Valid Roll Number",parent=self.root)     
            return False

    def checkid(self,id):
        if id.isdigit():
            return True
        if id=='':
            return True
        else:
            self.engine.say('Please Enter A Valid ID')
            self.engine.runAndWait()
            messagebox.showerror("Invalid Roll Number","Please Enter A Valid ID",parent=self.root)     
            return False

    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            self.engine.say('Please Enter Your Phone Number')
            self.engine.runAndWait()
            messagebox.showerror("Invalid Phone Number","Please Enter Your Phone Number",parent=self.root)
            return False

    
    # ============== function declaration ===============

    def add_data(self):
        if self.var_std_name.get()=='':
            self.engine.say('Please Enter Your Name')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter Your Name',parent=self.root)

        elif self.var_email.get()=='':
            self.engine.say('Please Enter Your email')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter Your email',parent=self.root)

        elif self.var_phone.get()=='' or len(self.var_phone.get())!=10:
            self.engine.say('Please Enter Your Valid Phone Number')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter Your Valid Phone Number',parent=self.root)

        elif self.var_roll.get()=='':
            self.engine.say('Please Enter Your Roll Number')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter Your Roll Number',parent=self.root)

        elif self.var_dob.get()=='' or self.var_dob.get()=='yyyy-mm-dd' :
            self.engine.say('Please Enter Your Date Of Birth')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter Your Date Of Birth',parent=self.root)

        elif self.var_address.get()=='' :
            self.engine.say('Please Enter Your Address')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter Your Address',parent=self.root)

        elif self.var_teacher.get()=='' :
            self.engine.say('Please Enter Your Teacher Name')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter Your Teacher Name',parent=self.root)

        elif self.va_std_id.get()=='' :
            self.engine.say('Please Enter Your Student ID')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Enter Your Student ID',parent=self.root)


        elif self.var_semester.get()=='' or self.var_semester.get()=='Select Semester':
            self.engine.say('Please Select Your Semester')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Select Your Semester',parent=self.root)

        elif self.var_course.get()=='' or self.var_course.get()=='Select Course':
            self.engine.say('Please Select Your Course')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Select Your Course',parent=self.root)

        elif self.var_year.get()=='' or self.var_year.get()=='Select Year':
            self.engine.say('Please Select Your Year')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Select Your Year',parent=self.root)

        elif self.var_dep.get()=='' or self.var_dep.get()=='Select Department':
            self.engine.say('Please Select Your Department')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Select Your Department',parent=self.root)

        elif self.var_div.get()=='' or self.var_div.get()=='Select Division' :
            self.engine.say('Please Select Your Division')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Select Your Division',parent=self.root)

        elif self.var_gender.get()=='' or self.var_gender.get()=='Select Gender':
            self.engine.say('Please Select Your Gender')
            self.engine.runAndWait()
            messagebox.showerror('Error','Please Select Your Gender',parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_dep.get(),
                                                                                                self.var_course.get(),
                                                                                                self.var_year.get(),
                                                                                                self.var_semester.get(),
                                                                                                self.va_std_id.get(),
                                                                                                self.var_std_name.get(),
                                                                                                self.var_div.get(),
                                                                                                self.var_roll.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_dob.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_phone.get(),
                                                                                                self.var_address.get(),
                                                                                                self.var_teacher.get(),
                                                                                                self.var_radio1.get()
                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



    #=========== fetch data=============
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()


        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #================get cursor===================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])


    #======================update function=====================
    def update_data(self):
        if  self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dept=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                            
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_course.get(), 
                                                                                                                                                                        self.var_year.get(), 
                                                                                                                                                                        self.var_semester.get(), 
                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.va_std_id.get()
                                                                                                                                                                        
                                                                                                                                                                                   
                                                                                                                                                                      ))
 
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #====================delete function=============================
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student details",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="face_recognition")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    
    # Reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #===================Generate dataset or take a photo sample===========================
    def generate_dataset(self):
        if  self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All Field are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dept=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                            
                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                        self.var_course.get(), 
                                                                                                                                                                        self.var_year.get(), 
                                                                                                                                                                        self.var_semester.get(), 
                                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                        self.var_teacher.get(),
                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                        self.va_std_id.get()==id+1
                                                                                                                                                                    ))

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()    


                #=========Load predefined data on facefrontals from opencv==========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor=1.3
                    #Minimum neighbour=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result","Generating datasets completed !!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)




                                                                                                                                                                                   




if __name__=="__main__":   
    root=Tk()
    obj=Student(root)
    root.mainloop()
   