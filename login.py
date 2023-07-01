from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System


def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title('Login')
        self.root.geometry('1550x800+0+0')
        self.root.wm_iconbitmap("face.ico")
        
        self.bg=ImageTk.PhotoImage(file=r"College Imges\222.jpg")

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r'C:\Users\Lenovo\Documents\Final_Year_Project\College Imges\0000.jpg')
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.phtotimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.phtotimg1,bg='black',borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("time new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=105)

        #labels

        username_lbl=Label(frame,text="Username",font=("time new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=70,y=155)

        self.textuser=ttk.Entry(frame,font=("time new roman",15))
        self.textuser.place(x=40,y=185,width=270)

        password_lbl=Label(frame,text="Password",font=("time new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=70,y=230)

        self.textpass=ttk.Entry(frame,font=("time new roman",15),show="*")
        self.textpass.place(x=40,y=260,width=270)

        #icon images

        img2=Image.open(r'C:\Users\Lenovo\Documents\Final_Year_Project\College Imges\151.jpg')
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.phtotimg2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.phtotimg2,bg='black',borderwidth=0)
        lblimg1.place(x=650,y=326,width=25,height=25)
        
        img3=Image.open(r'C:\Users\Lenovo\Documents\Final_Year_Project\College Imges\1915773.png')
        img3=img3.resize((20,20),Image.ANTIALIAS)
        self.phtotimg3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.phtotimg3,bg='black',borderwidth=0)
        lblimg1.place(x=650,y=405,width=21,height=21)

        # buttons

        login_button=Button(frame,text="Login",command=self.login,font=("time new roman",15,"bold"),bd=3,activeforeground="white",activebackground="red",relief=RIDGE,fg="white",bg="red")
        login_button.place(x=110,y=315,width=120,height=35)

        register_button=Button(frame,text="New User",command=self.register_window,font=("time new roman",10,"bold"),borderwidth=0,activeforeground="white",activebackground="black",fg="white",bg="black")
        register_button.place(x=0,y=370,width=150)

        forgot_button=Button(frame,text="Forgot Password ?",command=self.forgot_pass,font=("time new roman",10,"bold"),borderwidth=0,activeforeground="white",activebackground="black",fg="white",bg="black")
        forgot_button.place(x=23,y=395,width=160)
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=register(self.new_window)




    def login(self):
        if self.textuser.get()=='' or self.textpass.get()=='':
            messagebox.showerror('Error','All Fields Are Required')
        # elif self.textuser.get()=='Rohit' and self.textpass.get()=='Gupta':
        #     messagebox.showinfo('Success','Welcome To Digital Attendance System')
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="login")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from mydata where email=%s and password=%s",(
                                                                                            self.textuser.get(),
                                                                                            self.textpass.get()              
                                                                                        ))
                row=my_cursor.fetchone()
                if row== None:
                    messagebox.showerror('Error','Invalid Username And Password')
                else:
                    open_main=messagebox.askyesno("Access","Are You an Admin ?")
                    if open_main>0:
                        self.new_window=Toplevel(self.root)
                        self.app=Face_Recognition_System(self.new_window)
                    else:
                        if not open_main:
                            return
                conn.commit()
                conn.close()



    def reset_pass(self):
        if self.txt_security_q.get()=="Select Your Question":
            messagebox.showerror("Error",'Please Select The security Question',parent=self.root2)
        elif self.txtsecurity_a.get()=='':
            messagebox.showerror("Error",'Please Enter The security Answer',parent=self.root2)
        elif self.txt_new_password.get()=='':
            messagebox.showerror("Error",'Please Enter The New Password',parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="login")
            my_cursor=conn.cursor()
            query=('Select * from mydata where email=%s and securityQ=%s and securityA=%s')
            value=(self.textuser.get(),self.txt_security_q.get(),self.txtsecurity_a.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Please Enter The Correct Answer',parent=self.root2)
            else:
                query1=("update mydata set password=%s where email=%s")
                value1=(self.txt_new_password.get(),self.textuser.get(),)
                my_cursor.execute(query1,value1)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password Has Been Reset",parent=self.root2)
                self.root2.destroy()



    def forgot_pass(self):
        if self.textuser.get()=='':
            messagebox.showerror('Error','Please Enter Your Email ID To Reset Your Password')
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="login")
            my_cursor=conn.cursor()
            query=("select * from mydata where email=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Please Enter Your Username')
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("time new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)
                
                security_q=Label(self.root2,text="Security Question",font=("time new roman",15,"bold"),bg='white',fg='black')
                security_q.place(x=50,y=80)

                self.txt_security_q=ttk.Combobox(self.root2,font=("time new roman",13),state='readonly')
                self.txt_security_q['values']=("Select Your Question","What is the name of your favorite pet ?","What is your mother's maiden name ?","In what city were you born ?","What high school did you attend ?","What was your favorite food as a child ?")
                self.txt_security_q.place(x=50,y=110,width=200)
                self.txt_security_q.current(0)

                security_a=Label(self.root2,text="Security Answer",font=("time new roman",15,"bold"),bg='white',fg='black')
                security_a.place(x=50,y=150)

                self.txtsecurity_a=ttk.Entry(self.root2,font=("time new roman",15))
                self.txtsecurity_a.place(x=50,y=180,width=200)

                new_password=Label(self.root2,text="New Password",font=("time new roman",15,"bold"),bg='white',fg='black')
                new_password.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("time new roman",15))
                self.txt_new_password.place(x=50,y=250,width=200)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("time new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=120,y=310)






class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        # variables

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        # background image
        self.bg=ImageTk.PhotoImage(file=r"College Imges\900.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        # left image
        self.bg1=ImageTk.PhotoImage(file=r"College Imges\00.png")
        lbl_left=Label(self.root,image=self.bg1)
        lbl_left.place(x=50,y=100,width=470,height=550)

        # main frame

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        # lables 

        register_lbl=Label(frame,text='Register Here',font=("time new roman",25,"bold"),fg='darkgreen',bg='white')
        register_lbl.place(x=20,y=20)

        # row 1
        fname=Label(frame,text="First Name",font=("time new roman",15,"bold"),bg='white',fg='black')
        fname.place(x=50,y=100)

        self.txt_fname=ttk.Entry(frame,textvariable=self.var_fname,font=("time new roman",15))
        self.txt_fname.place(x=50,y=135,width=200)

        lname=Label(frame,text="Last Name",font=("time new roman",15,"bold"),bg='white',fg='black')
        lname.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("time new roman",15))
        self.txt_lname.place(x=370,y=135,width=200)

        # row 2
        contact=Label(frame,text="Contact Number",font=("time new roman",15,"bold"),bg='white',fg='black')
        contact.place(x=50,y=190)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("time new roman",15))
        self.txt_contact.place(x=50,y=223,width=200)

        email=Label(frame,text="Email ID",font=("time new roman",15,"bold"),bg='white',fg='black')
        email.place(x=370,y=190)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("time new roman",15))
        self.txt_email.place(x=370,y=223,width=200)

        # row 3
        security_q=Label(frame,text="Security Question",font=("time new roman",15,"bold"),bg='white',fg='black')
        security_q.place(x=50,y=269)

        self.txt_security_q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("time new roman",13),state='readonly')
        self.txt_security_q['values']=("Select Your Question","What is the name of your favorite pet ?","What is your mother's maiden name ?","In what city were you born ?","What high school did you attend ?","What was your favorite food as a child ?")
        self.txt_security_q.place(x=50,y=305,width=200)
        self.txt_security_q.current(0)

        security_a=Label(frame,text="Security Answer",font=("time new roman",15,"bold"),bg='white',fg='black')
        security_a.place(x=370,y=269)

        self.txtsecurity_a=ttk.Entry(frame,textvariable=self.var_securityA,font=("time new roman",15))
        self.txtsecurity_a.place(x=370,y=305,width=200)
         
        # row 4
        password=Label(frame,text="password",font=("time new roman",15,"bold"),bg='white',fg='black')
        password.place(x=50,y=342)

        self.txt_password=ttk.Entry(frame,textvariable=self.var_pass,font=("time new roman",15))
        self.txt_password.place(x=50,y=374,width=200)

        confirm_password=Label(frame,text="Confirm Password",font=("time new roman",15,"bold"),bg='white',fg='black')
        confirm_password.place(x=370,y=342)

        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confpass,font=("time new roman",15))
        self.txt_confirm_password.place(x=370,y=374,width=200)

        # checkbuttons

        self.var_check=IntVar()
        checkbut=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("time new roman",13,"bold"),onvalue=1,offvalue=0)
        checkbut.place(x=50,y=425)

        # image button
 
        img1=Image.open(r"College Imges\s.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimg1,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=220,y=470,width=200)


    # functions

    def register_data(self):
        if self.var_fname.get()=='' or self.var_email.get()=='' or self.var_securityQ.get()=='Select Your Question':
            messagebox.showerror('Error','All Fields Are Required',parent=self.root)            
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror('Error','Password And Confirm Password Must Be Same',parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror('Error','Please Agree The Terms And Conditions',parent=self.root)
        else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Rohit@12345678",database="login")
                my_cursor=conn.cursor()
                query=("select * from mydata where email=%s")
                value=(self.var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row != None:
                    messagebox.showerror('Error','User Already Exist')
                else:

                    my_cursor.execute("insert into mydata values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.var_fname.get(),
                                                                                                self.var_lname.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_securityQ.get(),
                                                                                                self.var_securityA.get(),
                                                                                                self.var_pass.get()
                                                                                            ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Registration Successful",parent=self.root)
                self.root.destroy()
            


if __name__=="__main__":
    main()


        