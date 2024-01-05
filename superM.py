from tkinter import *
from tkinter import messagebox
import webbrowser
import os
import sys


class Super1:
    def __init__(self, pro):
        self.pro=pro
        self.pro.geometry('800x450+280+50')# size frame
        self.pro.resizable(FALSE,FALSE) # unlook size
        self.pro.title("PYTHON") # title
        self.pro.iconbitmap('store-64.ico') # icon
        title = Label(pro,text='towfic sinno',fg='gold',bg='black',font=('tajawal',16,'bold'))
        title.pack(fill=X) # pack to show # fill to filling all X
        self.u1='https://www.minecraft-crafting.net/'
        self.u2='https://www.chunkbase.com/apps/village-finder#-6309561481274458664'
        self.u3='https://aternos.org/:en/'
        self.queue = []
        self.namo = StringVar()
        self.passo = StringVar()
        F1 = Frame(pro,width=230,height=420,bg='#0b2f3a')
        F1.place(x=570,y=30)
        Title1 = Label(F1,text='مشروع سوبر ماركت',fg='white',bg='#0b2f3a',font=('tajawal',12,'bold'))
        Title1.place(x=42,y=10)
        Title2 = Label(F1,text='المطور توفيق سنو',fg='white',bg='#0b2f3a',font=('tajawal',12,'bold'))
        Title2.place(x=42,y=40)
        Title3 = Label(F1,text='facbook',fg='white',bg='#0b2f3a',font=('tajawal',12,'bold'))
        Title3.place(x=57,y=70)

        B1=Button(F1,text='crafting',width=20,height=1, fg='black',bg='Gold',font=('tajawal',11,'bold'),command=self.Open1)
        B1.place(x=15,y=180)
        B2=Button(F1,text='Seed',width=20,height=1, fg='black',bg='Gold',font=('tajawal',11,'bold'),command=self.Open2)
        B2.place(x=15,y=220)
        B3=Button(F1,text='aternos',width=20,height=1, fg='black',bg='Gold',font=('tajawal',11,'bold'),command=self.Open3)
        B3.place(x=15,y=260)
        B4=Button(F1,text='About',width=20,height=1, fg='black',bg='Gold',font=('tajawal',11,'bold'),command=self.about)
        B4.place(x=15,y=300)          
        B5=Button(F1,text='Info',width=20,height=1, fg='black',bg='Gold',font=('tajawal',11,'bold'),command=self.Info)
        B5.place(x=15,y=340)
        B6=Button(F1,text='Close',width=20,height=1, fg='black',bg='Gold',font=('tajawal',11,'bold'),command=quit)
        B6.place(x=15,y=380)

        self.photo = PhotoImage(file='TMS_free-file.png')
        imo =Label(pro,image=self.photo)
        imo.place(x=180,y=35)
        F2 =  Frame(pro,width=570,height=120,bg='#0b2f3a')
        F2.place(x=0,y=350)                  
        self.ph1 = PhotoImage(file='user-64-bg=#0b2f3a.png')
        imo1=Label(F2,image=self.ph1)
        imo1.place(x=2,y=10)

        L1 = Label(F2,text='user_name',fg='Gold',bg='#0b2f3a',font=('tajawal',11,'bold'))
        L1.place(x=108,y=2)
        E1 = Entry(F2,textvariable=self.namo,fg='black')
        E1.place(x=190,y=2)
        L2 = Label(F2,text='Password',fg='Gold',bg='#0b2f3a',font=('tajawal',11,'bold'))
        L2.place(x=108,y=50)
        E2 = Entry(F2,textvariable=self.passo,fg='black')
        E2.place(x=190,y=50)
        Bl=Button(F2,text='Login',width=20,height=1, fg='black',bg='Gold',font=('tajawal',11,'bold'),command=self.Login)
        Bl.place(x=350,y=25)
        Br=Button(F2,text='Join',width=20,height=1, fg='Gold',bg='#0b2f3a',font=('tajawal',11,'bold'),command=self.Join)
        Br.place(x=350,y=55)
    def  Open1(self):# to dala
        webbrowser.open_new(self.u1)
    def  Open2(self):
        webbrowser.open_new(self.u2)
    def  Open3(self):
        webbrowser.open_new(self.u3)    
    def about(self):
        messagebox.showinfo('About','This is a program made by Towfic Sinno') # box massage  (1.'title', 2. 'massage')
        # box=Toplevel()
        # box.geometry('250x250')
        # l1=Label(box,text="This is a program made by Towfic Sinno.",bg='white').pack()
        # b1=Button(box,text="OK",command=box.destroy).place(x=0,y=50,width=50,height=20)
    def Info(self):
      messagebox.showinfo('Info','The App Store is a digital distribution platform, developed and maintained by Apple Inc., for mobile apps on its iOS operating system')  
    def Login(self):
        user = self.namo.get()
        passw= self.passo.get()
        for customer in self.queue:
            if (user == customer["name"] and passw == customer["pass"] ):   
                self.close_current_window()
                from super import Super
                messagebox.showinfo('Join','Thank You For Your Registration!')
        
            elif (user != customer["name"]):
                messagebox.showerror('Error','User Not Found!')
            elif (passw != customer["pass"]):
                messagebox.showerror('Error','Password Wrong!')
            elif(user != customer["name"] and passw != customer["pass"]):
                messagebox.showerror('Error','Wrong Username and Password!')      
            else:
              messagebox.showwarning('Warning','Please Fill All Fields!')
    def Join(self):
        user = self.namo.get()
        passw= self.passo.get()
        self.queue.append({"name": user, "pass":passw})
        print(self.queue)
        #  close_current_window()
        #  from super import Super
        messagebox.showinfo('Join','Thank You For Your Registration!')  
    def close_current_window(self):
        self.pro.destroy()
    def dequeue(self):
            if len(self.queue) < 1:
                return None
            return self.queue.pop(0)
    def size(self):
        return len(self.queue)    
pro = Tk()
ee =Super1(pro)
pro.mainloop()
#hi 


