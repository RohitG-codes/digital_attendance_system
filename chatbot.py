from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk

class chatbot:
    def __init__(self,root):
        self.root=root
        self.root.title('CHATBOT')
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_func)
        self.root.wm_iconbitmap("face.ico")

    

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()

        img_chat=Image.open(r'College Imges\bot.jpg')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="CHAT WITH ME",font=('arial',30,'bold'),fg='green',bg='white')
        title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=38,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text='Send >>',command=self.send,font=('arial',15,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text='Clear Data',command=self.clear,font=('arial',15,'bold'),width=8,bg='red',fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)

    # functions

    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')



    def send(self):
        send='\t\t\t'+'You: '+ self.entry.get()
        self.text.insert(END,"\n"+send)
        self.text.yview(END)

        if(self.entry.get())=='':
            self.msg='please Enter Some Input'
            self.label_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')
        if(self.entry.get())=='hello':
            self.text.insert(END,'\n\n'+'Bot : Hi.')
        
        elif(self.entry.get())=='hi':
            self.text.insert(END,'\n\n'+'Bot : Hello.')

        elif(self.entry.get())=='how are You?':
            self.text.insert(END,'\n\n'+'Bot : Fine and You.')
        
        elif(self.entry.get())=='fantastic':
            self.text.insert(END,'\n\n'+'Bot : Nice to Hear that.')

        elif(self.entry.get())=='who created you?':
            self.text.insert(END,'\n\n'+'Bot : My Boss, Mr. Rohit Gupta Created me using Python programming language.')

        elif(self.entry.get())=='what is your name?':
            self.text.insert(END,'\n\n'+'Bot : My name is rglite.')

        elif(self.entry.get())=='can you speak bengali?':
            self.text.insert(END,'\n\n'+"Bot : I'm still learning it....")
        
        elif(self.entry.get())=='are you a robot?':
            self.text.insert(END,'\n\n'+'Bot : Yes I am a robot, but I am a good one. Let me prove it. How can I help you?')
        
        elif(self.entry.get())=='what is python programming language':
            self.text.insert(END,'\n\n'+"Bot : Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems.")
        
        elif(self.entry.get())=='ok, bye':
            self.text.insert(END,'\n\n'+'Bot : Ok, Thank You, Please Visit Again.')

        elif(self.entry.get())=='what is machine learning?':
            self.text.insert(END,'\n\n'+'Bot : Machine learning is a subfield of artificial intelligence, which is broadly defined as the capability of a machine to imitate intelligent human behavior. Artificial intelligence systems are used to perform complex tasks in a way that is similar to how humans solve problems.')
        
        elif(self.entry.get())=='what is face recognition?':
            self.text.insert(END,'\n\n'+'Bot : It works by identifying and measuring facial features in an image. Facial recognition can identify human faces in images or videos, determine if the face in two images belongs to the same person, or search for a face among a large collection of existing images.')

        elif(self.entry.get())=='what is digital attendance system?':
            self.text.insert(END,'\n\n'+'Bot : The Digital Attendance App (DAA) is an application that tracks student attendance quickly, safely, and efficiently to support learning and school re-entry, thus providing insight on out-of-school children.')

        else:
            self.text.insert(END,'\n\n'"Bot : Sorry! I didn't get it")
        
        






if __name__=="__main__":
    root=Tk()
    obj=chatbot(root)
    root.mainloop()