import queue
import sqlite3
from sqlite3 import Error
from tkinter import *
from tkinter import messagebox
import math
import os
import sys
import random
from collections import deque
class Super:  
    def __init__(self, root):
        self.root = root
        self.root.geometry('1300x700+30+10')
        self.root.title('PYTHON')
        self.root.resizable(FALSE,FALSE) # unlook size
        self.root.iconbitmap('store-64.ico') # icon
        title = Label(self.root,text='Super',fg='white',bg='#0b2f3a',font=('PlayfairDisplay.ttfdr',16,'bold'))
        title.place(x=50,y=2)
        bake = Button(self.root,text='bake',width=13,height=1,font='tajawal',bg='#dba901',command=self.bake)
        bake.place(x=10,y=2)
        #======= food ========
        self.fq1=IntVar()
        self.fq2=IntVar()
        self.fq3=IntVar()
        self.fq4=IntVar()
        self.fq5=IntVar()
        self.fq6=IntVar()
        self.fq7=IntVar()
        self.fq8=IntVar()
        self.fq9=IntVar()
        self.fq10=IntVar()
        self.fq11=IntVar()
        self.fq12=IntVar()
        self.fq13=IntVar()
        self.fq14=IntVar()
        self.fq15=IntVar()
        self.fq16=IntVar()
        self.fq17=IntVar()
        self.fq18=IntVar()
        #======= home ========
        self.hq1=IntVar()
        self.hq2=IntVar()
        self.hq3=IntVar()
        self.hq4=IntVar()
        self.hq5=IntVar()
        self.hq6=IntVar()
        self.hq7=IntVar()
        self.hq8=IntVar()
        self.hq9=IntVar()
        self.hq10=IntVar()
        self.hq11=IntVar()
        self.hq12=IntVar()
        self.hq13=IntVar()
        self.hq14=IntVar()
        self.hq15=IntVar()
        self.hq16=IntVar()
        self.hq17=IntVar()
        self.hq18=IntVar()
        #======= electric ========
        self.eq1=IntVar()
        self.eq2=IntVar()
        self.eq3=IntVar()
        self.eq4=IntVar()
        self.eq5=IntVar()
        self.eq6=IntVar()
        self.eq7=IntVar()
        self.eq8=IntVar()
        self.eq9=IntVar()
        self.eq10=IntVar()
        self.eq11=IntVar()
        self.eq12=IntVar()
        self.eq13=IntVar()
        self.eq14=IntVar()
        self.eq15=IntVar()
        self.eq16=IntVar()
        #====== متغيرات المشتري ======
        self.namo = StringVar()
        self.phono = StringVar()
        self.fatora = StringVar()
        self.adde = StringVar()
        x=random.randint(1000,9999)
        self.fatora.set(str(x))
        self.queue = []
        #===== Rabbish account variables======
        self.cf=StringVar() # cf == calculation food
        self.ch=StringVar() # ch == calculation home
        self.ce=StringVar() # ce == calculation electric
        #======== Customer DATA =========
        F1 =Frame(root,bd=2, width=338,height=170,bg='#0b4c5f') # bd == al bordar
        F1.place(x=0,y=30)
        tit = Label(F1,text = 'Informaion of costomer : ',fg='tomato',bg='#0b4c5f',font=('tajawal',13,'bold'))
        tit.place(x=55,y=0)
        lbl_name = Label(F1, text="Name : ", bg="#0b4c5f", fg="white",font=('tajawal',10,'bold'))
        lbl_name.place(x=10,y=40)
        lbl_phone = Label(F1, text="phone : ", bg="#0b4c5f", fg="white",font=('tajawal',10,'bold'))
        lbl_phone.place(x=10,y=80)
        lbl_num = Label(F1, text="ID : ", bg="#0b4c5f", fg="white",font=('tajawal',10,'bold'))
        lbl_num.place(x=10,y=120)
          # ====== input ====== 
        E_name = Entry(F1, justify='center',textvariable=self.namo)
        E_name.place(x=62,y=42)
        E_phone = Entry(F1,justify='center',textvariable=self.phono)
        E_phone.place(x=62,y=82)
        E_bill =Entry(F1,justify='center',textvariable=self.fatora)
        E_bill.place(x=62,y=122)

          # ====== Buttons ======
        btn_customer  = Button(F1,text ='search',font=('tajawal',10,'bold'),command=self.search)
        btn_customer.place(x=200,y=42,width=100,height=100)
        #====== Bill ======
        titdd = Label(F1,text='[--- BILL --- ]',fg='gold',bg='#0b4c5f',font=('tajawal',13,'bold'))
        titdd.place(x=120,y=145)
        F2 = Frame(root,bd=2, width=338,height=399,bg='white') # bd == al bordar
        F2.place(x=0,y=200)
        scroll_y = Scrollbar(F2,orient=VERTICAL) # scroll Y
        self.textarea=Text(F2,yscrollcommand=scroll_y.set,width=39,height=23) # use scroll
        scroll_y.pack(side=LEFT,fill=Y) # side [ LEFT ,RIGHT, UP ,DWON ]
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        # ====== PRICE =======
        F3 = Frame(root,bd=2, width=662,height=122,bg='#0b4c5f') # bd == al bordar
        F3.place(x=0,y=578)
        Account_btn = Button(F3,text='Account',width=13,height=1,font='tajawal',bg='#dba901',command=self.total)
        Account_btn.place(x=10,y=20)
        Fatora = Button(F3,text='Export',width=13,height=1,font='tajawal',bg='#dba901',command=self.export)
        Fatora.place(x=10,y=70)
        clear = Button(F3,text='Clear',width=13,height=1,font='tajawal',bg='#dba901',command=self.clear)
        clear.place(x=150,y=20)
        exit = Button(F3,text='Exit',width=13,height=1,font='tajawal',bg='#dba901',command=self.close)
        exit.place(x=150,y=70)
        
        Labelo1 = Label(F3,text='Total calculation food',font=('tajawal',10,'bold'),bg='#0b4c5f',fg='gold')
        Labelo1.place(x=330,y=20)
        Labelo2 = Label(F3,text='Total calculation home',font=('tajawal',10,'bold'),bg='#0b4c5f',fg='gold')
        Labelo2.place(x=330,y=50)
        Labelo2 = Label(F3,text='Total calculation electric',font=('tajawal',10,'bold'),bg='#0b4c5f',fg='gold')
        Labelo2.place(x=330,y=80)
        ento1 =Entry(F3,textvariable=self.cf,width=24)
        ento1.place(x=495,y=20)
        ento2 =Entry(F3,textvariable=self.ch,width=24)
        ento2.place(x=495,y=50)
        ento3 =Entry(F3,textvariable=self.ce,width=24)
        ento3.place(x=495,y=80)
        # ======== items 1 =======
        food = Frame(root,bd=2, width=318,height=670,bg='#0b4c5f')
        food.place(x=982,y=30)
        t = Label(food,text='Food',font=('tajawal',20,'bold'),bg='#4b4c5f',fg='gold',width=20,height=1)
        t.place(x=0,y=0)
        # I = items
        I1 =Label(food,text='Rice',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# رز
        I1.place(x=0,y=40)
        I2 =Label(food,text='bulgur',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# برغل
        I2.place(x=0,y=70)
        I3 =Label(food,text='Beans',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# فاصوليا
        I3.place(x=0,y=100)
        I4 =Label(food,text='lentils',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#عدس
        I4.place(x=0,y=130)
        I5 =Label(food,text='pasta',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#معكرونة
        I5.place(x=0,y=160)
        I6 =Label(food,text='Freekeh',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#فريكة
        I6.place(x=0,y=190)
        I7 =Label(food,text='Homs',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#حمص
        I7.place(x=0,y=220)
        I8 =Label(food,text='foll',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#فول
        I8.place(x=0,y=250)
        I9 =Label(food,text='salt',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#ملح
        I9.place(x=0,y=280)
        I10 =Label(food,text='sugar',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#سكر
        I10.place(x=0,y=310)
        I11 =Label(food,text='Black pepper',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# فلفل اسود
        I11.place(x=0,y=340)
        I12 =Label(food,text='Red pepper',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# فلفل احمر
        I12.place(x=0,y=370)
        I13 =Label(food,text='Lobby',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# لوبي
        I13.place(x=0,y=400)
        I14 =Label(food,text='Adamami',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# (فول اخضر)الادمامي
        I14.place(x=0,y=430)
        I15 =Label(food,text='wheat',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#قمح
        I15.place(x=0,y=460)
        I16 =Label(food,text='barley',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#شعير
        I16.place(x=0,y=490)
        I17 =Label(food,text='oats',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#شوفان
        I17.place(x=0,y=520)
        I18 =Label(food,text='Corn',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#ذره
        I18.place(x=0,y=550)

        En_I1 = Entry(food,width=12,textvariable=self.fq1)
        En_I1.place(x=190,y=44)
        En_I2 = Entry(food,width=12,textvariable=self.fq2)
        En_I2.place(x=190,y=74)
        En_I3 = Entry(food,width=12,textvariable=self.fq3)
        En_I3.place(x=190,y=104)
        En_I4 = Entry(food,width=12,textvariable=self.fq4)
        En_I4.place(x=190,y=134)
        En_I5 = Entry(food,width=12,textvariable=self.fq5)
        En_I5.place(x=190,y=164)
        En_I6 = Entry(food,width=12,textvariable=self.fq6)
        En_I6.place(x=190,y=194)
        En_I7 = Entry(food,width=12,textvariable=self.fq7)
        En_I7.place(x=190,y=224)
        En_I8 = Entry(food,width=12,textvariable=self.fq8)
        En_I8.place(x=190,y=254)
        En_I9 = Entry(food,width=12,textvariable=self.fq9)
        En_I9.place(x=190,y=284)
        En_I10 = Entry(food,width=12,textvariable=self.fq10)
        En_I10.place(x=190,y=314)
        En_I11 = Entry(food,width=12,textvariable=self.fq11)
        En_I11.place(x=190,y=344)
        En_I12 = Entry(food,width=12,textvariable=self.fq12)
        En_I12.place(x=190,y=374)
        En_I13 = Entry(food,width=12,textvariable=self.fq13)
        En_I13.place(x=190,y=404)
        En_I14 = Entry(food,width=12,textvariable=self.fq14)
        En_I14.place(x=190,y=434)
        En_I15 = Entry(food,width=12,textvariable=self.fq15)
        En_I15.place(x=190,y=464)
        En_I16 = Entry(food,width=12,textvariable=self.fq16)
        En_I16.place(x=190,y=494)
        En_I17 = Entry(food,width=12,textvariable=self.fq17)
        En_I17.place(x=190,y=524)
        En_I18 = Entry(food,width=12,textvariable=self.fq18)
        En_I18.place(x=190,y=554)
        # ======== items 2 =======
        home = Frame(root,bd=2, width=318,height=670,bg='#0b4c5f')
        home.place(x=663,y=30)
        t = Label(home,text='Home',font=('tajawal',20,'bold'),bg='#4b4c5f',fg='gold',width=20,height=1)
        t.place(x=0,y=0)
        # I = items
        I1 =Label(home,text='Refinery',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# مصفاة
        I1.place(x=0,y=40)
        I2 =Label(home,text='Apron',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# صحن
        I2.place(x=0,y=70)
        I3 =Label(home,text='cup',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# كأس
        I3.place(x=0,y=100)
        I4 =Label(home,text='kettle',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#ابريق
        I4.place(x=0,y=130)
        I5 =Label(home,text='knife',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#سكين
        I5.place(x=0,y=160)
        I6 =Label(home,text='fork',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#شوكة
        I6.place(x=0,y=190)
        I7 =Label(home,text='big pot',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#طنجرة
        I7.place(x=0,y=220)
        I8 =Label(home,text='Basket',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#سلة
        I8.place(x=0,y=250)
        I9 =Label(home,text='Spoons',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#ملاعق
        I9.place(x=0,y=280)
        I10 =Label(home,text='tray',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#صينية
        I10.place(x=0,y=310)
        I11 =Label(home,text='pot',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# وعاء
        I11.place(x=0,y=340)
        I12 =Label(home,text='opener',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# فتاحة
        I12.place(x=0,y=370)
        I13 =Label(home,text='scaler',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# قشارة
        I13.place(x=0,y=400)
        I14 =Label(home,text='cutting board',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# لوح تقطيع
        I14.place(x=0,y=430)
        I15 =Label(home,text='Benot',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#منقرة
        I15.place(x=0,y=460)
        I16 =Label(home,text='Pure',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#صطل
        I16.place(x=0,y=490)
        I17 =Label(home,text='Dirty',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#منفضة
        I17.place(x=0,y=520)
        I18 =Label(home,text='bag',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#كيس
        I18.place(x=0,y=550)

        En_I1 = Entry(home,width=12,textvariable=self.hq1)
        En_I1.place(x=190,y=44)
        En_I2 = Entry(home,width=12,textvariable=self.hq2)
        En_I2.place(x=190,y=74)
        En_I3 = Entry(home,width=12,textvariable=self.hq3)
        En_I3.place(x=190,y=104)
        En_I4 = Entry(home,width=12,textvariable=self.hq4)
        En_I4.place(x=190,y=134)
        En_I5 = Entry(home,width=12,textvariable=self.hq5)
        En_I5.place(x=190,y=164)
        En_I6 = Entry(home,width=12,textvariable=self.hq6)
        En_I6.place(x=190,y=194)
        En_I7 = Entry(home,width=12,textvariable=self.hq7)
        En_I7.place(x=190,y=224)
        En_I8 = Entry(home,width=12,textvariable=self.hq8)
        En_I8.place(x=190,y=254)
        En_I9 = Entry(home,width=12,textvariable=self.hq9)
        En_I9.place(x=190,y=284)
        En_I10 = Entry(home,width=12,textvariable=self.hq10)
        En_I10.place(x=190,y=314)
        En_I11 = Entry(home,width=12,textvariable=self.hq11)
        En_I11.place(x=190,y=344)
        En_I12 = Entry(home,width=12,textvariable=self.hq12)
        En_I12.place(x=190,y=374)
        En_I13 = Entry(home,width=12,textvariable=self.hq13)
        En_I13.place(x=190,y=404)
        En_I14 = Entry(home,width=12,textvariable=self.hq14)
        En_I14.place(x=190,y=434)
        En_I15 = Entry(home,width=12,textvariable=self.hq15)
        En_I15.place(x=190,y=464)
        En_I16 = Entry(home,width=12,textvariable=self.hq16)
        En_I16.place(x=190,y=494)
        En_I17 = Entry(home,width=12,textvariable=self.hq17)
        En_I17.place(x=190,y=524)
        En_I18 = Entry(home,width=12,textvariable=self.hq18)
        En_I18.place(x=190,y=554)
       # ======== items 3 =======
        electric = Frame(root,bd=2, width=318,height=545,bg='#0b4c5f')
        electric.place(x=344,y=30)
        t = Label(electric,text='Electric',font=('tajawal',20,'bold'),bg='#4b4c5f',fg='gold',width=20,height=1)
        t.place(x=0,y=0)
        # I = items
        I1 =Label(electric,text='broom',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# مصفاة
        I1.place(x=0,y=40)
        I2 =Label(electric,text='television',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# صحن
        I2.place(x=0,y=70)
        I3 =Label(electric,text='washing machine',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# كأس
        I3.place(x=0,y=100)
        I4 =Label(electric,text='Microwave',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#ابريق
        I4.place(x=0,y=130)
        I5 =Label(electric,text='Blender',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#سكين
        I5.place(x=0,y=160)
        I6 =Label(electric,text='oven',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#شوكة
        I6.place(x=0,y=190)
        I7 =Label(electric,text='panelectricity',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#طنجرة
        I7.place(x=0,y=220)
        I8 =Label(electric,text='Big fan',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#سلة
        I8.place(x=0,y=250)
        I9 =Label(electric,text='Fans small',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#ملاعق
        I9.place(x=0,y=280)
        I10 =Label(electric,text='television 32',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#صينية
        I10.place(x=0,y=310)
        I11 =Label(electric,text='television 43',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# وعاء
        I11.place(x=0,y=340)
        I12 =Label(electric,text='filter',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# فتاحة
        I12.place(x=0,y=370)
        I13 =Label(electric,text='washing Outomic',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# قشارة
        I13.place(x=0,y=400)
        I14 =Label(electric,text='iron',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')# لوح تقطيع
        I14.place(x=0,y=430)
        I15 =Label(electric,text='Refrigerant',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#منقرة
        I15.place(x=0,y=460)
        I16 =Label(electric,text='air conditioner',font=('tajawal',14,'bold'),bg='#0b4c5f',fg='white')#صطل
        I16.place(x=0,y=490)
        

        En_I1 = Entry(electric,width=12,textvariable=self.eq1)
        En_I1.place(x=190,y=44)
        En_I2 = Entry(electric,width=12,textvariable=self.eq2)
        En_I2.place(x=190,y=74)
        En_I3 = Entry(electric,width=12,textvariable=self.eq3)
        En_I3.place(x=190,y=104)
        En_I4 = Entry(electric,width=12,textvariable=self.eq4)
        En_I4.place(x=190,y=134)
        En_I5 = Entry(electric,width=12,textvariable=self.eq5)
        En_I5.place(x=190,y=164)
        En_I6 = Entry(electric,width=12,textvariable=self.eq6)
        En_I6.place(x=190,y=194)
        En_I7 = Entry(electric,width=12,textvariable=self.eq7)
        En_I7.place(x=190,y=224)
        En_I8 = Entry(electric,width=12,textvariable=self.eq8)
        En_I8.place(x=190,y=254)
        En_I9 = Entry(electric,width=12,textvariable=self.eq9)
        En_I9.place(x=190,y=284)
        En_I10 = Entry(electric,width=12,textvariable=self.eq10)
        En_I10.place(x=190,y=314)
        En_I11 = Entry(electric,width=12,textvariable=self.eq11)
        En_I11.place(x=190,y=344)
        En_I12 = Entry(electric,width=12,textvariable=self.eq12)
        En_I12.place(x=190,y=374)
        En_I13 = Entry(electric,width=12,textvariable=self.eq13)
        En_I13.place(x=190,y=404)
        En_I14 = Entry(electric,width=12,textvariable=self.eq14)
        En_I14.place(x=190,y=434)
        En_I15 = Entry(electric,width=12,textvariable=self.eq15)
        En_I15.place(x=190,y=464)
        En_I16 = Entry(electric,width=12,textvariable=self.eq16)
        En_I16.place(x=190,y=494)
        self.welcom()   
    def total(self):
        # =====food =====
        self.f1=self.fq1.get()*1.5
        self.f2=self.fq2.get()*1.5
        self.f3=self.fq3.get()*2
        self.f4=self.fq4.get()*1
        self.f5=self.fq5.get()*1.5
        self.f6=self.fq6.get()*1.5
        self.f7=self.fq7.get()*2
        self.f8=self.fq8.get()*1
        self.f9=self.fq9.get()*1.5
        self.f10=self.fq10.get()*1.5
        self.f11=self.fq11.get()*2
        self.f12=self.fq12.get()*1
        self.f13=self.fq13.get()*1.5
        self.f14=self.fq14.get()*1.5
        self.f15=self.fq15.get()*2
        self.f16=self.fq16.get()*1
        self.f17=self.fq17.get()*2
        self.f18=self.fq18.get()*1
        self.totalf=float(
            self.f1+
            self.f2+
            self.f3+
            self.f4+
            self.f5+
            self.f6+
            self.f7+
            self.f8+
            self.f9+
            self.f10+
            self.f11+
            self.f12+
            self.f13+
            self.f14+
            self.f15+
            self.f16+
            self.f17+
            self.f18
            )
        self.cf.set(str(self.totalf)+' $')
        # =====home =====
        self.h1=self.hq1.get()*1.5
        self.h2=self.hq2.get()*1.5
        self.h3=self.hq3.get()*2
        self.h4=self.hq4.get()*1
        self.h5=self.hq5.get()*1.5
        self.h6=self.hq6.get()*1.5
        self.h7=self.hq7.get()*2
        self.h8=self.hq8.get()*1
        self.h9=self.hq9.get()*1.5
        self.h10=self.hq10.get()*1.5
        self.h11=self.hq11.get()*2
        self.h12=self.hq12.get()*1
        self.h13=self.hq13.get()*1.5
        self.h14=self.hq14.get()*1.5
        self.h15=self.hq15.get()*2
        self.h16=self.hq16.get()*1
        self.h17=self.hq17.get()*2
        self.h18=self.hq18.get()*1
        self.totalh=float(
            self.h1+
            self.h2+
            self.h3+
            self.h4+
            self.h5+
            self.h6+
            self.h7+
            self.h8+
            self.h9+
            self.h10+
            self.h11+
            self.h12+
            self.h13+
            self.h14+
            self.h15+
            self.h16+
            self.h17+
            self.h18
            )
        self.ch.set(str(self.totalh)+' $')
        # =====electric =====
        self.e1=self.eq1.get()*1.5
        self.e2=self.eq2.get()*1.5
        self.e3=self.eq3.get()*2
        self.e4=self.eq4.get()*1
        self.e5=self.eq5.get()*1.5
        self.e6=self.eq6.get()*1.5
        self.e7=self.eq7.get()*2
        self.e8=self.eq8.get()*1
        self.e9=self.eq9.get()*1.5
        self.e10=self.eq10.get()*1.5
        self.e11=self.eq11.get()*2
        self.e12=self.eq12.get()*1
        self.e13=self.eq13.get()*1.5
        self.e14=self.eq14.get()*1.5
        self.e15=self.eq15.get()*2
        self.e16=self.eq16.get()*1
        self.totale=float(
            self.e1+
            self.e2+
            self.e3+
            self.e4+
            self.e5+
            self.e6+
            self.e7+
            self.e8+
            self.e9+
            self.e10+
            self.e11+
            self.e12+
            self.e13+
            self.e14+
            self.e15+
            self.e16
            )
        self.ce.set(str(self.totale)+' $')
        self.all=float(
            self.totalf+
            self.totalh+
            self.totale
        )
        self.textarea.insert(END,{self.bille()})
    def welcom(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Super Market TMS")
        self.textarea.insert(END,"\n======================================")
        self.textarea.insert(END,f"\n\t B.NUM  :{self.fatora.get()}")
        self.textarea.insert(END,f"\n\t NAME   :{self.namo.get()}")
        self.textarea.insert(END,f"\n\t PHONE  :{self.phono.get()}")
        self.textarea.insert(END,"\n=======================================")
        self.textarea.insert(END,f"\n  price \t     number \t    Purchases")
        self.textarea.insert(END,"\n=======================================")
    def clear(self):
         # =====food =====
        self.f1=self.fq1.set(0)
        self.f2=self.fq2.set(0)
        self.f3=self.fq3.set(0)
        self.f4=self.fq4.set(0)
        self.f5=self.fq5.set(0)
        self.f6=self.fq6.set(0)
        self.f7=self.fq7.set(0)
        self.f8=self.fq8.set(0)
        self.f9=self.fq9.set(0)
        self.f10=self.fq10.set(0)
        self.f11=self.fq11.set(0)
        self.f12=self.fq12.set(0)
        self.f13=self.fq13.set(0)
        self.f14=self.fq14.set(0)
        self.f15=self.fq15.set(0)
        self.f16=self.fq16.set(0)
        self.f17=self.fq17.set(0)
        self.f18=self.fq18.set(0)
        # =====home =====
        self.h1=self.hq1.set(0)
        self.h2=self.hq2.set(0)
        self.h3=self.hq3.set(0)
        self.h4=self.hq4.set(0)
        self.h5=self.hq5.set(0)
        self.h6=self.hq6.set(0)
        self.h7=self.hq7.set(0)
        self.h8=self.hq8.set(0)
        self.h9=self.hq9.set(0)
        self.h10=self.hq10.set(0)
        self.h11=self.hq11.set(0)
        self.h12=self.hq12.set(0)
        self.h13=self.hq13.set(0)
        self.h14=self.hq14.set(0)
        self.h15=self.hq15.set(0)
        self.h16=self.hq16.set(0)
        self.h17=self.hq17.set(0)
        self.h18=self.hq18.set(0)
        
        # =====electric =====
        self.e1=self.eq1.set(0)
        self.e2=self.eq2.set(0)
        self.e3=self.eq3.set(0)
        self.e4=self.eq4.set(0)
        self.e5=self.eq5.set(0)
        self.e6=self.eq6.set(0)
        self.e7=self.eq7.set(0)
        self.e8=self.eq8.set(0)
        self.e9=self.eq9.set(0)
        self.e10=self.eq10.set(0)
        self.e11=self.eq11.set(0)
        self.e12=self.eq12.set(0)
        self.e13=self.eq13.set(0)
        self.e14=self.eq14.set(0)
        self.e15=self.eq15.set(0)
        self.e16=self.eq16.set(0)
        #====== =====
        self.cf.set(0)
        self.ch.set(0)
        self.ce.set(0)
        self.namo.set('')
        self.phono.set('')
        self.fatora.set('')
        self.textarea.delete('1.0',END)
    def close(self):
        self.root.destroy()
    def export(self):
        op = messagebox.askyesno("Save "," Do you want to save the girl ?")
        if op > 0 :
            self.add = self.textarea.get('1.0',END)
            f = open ( 'r'+ str(self.fatora.get())+".txt","w",encoding='utf8')
            f.write(self.add)
            f.close()
            self.adde = self.add
            name = self.namo.get()
            phone = self.phono.get()
            bill = self.fatora.get()
            see =  self.add
            self.queue.append({"name": name, "phone": phone, "bill": bill,"add":see})
            print(self.queue)
        else:
            return
    def bille(self):
        if self.namo.get() == "" or self.phono.get() == "":
            messagebox.showerror("Error!", "Please fill all fields.")
        elif self.cf.get()=="0.0 $" and self.ch.get()=="0.0 $" and self.ce.get()=="0.0 $":
            messagebox.showwarning("Warning!", "You must enter a cost for each type of work.")
        else:
            self.welcom()
            #=====food========
            if self.fq1.get()!=0:
                self.textarea.insert(END,f"\n {self.f1}\t\t{self.fq1.get()}\t Rice")          
                
                
            if self.fq2.get()!=0:
                self.textarea.insert(END,f"\n {self.f2}\t\t{self.fq2.get()}\t bulgur")
            
                
            if self.fq3.get()!=0:
                self.textarea.insert(END,f"\n {self.f3}\t\t{self.fq3.get()}\t Beans")           
                
            if self.fq4.get()!=0:
                self.textarea.insert(END,f"\n {self.f4}\t\t{self.fq4.get()}\t lentils")
                
            
                    
            if self.fq5.get()!=0:
                self.textarea.insert(END,f"\n {self.f5}\t\t{self.fq5.get()}\t pasta")           
                
            if self.fq6.get()!=0:
                self.textarea.insert(END,f"\n {self.f6}\t\t{self.fq6.get()}\t Freekeh")
                
            
                
            if self.fq7.get()!=0:
                self.textarea.insert(END,f"\n {self.f7}\t\t{self.fq7.get()}\t Homs")          
                
            if self.fq8.get()!=0:
                self.textarea.insert(END,f"\n {self.f8}\t\t{self.fq8.get()}\t foll")           
                 
            if self.fq9.get()!=0:
                self.textarea.insert(END,f"\n {self.f9}\t\t{self.fq9.get()}\t salt")        
                
            if self.fq10.get()!=0:
                self.textarea.insert(END,f"\n {self.f10}\t\t{self.fq10.get()}\t sugar")
            
                
            if self.fq11.get()!=0:
                self.textarea.insert(END,f"\n {self.f11}\t\t{self.fq11.get()}\t Black pepper")
            
                
            if self.fq12.get()!=0:
                self.textarea.insert(END,f"\n {self.f12}\t\t{self.fq12.get()}\t Red pepper")
               
                
            if self.fq13.get()!=0:
                self.textarea.insert(END,f"\n {self.f13}\t\t{self.fq13.get()}\t Lobby")
                
            
                
            if self.fq14.get()!=0:
                self.textarea.insert(END,f"\n {self.f14}\t\t{self.f1q4.get()}\t Adamami")
             
            
                    
            if self.fq15.get()!=0:
                self.textarea.insert(END,f"\n {self.f15}\t\t{self.fq15.get()}\t wheat")
            
                
            if self.fq16.get()!=0:
                self.textarea.insert(END,f"\n {self.f16}\t\t{self.fq16.get()}\t barley")
                
            
                
            if self.fq17.get()!=0:
                self.textarea.insert(END,f"\n {self.f17}\t\t{self.fq17.get()}\t oats")           
                
            if self.fq18.get()!=0:
                self.textarea.insert(END,f"\n {self.f18}\t\t{self.fq18.get()}\t Corn")           
                
                #======home===========
            if self.hq1.get()!=0:
                self.textarea.insert(END,f"\n {self.h1}\t\t{self.hq1.get()}\t Refinery")
                
            
                
            if self.hq2.get()!=0:
                self.textarea.insert(END,f"\n {self.h2}\t\t{self.hq2.get()}\t Apron")          
                
            if self.hq3.get()!=0:
                self.textarea.insert(END,f"\n {self.h3}\t\t{self.hq3.get()}\t cup")       
                
            if self.hq4.get()!=0:
                self.textarea.insert(END,f"\n {self.h4}\t\t{self.hq4.get()}\t kettle")           
                    
            if self.hq5.get()!=0:
                self.textarea.insert(END,f"\n {self.h5}\t\t{self.hq5.get()}\t knife")          
                
            if self.hq6.get()!=0:
                self.textarea.insert(END,f"\n {self.h6}\t\t{self.hq6.get()}\t fork")         
                
            if self.hq7.get()!=0:
                self.textarea.insert(END,f"\n {self.h7}\t\t{self.hq7.get()}\t big pot")
            
                
            if self.hq8.get()!=0:
                self.textarea.insert(END,f"\n {self.h8}\\tt{self.hq8.get()}\t Basket")           
                 
            if self.hq9.get()!=0:
                self.textarea.insert(END,f"\n {self.h9}\t\t{self.hq9.get()}\t Spoons")           
                
            if self.hq10.get()!=0:
                self.textarea.insert(END,f"\n {self.h10}\t\t{self.hq10.get()}\t tray")           
                
            if self.hq11.get()!=0:
                self.textarea.insert(END,f"\n {self.h11}\t\t{self.hq11.get()}\t pot")          
                
            if self.hq12.get()!=0:
                self.textarea.insert(END,f"\n {self.h12}\t\t{self.hq12.get()}\t opener")
                
            
                
            if self.hq13.get()!=0:
                self.textarea.insert(END,f"\n {self.h13}\t\t{self.hq13.get()}\t scaler")
                
            
                
            if self.hq14.get()!=0:
                self.textarea.insert(END,f"\n {self.h14}\t\t{self.hq14.get()}\tcutting board")
              
            
                    
            if self.hq15.get()!=0:
                self.textarea.insert(END,f"\n {self.h15}\t\t{self.hq15.get()}\t Benot")
            
                
            if self.hq16.get()!=0:
                self.textarea.insert(END,f"\n {self.h16}\t\t{self.hq16.get()}\t Pure")           
                
            if self.hq17.get()!=0:
                self.textarea.insert(END,f"\n {self.h17}\t\t{self.hq17.get()}\t Dirty")
            
                
            if self.hq18.get()!=0:
                self.textarea.insert(END,f"\n {self.h18}\t\t{self.hq18.get()}\t bag")          
                
            #====electr======
            if self.eq1.get()!=0:
                self.textarea.insert(END,f"\n {self.e1}\t\t{self.eq1.get()}\t broom")          
                
            if self.eq2.get()!=0:
                self.textarea.insert(END,f"\n {self.e2}\t\t{self.eq2.get()}\t television")
        
                
            if self.eq3.get()!=0:
                self.textarea.insert(END,f"\n {self.e3}\t\t{self.eq3.get()}\t washing machine")
            
                
            if self.eq4.get()!=0:
                self.textarea.insert(END,f"\n {self.e4}\t\t{self.eq4.get()}\t Microwave")
                            
                    
            if self.eq5.get()!=0:
                self.textarea.insert(END,f"\n {self.e5}\t\t{self.eq5.get()}\t Blender")
            
                
            if self.eq6.get()!=0:
                self.textarea.insert(END,f"\n {self.e6}\t\t{self.eq6.get()}\t oven")        
                
            if self.eq7.get()!=0:
                self.textarea.insert(END,f"\n {self.e7}\t\t{self.eq7.get()}\t panelectricity")
         
            
                
            if self.eq8.get()!=0:
                self.textarea.insert(END,f"\n {self.e8}\t\t{self.eq8.get()}\t Big fan")
            
                 
            if self.eq9.get()!=0:
                self.textarea.insert(END,f"\n {self.e9}\t\t{self.eq9.get()}\t Fans small")
             
            
                
            if self.eq10.get()!=0:
                self.textarea.insert(END,f"\n {self.e10}\t\t{self.eq10.get()}\t television 32")
                
            
                
            if self.eq11.get()!=0:
                self.textarea.insert(END,f"\n {self.e11}\t\t{self.eq11.get()}\t television 43")
                
            
                
            if self.eq12.get()!=0:
                self.textarea.insert(END,f"\n {self.h12}\t\t{self.eq12.get()}\t filter")
                
            
                
            if self.eq13.get()!=0:
                self.textarea.insert(END,f"\n {self.e13}\t\t{self.eq13.get()}\t washing Outomic")
            
                
            if self.eq14.get()!=0:
                self.textarea.insert(END,f"\n {self.e14}\t\t{self.eq14.get()}\t iron")           
                    
            if self.eq15.get()!=0:
                self.textarea.insert(END,f"\n {self.e15}\t\t{self.eq15.get()}\t Refrigerant")
             
            
                
            if self.eq16.get()!=0:
                self.textarea.insert(END,f"\n {self.e16}\t\t{self.eq16.get()}\t air conditioner")
              
            
                
            self.textarea.insert(END,"\n=======================================\n")
            self.textarea.insert(END,f"\n\t  totale  \t {self.all}$ \n")
            self.textarea.insert(END,"\n=======================================\n")
    def search(self):
        # replace with actual code to search customer in queue
        bill = self.fatora.get()
        for customer in self.queue:
            if bill == customer["bill"]:
                self.namo.set(customer["name"])
                self.phono.set(customer["phone"])
                self.fatora.set(customer["bill"])
                self.textarea.delete('1.0',END)
                self.textarea.insert(END,customer["add"])              
                return
            else:
                messagebox.showerror("Error", "Customer not found")                                 
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def size(self):
        return len(self.queue)
    def bake(self):
        self.close_current_window()
        from superM import Super1
    def close_current_window(self):
        root.destroy()    
root = Tk()
ob =Super(root)      
root.mainloop()