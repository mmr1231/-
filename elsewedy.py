from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests
import json
from datetime import datetime

# current date and time
now = datetime.now()

#Functions

#######pricelist




def test():

        
    try:
            with open("datalist.json", "r") as file:
                data = json.load(file)
                me11.set(data["me11"]),
                me21.set(data["me21"]),
                me31.set(data["me31"]),
                me41.set(data["me41"]),
                me51.set(data["me51"]),
                me61.set(data["me61"]),
                me71.set(data["me71"]),
                me81.set(data["me81"]),
                me91.set(data["me91"]),
                me101.set(data["me101"]),
                me111.set(data["me111"]),
                me121.set(data["me121"]),
                me131.set(data["me131"]),
                me141.set(data["me141"]),
                me151.set(data["me151"]),
                me161.set(data["me161"]),
                me171.set(data["me171"]),
                me181.set(data["me181"]),
                me191.set(data["me191"]),
                me201.set(data["me201"]),
                me211.set(data["me211"]),
                me221.set(data["me221"]),
                me231.set(data["me231"]),
                me241.set(data["me241"]),
                me251.set(data["me251"]),
                me261.set(data["me261"]),
                me271.set(data["me271"]),
                me281.set(data["me281"]),
                me291.set(data["me291"]),
                me301.set(data["me301"]),
                me311.set(data["me311"]),
                me321.set(data["me321"]),
                me331.set(data["me331"]),
                me341.set(data["me341"]),
                me351.set(data["me351"]),
                me361.set(data["me361"]),
                me371.set(data["me371"]),
                me381.set(data["me381"]),
                me391.set(data["me391"]),
                me401.set(data["me401"]),
                me411.set(data["me411"]),
                me421.set(data["me421"]),
                me431.set(data["me431"]),
                me441.set(data["me441"]),
                me451.set(data["me451"]),
                me461.set(data["me461"]),
                me471.set(data["me471"]),
                me481.set(data["me481"]),
                me491.set(data["me491"]),
                me501.set(data["me501"]),
                me511.set(data["me511"]),
                me521.set(data["me521"]),
                me531.set(data["me531"]),
    except FileNotFoundError:
        pass
               




##########

def pricelist():
    


    def savelist():
            

            data = {
                "me11": me11.get(),
                "me21": me21.get(),
                                "me31": me31.get(),
                "me41": me41.get(),
                                "me51": me51.get(),
                "me61": me61.get(),
                                "me71": me71.get(),
                "me81": me81.get(),
                                "me91": me91.get(),
                "me101": me101.get(),
                                "me111": me111.get(),
                "me121": me121.get(),
                                "me131": me131.get(),
                "me141": me141.get(),
                                "me151": me151.get(),
                "me161": me161.get(),
                                "me171": me171.get(),
                "me181": me181.get(),
                                "me191": me191.get(),
                "me201": me201.get(),
                                "me211": me211.get(),
                "me221": me221.get(),
                                "me231": me231.get(),
                "me241": me241.get(),
                                "me251": me251.get(),
                "me261": me261.get(),
                                "me271": me271.get(),
                "me281": me281.get(),
                                "me291": me291.get(),
                "me301": me301.get(),
                                "me311": me311.get(),
                "me321": me321.get(),
                                "me331": me331.get(),
                "me341": me341.get(),
                                "me351": me351.get(),
                "me361": me361.get(),
                                "me371": me371.get(),
                "me381": me381.get(),
                                "me391": me391.get(),
                "me401": me401.get(),
                                "me411": me411.get(),
                "me421": me421.get(),
                                "me431": me431.get(),
                "me441": me441.get(),
                                "me451": me451.get(),
                "me461": me461.get(),
                                "me471": me471.get(),
                "me481": me481.get(),
                                "me491": me491.get(),
                "me501": me501.get(),
                                "me511": me511.get(),
                "me521": me521.get(),
                "me531": me531.get(),

            }



            with open("datalist.json", "w") as file:
                json.dump(data, file)
                messagebox.showinfo('Information','تم تحديث الاسعار')
                prices.destroy()









    prices=Toplevel()

    prices.geometry('1200x600')
    prices.title('الاسعار ')
    menuFrame=Frame(prices,bd=10,relief=RIDGE,bg='#ffffff')
    menuFrame.place(x=5,y=90)

    buttonTotal=Button(menuFrame,text='حفظ الاسعار',font=('lithograph',15,'bold'),bg='#FFA500',bd=3,padx=15,
                   command=savelist )
    buttonTotal.pack(side=BOTTOM)
    buttonTotal=Button(menuFrame,text='لست الاسعار',font=('lithograph',15,'bold'),bg='#FFFFFF',bd=3,padx=15,
                   command=test )
    buttonTotal.pack(side=BOTTOM  )

    foodFrame1=LabelFrame(menuFrame,text='برستول',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
    foodFrame1.pack(side=LEFT)

    foodFrame=LabelFrame(menuFrame,text='1الكوشية',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
    foodFrame.pack(side=LEFT)

    foodFrame2=LabelFrame(menuFrame,text='2الكوشية',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
    foodFrame2.pack(side=LEFT)


    drinksFrame=LabelFrame(menuFrame,text='(الطبع برتغالي)',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
    drinksFrame.pack(side=LEFT)

    drinksFrame1=LabelFrame(menuFrame,text='(الطبع اماراتي)',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
    drinksFrame1.pack(side=LEFT)

    cakesFrame=LabelFrame(menuFrame,text='الدوبلكس',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
    cakesFrame.pack(side=LEFT)

    cakesFrame1=LabelFrame(menuFrame,text='الاستيكر',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
    cakesFrame1.pack(side=LEFT)

    cakesFrame1=LabelFrame(menuFrame,text='الاستيكر',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
    cakesFrame1.pack(side=BOTTOM)

    


##برستول,##

    b250x100=Label(foodFrame1,text='250(70x100)',font=('arial',10,'bold'))
    b250x100.grid(row=0,column=0,sticky=W)

    b250x88=Label(foodFrame1,text='250(66x88)',font=('arial',10,'bold'))
    b250x88.grid(row=1,column=0,sticky=W)

    b270x100=Label(foodFrame1,text='270(70x100)',font=('arial',10,'bold')  )
    b270x100.grid(row=2,column=0,sticky=W)

    b270x88=Label(foodFrame1,text='270(66x88)',font=('arial',10,'bold'))
    b270x88.grid(row=3,column=0,sticky=W)

    b300x100=Label(foodFrame1,text='300(70x100)',font=('arial',10,'bold'))
    b300x100.grid(row=4,column=0,sticky=W)

    b300x88=Label(foodFrame1,text='300(66x88)',font=('arial',10,'bold'))
    b300x88.grid(row=5,column=0,sticky=W)

    b350x100=Label(foodFrame1,text='350(70x100)',font=('arial',10,'bold'))
    b350x100.grid(row=6,column=0,sticky=W)

    b350x88=Label(foodFrame1,text='350(66x88)',font=('arial',10,'bold'))
    b350x88.grid(row=7,column=0,sticky=W)

    e=Label(foodFrame1,text=' ',font=('arial',10,'bold'))
    e.grid(row=8,column=0,sticky=W)

    ee=Label(foodFrame1,text=' ',font=('arial',10,'bold'))
    ee.grid(row=9,column=0,sticky=W)



    #Entry Fields for برستول

    b250x100e=Entry(foodFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me11)
    b250x100e.grid(row=0,column=1)

    b250x88e=Entry(foodFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me21)
    b250x88e.grid(row=1,column=1)

    b270x100e=Entry(foodFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me31)
    b270x100e.grid(row=2,column=1)

    b270x88e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me41)
    b270x88e.grid(row=3, column=1)

    b300x100e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me51)
    b300x100e.grid(row=4, column=1)

    b300x88e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me61 )
    b300x88e.grid(row=5, column=1)

    b350x100e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me71)
    b350x100e.grid(row=6, column=1)

    b350x88e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me81 )
    b350x88e.grid(row=7, column=1)

    eee = Label(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
    eee.grid(row=8, column=1)

    eeee = Label(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
    eeee.grid(row=9, column=1)


    ##الكوشيه

    k90x100=Label(foodFrame,text='90(70x100)',font=('arial',10,'bold'))
    k90x100.grid(row=0,column=0,sticky=W)

    k90x88=Label(foodFrame,text='90(66x88)',font=('arial',10,'bold'))
    k90x88.grid(row=1,column=0,sticky=W)

    k115x100=Label(foodFrame,text='115(70x100)',font=('arial',10,'bold')  )
    k115x100.grid(row=2,column=0,sticky=W)

    k115x88=Label(foodFrame,text='115(66x88)',font=('arial',10,'bold'))
    k115x88.grid(row=3,column=0,sticky=W)

    k130x100=Label(foodFrame,text='130(70x100)',font=('arial',10,'bold'))
    k130x100.grid(row=4,column=0,sticky=W)

    k130x88=Label(foodFrame,text='130(66x88)',font=('arial',10,'bold'))
    k130x88.grid(row=5,column=0,sticky=W)

    k150x100=Label(foodFrame,text='150(70x100)',font=('arial',10,'bold'))
    k150x100.grid(row=6,column=0,sticky=W)

    k150x88=Label(foodFrame,text='150(66x88)',font=('arial',10,'bold'))
    k150x88.grid(row=7,column=0,sticky=W)

    k170x100=Label(foodFrame,text='170(70x100)',font=('arial',10,'bold'))
    k170x100.grid(row=8,column=0,sticky=W)

    k170x88=Label(foodFrame,text='170(66x88)',font=('arial',10,'bold'))
    k170x88.grid(row=9,column=0,sticky=W)




    #Entry Fields for الكوشيه

    k90x100e=Entry(foodFrame,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me91)
    k90x100e.grid(row=0,column=1)

    k90x88e=Entry(foodFrame,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me101)
    k90x88e.grid(row=1,column=1)

    k115x100e=Entry(foodFrame,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me111)
    k115x100e.grid(row=2,column=1)

    k115x88e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6, justify="center",textvariable=me121)
    k115x88e.grid(row=3, column=1)

    k130x100e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me131 )
    k130x100e.grid(row=4, column=1)

    k130x88e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me141 )
    k130x88e.grid(row=5, column=1)

    k150x100e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me151)
    k150x100e.grid(row=6, column=1)

    k150x88e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me161)
    k150x88e.grid(row=7, column=1)

    k170x100e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me171)
    k170x100e.grid(row=8, column=1)

    k170x88e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me181)
    k170x88e.grid(row=9, column=1)

    ######

    ##2الكوشيه

    k200x100=Label(foodFrame2,text='200(70x100)',font=('arial',10,'bold'))
    k200x100.grid(row=0,column=0,sticky=W)

    k200x88=Label(foodFrame2,text='200(66x88)',font=('arial',10,'bold'))
    k200x88.grid(row=1,column=0,sticky=W)

    k250x100=Label(foodFrame2,text='250(70x100)',font=('arial',10,'bold')  )
    k250x100.grid(row=2,column=0,sticky=W)

    k250x88=Label(foodFrame2,text='250(66x88)',font=('arial',10,'bold'))
    k250x88.grid(row=3,column=0,sticky=W)

    k300x100=Label(foodFrame2,text='300(70x100)',font=('arial',10,'bold'))
    k300x100.grid(row=4,column=0,sticky=W)

    k300x88=Label(foodFrame2,text='300(66x88)',font=('arial',10,'bold'))
    k300x88.grid(row=5,column=0,sticky=W)

    k350x100=Label(foodFrame2,text='350(70x100)',font=('arial',10,'bold'))
    k350x100.grid(row=6,column=0,sticky=W)

    k350x88=Label(foodFrame2,text='350(66x88)',font=('arial',10,'bold'))
    k350x88.grid(row=7,column=0,sticky=W)






    #Entry Fields for 2الكوشيه

    k200x100e=Entry(foodFrame2,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me191)
    k200x100e.grid(row=0,column=1)

    k200x88e=Entry(foodFrame2,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me201)
    k200x88e.grid(row=1,column=1)

    k250x100e=Entry(foodFrame2,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me211)
    k250x100e.grid(row=2,column=1)

    k250x88e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6, justify="center",textvariable=me221)
    k250x88e.grid(row=3, column=1)

    k300x100e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me231)
    k300x100e.grid(row=4, column=1)

    k300x88e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me241 )
    k300x88e.grid(row=5, column=1)

    k350x100e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me251)
    k350x100e.grid(row=6, column=1)

    k350x88e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me261)
    k350x88e.grid(row=7, column=1)

    textchicken = Label(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
    textchicken.grid(row=8, column=1)

    textchicken1 = Label(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
    textchicken1.grid(row=9, column=1)






    ##الطبع الاماراتي 

    t60x100=Label(drinksFrame1,text='60(70x100)',font=('arial',10,'bold'))
    t60x100.grid(row=0,column=0,sticky=W)

    t60x85=Label(drinksFrame1,text='60(60x85)',font=('arial',10,'bold'),)
    t60x85.grid(row=1,column=0,sticky=W)

    t70x100=Label(drinksFrame1,text='70(70x100)',font=('arial',10,'bold')  )
    t70x100.grid(row=2,column=0,sticky=W)

    t70x85=Label(drinksFrame1,text='70(60x85)',font=('arial',10,'bold'))
    t70x85.grid(row=3,column=0,sticky=W)

    t80x100=Label(drinksFrame1,text='80(70x100)',font=('arial',10,'bold'))
    t80x100.grid(row=4,column=0,sticky=W)

    t80x85=Label(drinksFrame1,text='80(60x85)',font=('arial',10,'bold'))
    t80x85.grid(row=5,column=0,sticky=W)

    t100x100=Label(drinksFrame1,text='100(70x100)',font=('arial',10,'bold'))
    t100x100.grid(row=6,column=0,sticky=W)

    t100x85=Label(drinksFrame1,text='100(60x85)',font=('arial',10,'bold'))
    t100x85.grid(row=7,column=0,sticky=W)

    t120x100=Label(drinksFrame1,text='120(70x100)',font=('arial',10,'bold'))
    t120x100.grid(row=8,column=0,sticky=W)

    t120x85=Label(drinksFrame1,text='120(60x85)',font=('arial',10,'bold'))
    t120x85.grid(row=9,column=0,sticky=W)


    #Entry Fields for  الطبع الاماراتي

    t60x100e=Entry(drinksFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me271)
    t60x100e.grid(row=0,column=1)

    t60x85e=Entry(drinksFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me281)
    t60x85e.grid(row=1,column=1)

    t70x100e=Entry(drinksFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=me291)
    t70x100e.grid(row=2,column=1)

    t70x85e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center",textvariable=me301)
    t70x85e.grid(row=3, column=1)

    t80x100e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me311)
    t80x100e.grid(row=4, column=1)

    t80x85e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me321 )
    t80x85e.grid(row=5, column=1)

    t100x100e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me331 )
    t100x100e.grid(row=6, column=1)

    t100x85e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me341)
    t100x85e.grid(row=7, column=1)

    t120x100e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me351)
    t120x100e.grid(row=8, column=1)

    t120x85e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me361)
    t120x85e.grid(row=9, column=1)



    #Drinks الطبع

    tb60x100=Label(drinksFrame,text='60(70x100)',font=('arial',10,'bold'))
    tb60x100.grid(row=0,column=0,sticky=W)

    tb60x85=Label(drinksFrame,text='60(60x85)',font=('arial',10,'bold'),)
    tb60x85.grid(row=1,column=0,sticky=W)

    tb70x100=Label(drinksFrame,text='70(70x100)',font=('arial',10,'bold')  )
    tb70x100.grid(row=2,column=0,sticky=W)

    tb70x85=Label(drinksFrame,text='70(60x85)',font=('arial',10,'bold'))
    tb70x85.grid(row=3,column=0,sticky=W)

    tb80x100=Label(drinksFrame,text='80(70x100)',font=('arial',10,'bold'))
    tb80x100.grid(row=4,column=0,sticky=W)

    tb80x85=Label(drinksFrame,text='80(60x85)',font=('arial',10,'bold'))
    tb80x85.grid(row=5,column=0,sticky=W)

    tb100x100=Label(drinksFrame,text='100(70x100)',font=('arial',10,'bold'))
    tb100x100.grid(row=6,column=0,sticky=W)

    tb100x85=Label(drinksFrame,text='100(60x85)',font=('arial',10,'bold'))
    tb100x85.grid(row=7,column=0,sticky=W)

    tb120x100=Label(drinksFrame,text='120(70x100)',font=('arial',10,'bold'))
    tb120x100.grid(row=8,column=0,sticky=W)

    tb120x85=Label(drinksFrame,text='120(60x85)',font=('arial',10,'bold'))
    tb120x85.grid(row=9,column=0,sticky=W)

    #entry fields for  الطبع

    tb60x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me371)
    tb60x100e.grid(row=0, column=1)

    tb60x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me381)
    tb60x85e.grid(row=1, column=1)

    tb70x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me391)
    tb70x100e.grid(row=2, column=1)

    tb70x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me401)
    tb70x85e.grid(row=3, column=1)

    tb80x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me411)
    tb80x100e.grid(row=4, column=1)

    tb80x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me421)
    tb80x85e.grid(row=5, column=1)

    tb100x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me431)
    tb100x100e.grid(row=6, column=1)

    tb100x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me441)
    tb100x85e.grid(row=7, column=1)

    tb120x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me451)
    tb120x100e.grid(row=8, column=1)

    tb120x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me461)
    tb120x85e.grid(row=9, column=1)





    #الدوبلكس

    d250x100=Label(cakesFrame,text='250(70x100)',font=('arial',10,'bold'))
    d250x100.grid(row=0,column=0,sticky=W)

    d300x100=Label(cakesFrame,text='300(70x100)',font=('arial',10,'bold'))
    d300x100.grid(row=1,column=0,sticky=W)

    d350x100=Label(cakesFrame,text='350(70x100)',font=('arial',10,'bold'))
    d350x100.grid(row=2,column=0,sticky=W)

    vanillacake=Label(cakesFrame,text='',font=('arial',10,'bold'))
    vanillacake.grid(row=3,column=0,sticky=W)

    bananacake=Label(cakesFrame,text='',font=('arial',10,'bold'),)
    bananacake.grid(row=4,column=0,sticky=W)

    browniecake=Label(cakesFrame,text='',font=('arial',10,'bold'))
    browniecake.grid(row=5,column=0,sticky=W)

    pineapplecake=Label(cakesFrame,text='',font=('arial',10,'bold'))
    pineapplecake.grid(row=6,column=0,sticky=W)

    chocolatecake=Label(cakesFrame,text='',font=('arial',10,'bold'))
    chocolatecake.grid(row=7,column=0,sticky=W)

    blackforestcake=Label(cakesFrame,text='',font=('arial',10,'bold'))
    blackforestcake.grid(row=8,column=0,sticky=W)

    blackforestcake1=Label(cakesFrame,text='',font=('arial',10,'bold'))
    blackforestcake1.grid(row=9,column=0,sticky=W)

    #entry fields for الدوبلكس

    d250x100e = Entry(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me471)
    d250x100e.grid(row=0, column=1)

    d300x100e = Entry(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=me481)
    d300x100e.grid(row=1, column=1)

    d350x100e = Entry(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me491 )
    d350x100e.grid(row=2, column=1)

    textvanilla = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",)
    textvanilla.grid(row=3, column=1)

    textbanana = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
    textbanana.grid(row=4, column=1)

    textbrownie = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
    textbrownie.grid(row=5, column=1)

    textpineapple = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
    textpineapple.grid(row=6, column=1)

    textchocolate = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
    textchocolate.grid(row=7, column=1)

    textblackforest = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center")
    textblackforest.grid(row=8, column=1)

    textblackforest1 = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center")
    textblackforest1.grid(row=9, column=1)

    #الاستيكر

    a25=Label(cakesFrame1,text='   25   ',font=('arial',10,'bold'),)
    a25.grid(row=0,column=0,sticky=W)

    a40=Label(cakesFrame1,text='   40   ',font=('arial',10,'bold'))
    a40.grid(row=1,column=0,sticky=W)

    a40b=Label(cakesFrame1,text='   40   ',font=('arial',10,'bold'))
    a40b.grid(row=2,column=0,sticky=W)

    a50=Label(cakesFrame1,text='   50   ',font=('arial',10,'bold'),)
    a50.grid(row=3,column=0,sticky=W)

    bananacake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
    bananacake.grid(row=4,column=0,sticky=W)

    browniecake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
    browniecake.grid(row=5,column=0,sticky=W)

    pineapplecake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
    pineapplecake.grid(row=6,column=0,sticky=W)

    chocolatecake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
    chocolatecake.grid(row=7,column=0,sticky=W)

    blackforestcake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
    blackforestcake.grid(row=8,column=0,sticky=W)

    blackforestcake1=Label(cakesFrame1,text='',font=('arial',10,'bold'))
    blackforestcake1.grid(row=9,column=0,sticky=W)

    #entry fields for الاستيكر

    a25e = Entry(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me501)
    a25e.grid(row=0, column=1)

    a40e = Entry(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me511)
    a40e.grid(row=1, column=1)

    a40be = Entry(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center",textvariable=me521)
    a40be.grid(row=2, column=1)

    a50e = Entry(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=me531)
    a50e.grid(row=3, column=1)

    textbanana = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
    textbanana.grid(row=4, column=1)

    textbrownie = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center")
    textbrownie.grid(row=5, column=1)

    textpineapple = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
    textpineapple.grid(row=6, column=1)

    textchocolate = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
    textchocolate.grid(row=7, column=1)

    textblackforest = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
    textblackforest.grid(row=8, column=1)

    textblackforest1 = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
    textblackforest1.grid(row=9, column=1)


    #costlabels & entry fields

    labelCostofFood=Label(costFrame,text='البرستول',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofFood.grid(row=0,column=1,padx=41)

    textCostofFood1=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=brestolvar)
    textCostofFood1.grid(row=0,column=0)

    labelCostofFood2=Label(costFrame,text='الكوشية',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofFood2.grid(row=1,column=1,padx=41)

    textCostofFood3=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=kosahvar)
    textCostofFood3.grid(row=1,column=0)


    labelCostofFood4=Label(costFrame,text='الطبع الاماراتي',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofFood4.grid(row=2,column=1,padx=41)

    textCostofFood5=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=tavar)
    textCostofFood5.grid(row=2,column=0)


    labelCostofFood6=Label(costFrame,text='الطبع البرتغالي',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofFood6.grid(row=0,column=3,padx=41)

    textCostofFood7=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=tbvar)
    textCostofFood7.grid(row=0,column=2)

    labelCostofFood8=Label(costFrame,text='الدوبلكس ',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofFood8.grid(row=1,column=3,padx=41)

    textCostofFood9=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=eldobleksvar)
    textCostofFood9.grid(row=1,column=2)




    labelCostofFood10=Label(costFrame,text='الاستيكر ',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofFood10.grid(row=2,column=3,padx=41)

    textCostofFood2=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=telastekarvar)
    textCostofFood2.grid(row=2,column=2)

    labelCostofFood=Label(buttonFrame1,text='  ',font=('arial',16,'bold'),bg='firebrick4',fg='white')
    labelCostofFood.grid(row=4,column=2)

    textCostofFood5=Entry(buttonFrame1,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=total,justify='center')
    textCostofFood5.grid(row=5,column=1)




























    prices.mainloop()


date = now.strftime("%d/%m/%Y, %H:%M:%S")

def receipt():

        




        def welcome():

            
            textarea.delete('1.0',END)
            textarea.insert(END,f'       {date}                تاريخ اليوم \t\t\t                  ')

            textarea.insert(END,'\n ==========================================================================')
            textarea.insert(END,'\n                          ـــــــفــــــــاتــــــــوره'" ")
            textarea.insert(END,'\n ==========================================================================')
            textarea.insert(END,f"\n   'رقم الفاتورة.\t\t'                              {num.get()}         ") 
            textarea.insert(END,f"\n   'اسم العميل .\t\t'                               {namevar.get()}      ") 
            textarea.insert(END,f"\n   'رقم الفون .\t\t'                               {phonevar.get()}      ")
            textarea.insert(END,f"\n -------------------------------------------------------------------------")
            textarea.insert(END,f"\n    المنتج\t\t                   \t                 السعر \t         ")
            textarea.insert(END,f"\n -------------------------------------------------------------------------")

            textarea.insert(END,f"\n    برستول   \t\t                                    {str(brestolvar.get())}   ")
            textarea.insert(END,f"\n    الكوشية   \t\t                                    {str(kosahvar.get())}   ")
            textarea.insert(END,f"\n    الطبع البرتغالي   \t\t                            {str(tbvar.get())}   ")
            textarea.insert(END,f"\n    الطبع الاماراتي   \t\t                             {str(tavar.get())}   ")
            textarea.insert(END,f"\n    الدوبلكس   \t\t                                   {str(eldobleksvar.get())}   ")
            textarea.insert(END,f"\n    الاستيكر   \t\t                                    {str(telastekarvar.get())}   ")
            textarea.insert(END,'\n ==========================================================================')

            textarea.insert(END,f"\n   الاجمالي   \t\t                                    {str(total.get())}       ")
       






 
        def save1():
                ms=messagebox.askyesno('حغظ','هل تريد الحظ')
                if ms > 0:
                    sav=textarea.get('1.0',END)
                    f1=open('V'+str(num.get()+'.txt')
                            ,'w',encoding='utf-8')
                    f1.write(sav)
                    f1.close()

        sub=Toplevel(root)
        sub.focus()
        refval=StringVar()
        widg_ref=Frame(sub,bd=10,relief=RIDGE,width=500,height=100)
        widg_ref.pack(side=TOP)
        shw_dta=Frame(sub)
        shw_dta.pack(side=TOP)

   ################scrolbar #######################
        scrol=Scrollbar(shw_dta,orient=VERTICAL)
        textarea=Text(shw_dta,yscrollcommand=scrol.set,)
        scrol.pack(side=LEFT,fill=Y)
        scrol.config(command=textarea.yview)
        textarea.pack(fill=BOTH,expand=1)

        lbl_ref=Label(widg_ref,text='رقم الفاتورة. No.',font=1)
        lbl_ref.grid(row=0,column=0,padx=20,pady=20)
        ety_ref=Entry(widg_ref,textvariable=refval,width=20,bd=5,font=1)
        ety_ref.grid(row=0,column=1,columnspan=2,padx=20,pady=20)
        btn1 =Button(widg_ref,text='بحث',width=10,font=1,bg='GreenYellow',bd=5,)
        btn1.grid(row=1,column=0,padx=20,pady=20)
        btn2 = Button(widg_ref, text='مسح', width=10, font=1, bg='yellow', bd=5,)
        btn2.grid(row=1, column=1, padx=20, pady=20)
        btn3 = Button(widg_ref, text='حفظ', width=10, bg='red', bd=5,command=save1)
        btn3.grid(row=1, column=2, padx=20, pady=20)
        btn4 = Button(widg_ref, text='عرض', width=10, bg='red', bd=5,command=welcome)
        btn4.grid(row=1, column=3, padx=20, pady=20)




def RESET():
    
    b250x100e.delete(0,END)
    we1.set('0')
    b250x88e.delete(0,END)
    we2.set('0')
    b270x100e.delete(0,END)
    we3.set('0')
    b270x88e.delete(0,END)
    we4.set('0')
    b300x100e.delete(0,END)
    we5.set('0')
    b300x88e.delete(0,END)
    we6.set('0')
    b350x100e.delete(0,END)
    we7.set('0')
    b350x88e.delete(0,END)
    we8.set('0')
    k90x100e.delete(0,END)
    we9.set('0')
    k90x88e.delete(0,END)
    we10.set('0')

    k115x100e.delete(0,END)
    we11.set('0')
    k115x88e.delete(0,END)
    we12.set('0')
    k130x100e.delete(0,END)
    we13.set('0')
    k130x88e.delete(0,END)
    we14.set('0')
    k150x100e.delete(0,END)
    we15.set('0')
    k150x88e.delete(0,END)
    we16.set('0')
    k170x100e.delete(0,END)
    we17.set('0')
    k170x88e.delete(0,END)
    we18.set('0')
    k200x100e.delete(0,END)
    we19.set('0')
    k200x88e.delete(0,END)
    we20.set('0')

    k250x100e.delete(0,END)
    we21.set('0')
    k250x88e.delete(0,END)
    we22.set('0')
    k300x100e.delete(0,END)
    we23.set('0')
    k300x88e.delete(0,END)
    we24.set('0')
    k350x100e.delete(0,END)
    we25.set('0')
    k350x88e.delete(0,END)
    we26.set('0')
    t60x100e.delete(0,END)
    we27.set('0')
    t60x85e.delete(0,END)
    we28.set('0')
    t70x100e.delete(0,END)
    we29.set('0')
    t70x85e.delete(0,END)
    we30.set('0')

    t80x100e.delete(0,END)
    we31.set('0')
    t80x85e.delete(0,END)
    we32.set('0')
    t100x100e.delete(0,END)
    we33.set('0')
    t100x85e.delete(0,END)
    we34.set('0')
    t120x100e.delete(0,END)
    we35.set('0')
    t120x85e.delete(0,END)
    we36.set('0')
    tb60x100e.delete(0,END)
    we37.set('0')
    tb60x85e.delete(0,END)
    we38.set('0')
    tb70x100e.delete(0,END)
    we39.set('0')
    tb70x85e.delete(0,END)
    we40.set('0')

    tb80x100e.delete(0,END)
    we41.set('0')
    tb80x85e.delete(0,END)
    we42.set('0')
    tb100x100e.delete(0,END)
    we43.set('0')
    tb100x85e.delete(0,END)
    we44.set('0')
    tb120x100e.delete(0,END)
    we45.set('0')
    tb120x85e.delete(0,END)
    we46.set('0')
    d250x100e.delete(0,END)
    we47.set('0')
    d300x100e.delete(0,END)
    we48.set('0')
    d350x100e.delete(0,END)
    we49.set('0')
    a25e.delete(0,END)
    we50.set('0')
    a40e.delete(0,END)
    we51.set('0')
    a40be.delete(0,END)
    we52.set('0')
    a50e.delete(0,END)
    we53.set('0')
    #############
    textCostofFood1.delete(0,END)
    brestolvar.set('جنية ')
    textCostofFood3.delete(0,END)
    kosahvar.set('جنيه')
    
    textCostofFood5.delete(0,END)
    tavar.set('جنية')
    textCostofFood7.delete(0,END)
    tbvar.set('جنية')
    textCostofFood9.delete(0,END)
    eldobleksvar.set('جنية')
    textCostofFood2.delete(0,END)
    telastekarvar.set('جنية')
    textCostofFood5.delete(0,END)
    total.set('جنية')
    nameenter.delete(0,END)
    namevar.set(' ')
    phoneenter.delete(0,END)
    phonevar.set('')
 

    



def totalcost():

    test()
    global brestolvar,kosahvar,tavar,tbvar,eldobleksvar,telastekarvar,totalio,total
    if we1.get() != 0 or we2.get() != 0 or we3.get() != 0 or we4.get() != 0 or we5.get() != 0 or \
        we6.get() != 0 or we7.get() != 0 or we8.get() != 0 or we9.get() != 0 or we10.get() != 0 or\
        we11.get() != 0 or we12.get() != 0 or we13.get() != 0 or we14.get() != 0 or we15.get() != 0 or \
        we16.get() != 0 or we17.get() != 0 or we18.get() != 0 or we19.get() != 0 or we20.get() != 0 or \
        we21.get() != 0 or we22.get() != 0 or we23.get() != 0 or we24.get() != 0 or we25.get() != 0 or\
        we26.get() != 0 or we27.get() != 0 or we28.get() != 0 or we29.get() != 0 or we30.get() != 0 or we31.get() != 0 or we32.get() != 0 or\
        we33.get() != 0 or we34.get() != 0 or we35.get() != 0 or we36.get() != 0 or we37.get() != 0 or\
        we38.get() != 0 or we39.get() != 0 or we40.get() != 0 or we41.get() != 0 or we42.get() != 0 or\
        we43.get() != 0 or we44.get() != 0 or we45.get() != 0 or we46.get() != 0 or we47.get() != 0 or\
        we48.get() != 0 or we49.get() != 0 or we50.get() != 0 or we51.get() != 0 or we52.get() != 0 or\
        we52.get() != 0  :
        io1=int(we1.get())
        io2=int(we2.get())
        io3=int(we3.get())
        io4 = int(we4.get())
        io5 = int(we5.get())
        io6 = int(we6.get())
        io7 = int(we7.get())
        io8 = int(we8.get())
####################################

        io9 = int(we9.get())
        io10 = int(we10.get())
        io11 = int(we11.get())
        io12 = int(we12.get())
        io13 = int(we13.get())
        io14 = int(we14.get())
        io15 = int(we15.get())
        io16 = int(we16.get())
        io17 = int(we17.get())
        io18 = int(we18.get())
        io19 = int(we19.get())
        io20 = int(we20.get())
        io21 = int(we21.get())
        io22 = int(we22.get())
        io23 = int(we23.get())
        io24 = int(we24.get())
        io25 = int(we25.get())
        io26 = int(we26.get())
        #################################
        io27 = int(we27.get())
        io28 = int(we28.get())
        io29 = int(we29.get())
        io30 = int(we30.get())
        io31 = int(we31.get())
        io32 = int(we32.get())
        io33 = int(we33.get())
        io34 = int(we34.get())
        io35 = int(we35.get())
        io36 = int(we36.get())
############## #########################
        io37 = int(we37.get())
        io38 = int(we38.get())
        io39 = int(we39.get())
        io40 = int(we40.get())
        io41 = int(we41.get())
        io42 = int(we42.get())
        io43 = int(we43.get())
        io44 = int(we44.get())
        io45 = int(we45.get())
        io46 = int(we46.get())
#########################################

        io47 = int(we47.get())
        io48 = int(we48.get())
        io49 = int(we49.get())
#####################################################        
        io50 = int(we50.get())
        io51 = int(we51.get())
        io52 = int(we52.get())
        io53 = int(we53.get())
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        mi1=int(me11.get())
        mi2=int(me21.get())
        mi3=int(me31.get())
        mi4 = int(me41.get())
        mi5 = int(me51.get())
        mi6 = int(me61.get())
        mi7 = int(me71.get())
        mi8 = int(me81.get())
####################################

        mi9 = int(me91.get())
        mi10 = int(me101.get())
        mi11 = int(me111.get())
        mi12 = int(me121.get())
        mi13 = int(me131.get())
        mi14 = int(me141.get())
        mi15 = int(me151.get())
        mi16 = int(me161.get())
        mi17 = int(me171.get())
        mi18 = int(me181.get())
        mi19 = int(me191.get())
        mi20 = int(me201.get())
        mi21 = int(me211.get())
        mi22 = int(me221.get())
        mi23 = int(me231.get())
        mi24 = int(me241.get())
        mi25 = int(me251.get())
        mi26 = int(me261.get())
        #################################
        mi27 = int(me271.get())
        mi28 = int(me281.get())
        mi29 = int(me291.get())
        mi30 = int(me301.get())
        mi31 = int(me311.get())
        mi32 = int(me321.get())
        mi33 = int(me331.get())
        mi34 = int(me341.get())
        mi35 = int(me351.get())
        mi36 = int(me361.get())
############## #########################
        mi37 = int(me371.get())
        mi38 = int(me381.get())
        mi39 = int(me391.get())
        mi40 = int(me401.get())
        mi41 = int(me411.get())
        mi42 = int(me421.get())
        mi43 = int(me431.get())
        mi44 = int(me441.get())
        mi45 = int(me451.get())
        mi46 = int(me461.get())
#########################################

        mi47 = int(me471.get())
        mi48 = int(me481.get())
        mi49 = int(me491.get())
#####################################################        
        mi50 = int(me501.get())
        mi51 = int(me51.get())
        mi52 = int(me521.get())
        mi53 = int(me531.get())





        brestol=(io1*mi1)+(io2*mi2)+(io3*mi3)+(io4*mi4)+ (io5*mi5) + (io6 * mi6) + (io7 * mi7) \
                    + (io8 * mi8) 

        kosah=(io9*mi9)+(io10*mi10)+ (io11 *mi11) + (io12 * mi12) + (io13 * mi13) + (io14 * mi14) \
                      + (io15 * mi15) + (io16 * mi16) + (io17 * mi17)+ (io18 * mi18) + (io19 * mi19) + (io20 * mi20)  + (io21 * mi21) + (io21 * mi22) + (io22 * mi23)+ (io23 * mi24) + (io24 * mi25) + (io25 * mi26)+(io26 * mi27)

        ta= (io27 * mi27) + (io28 * mi28) + (io29 * mi29)+ (io30 * mi30) + (io31 * mi31) + (io32 * mi32)  + (io33 * mi33) + (io34 * mi34) + (io35 * mi35)+ (io36 * mi36) 

        
        tb=(io37*mi37)+(io38*mi38)+ (io39 * mi39) + (io40 * mi40) + (io41 * mi41) + (io42 * mi42) \
                     + (io43 * mi43) + (io44 * mi44) + (io45 * mi45)+ (io46 * mi46)
        eldobleks=(io47*mi47)+(io48*mi48)+ (io49 * mi49) 
        
        telastekar=(io50*mi50)+(io51*mi51)+ (io52 * mi52) + (io53 * mi53) 
        


        brestolvar.set(str(brestol)+ ' جنية')
        kosahvar.set(str(kosah)+ ' جنية')
        tavar.set(str(ta)+ ' جنية')
        tbvar.set(str(tb)+ ' جنية')
        eldobleksvar.set(str(eldobleks)+ ' جنية')
        telastekarvar.set(str(telastekar)+ ' جنية')

        totalio=brestol+kosah+ta+tb+eldobleks+telastekar
        total.set(str(totalio)+' جنية')

    else:
        messagebox.showerror('Error','برجاء ادخال البيانات بشكل صحيح')



root=Tk()

root.geometry('1270x690+0+0')

root.resizable(0,0)

root.title('ELSewedy Print')

root.config(bg='firebrick4')
topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='                                                               خـــــــــاصه ادارة المــــبيعات ',font=('arial',30,'bold'),fg='yellow',bd=9,
                 bg='firebrick4',width=51)
labelTitle.grid(row=0,column=0,)

#########################

me11=StringVar()
me21=StringVar()

me31=StringVar()
me41=StringVar()

me51=StringVar()
me61=StringVar()

me71=StringVar()
me81=StringVar()
######################b الرستول من 1الي 8
me91=StringVar()
me101=StringVar()

me111=StringVar()
me121=StringVar()

me131=StringVar()
me141=StringVar()

me151=StringVar()
me161=StringVar()

me171=StringVar()
me181=StringVar()

me191=StringVar()
me201=StringVar()

me211=StringVar()
me221=StringVar()

me231=StringVar()
me241=StringVar()

me251=StringVar()
me261=StringVar()
################################### kk الكوشيه من 9 الي 26

me271=StringVar()
me281=StringVar()

me291=StringVar()
me301=StringVar()

me311=StringVar()
me321=StringVar()

me331=StringVar()
me341=StringVar()

me351=StringVar()
me361=StringVar()
#########################3ttt من 27 الي 36 الطبع الاماراتي
me371=StringVar()
me381=StringVar()

me391=StringVar()
me401=StringVar()

me411=StringVar()
me421=StringVar()

me431=StringVar()
me441=StringVar()

me451=StringVar()
me461=StringVar()
#####################tttb  من 37 الي 46 الطبع البرتغالي

me471=StringVar()
me481=StringVar()

me491=StringVar()
#######################ddd من 47 الي 49 الدوبلكس 
me501=StringVar()
me511=StringVar()

me521=StringVar()
me531=StringVar()





##################################


namevar=StringVar()
phonevar=StringVar()


labelSubTotal=Label(topFrame,text='اســــــم العمــــيــل',font=('arial',20,'bold'),fg='#00000F',bg='firebrick4')
labelSubTotal.place(x=200,y=5,)

nameenter=Entry(topFrame,font=('arial',15,'bold'),bd=3,width=14,textvariable=namevar,justify='center')
nameenter.place(x=2,y=10)

labelServiceTax=Label(topFrame,text='فون العمــــيــل',font=('arial',20,'bold'),bg='firebrick4',fg='#00000F')
labelServiceTax.place(x=600,y=5)

phoneenter=Entry(topFrame,font=('arial',15,'bold'),bd=3,width=14,textvariable=phonevar,justify='center')
phoneenter.place(x=400,y=10)

#frames

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.place(x=5,y=90)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM, anchor=W)

foodFrame1=LabelFrame(menuFrame,text='برستول',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
foodFrame1.pack(side=LEFT)

foodFrame=LabelFrame(menuFrame,text='1الكوشية',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
foodFrame.pack(side=LEFT)

foodFrame2=LabelFrame(menuFrame,text='2الكوشية',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4',)
foodFrame2.pack(side=LEFT)


drinksFrame=LabelFrame(menuFrame,text='(الطبع برتغالي)',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

drinksFrame1=LabelFrame(menuFrame,text='(الطبع اماراتي)',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame1.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='الدوبلكس',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame.pack(side=LEFT)

cakesFrame1=LabelFrame(menuFrame,text='الاستيكر',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame1.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)


calculatorFrame1=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
calculatorFrame1.place(x=900,y=465)



buttonFrame1=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
buttonFrame1.place(x=600,y=480)



#############################
num=StringVar()
x=random.randint(1,100000000)
num.set(str(x))       
brestolvar=StringVar()
kosahvar=StringVar()
tavar=StringVar()
tbvar=StringVar()
eldobleksvar=StringVar()
telastekarvar=StringVar()
total=StringVar()

#########################



we1=IntVar()
we2=IntVar()

we3=IntVar()
we4=IntVar()

we5=IntVar()
we6=IntVar()

we7=IntVar()
we8=IntVar()
######################b الرستول من 1الي 8
we9=IntVar()
we10=IntVar()

we11=IntVar()
we12=IntVar()

we13=IntVar()
we14=IntVar()

we15=IntVar()
we16=IntVar()

we17=IntVar()
we18=IntVar()

we19=IntVar()
we20=IntVar()

we21=IntVar()
we22=IntVar()

we23=IntVar()
we24=IntVar()

we25=IntVar()
we26=IntVar()
################################### kk الكوشيه من 9 الي 26

we27=IntVar()
we28=IntVar()

we29=IntVar()
we30=IntVar()

we31=IntVar()
we32=IntVar()

we33=IntVar()
we34=IntVar()

we35=IntVar()
we36=IntVar()
#########################3ttt من 27 الي 36 الطبع الاماراتي
we37=IntVar()
we38=IntVar()

we39=IntVar()
we40=IntVar()

we41=IntVar()
we42=IntVar()

we43=IntVar()
we44=IntVar()

we45=IntVar()
we46=IntVar()
#####################tttb  من 37 الي 46 الطبع البرتغالي

we47=IntVar()
we48=IntVar()

we49=IntVar()
#######################ddd من 47 الي 49 الدوبلكس 
we50=IntVar()
we51=IntVar()

we52=IntVar()
we53=IntVar()




##برستول,##

b250x100=Checkbutton(foodFrame1,text='250(70x100)',font=('arial',10,'bold'))
b250x100.grid(row=0,column=0,sticky=W)

b250x88=Checkbutton(foodFrame1,text='250(66x88)',font=('arial',10,'bold'))
b250x88.grid(row=1,column=0,sticky=W)

b270x100=Checkbutton(foodFrame1,text='270(70x100)',font=('arial',10,'bold')  )
b270x100.grid(row=2,column=0,sticky=W)

b270x88=Checkbutton(foodFrame1,text='270(66x88)',font=('arial',10,'bold'))
b270x88.grid(row=3,column=0,sticky=W)

b300x100=Checkbutton(foodFrame1,text='300(70x100)',font=('arial',10,'bold'))
b300x100.grid(row=4,column=0,sticky=W)

b300x88=Checkbutton(foodFrame1,text='300(66x88)',font=('arial',10,'bold'))
b300x88.grid(row=5,column=0,sticky=W)

b350x100=Checkbutton(foodFrame1,text='350(70x100)',font=('arial',10,'bold'))
b350x100.grid(row=6,column=0,sticky=W)

b350x88=Checkbutton(foodFrame1,text='350(66x88)',font=('arial',10,'bold'))
b350x88.grid(row=7,column=0,sticky=W)

e=Label(foodFrame1,text=' ',font=('arial',10,'bold'))
e.grid(row=8,column=0,sticky=W)

ee=Label(foodFrame1,text=' ',font=('arial',10,'bold'))
ee.grid(row=9,column=0,sticky=W)



#Entry Fields for برستول

b250x100e=Entry(foodFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we1)
b250x100e.grid(row=0,column=1)

b250x88e=Entry(foodFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we2)
b250x88e.grid(row=1,column=1)

b270x100e=Entry(foodFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we3)
b270x100e.grid(row=2,column=1)

b270x88e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we4)
b270x88e.grid(row=3, column=1)

b300x100e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we5)
b300x100e.grid(row=4, column=1)

b300x88e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we6 )
b300x88e.grid(row=5, column=1)

b350x100e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we7)
b350x100e.grid(row=6, column=1)

b350x88e = Entry(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we8 )
b350x88e.grid(row=7, column=1)

eee = Label(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
eee.grid(row=8, column=1)

eeee = Label(foodFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
eeee.grid(row=9, column=1)


##الكوشيه

k90x100=Checkbutton(foodFrame,text='90(70x100)',font=('arial',10,'bold'))
k90x100.grid(row=0,column=0,sticky=W)

k90x88=Checkbutton(foodFrame,text='90(66x88)',font=('arial',10,'bold'))
k90x88.grid(row=1,column=0,sticky=W)

k115x100=Checkbutton(foodFrame,text='115(70x100)',font=('arial',10,'bold')  )
k115x100.grid(row=2,column=0,sticky=W)

k115x88=Checkbutton(foodFrame,text='115(66x88)',font=('arial',10,'bold'))
k115x88.grid(row=3,column=0,sticky=W)

k130x100=Checkbutton(foodFrame,text='130(70x100)',font=('arial',10,'bold'))
k130x100.grid(row=4,column=0,sticky=W)

k130x88=Checkbutton(foodFrame,text='130(66x88)',font=('arial',10,'bold'))
k130x88.grid(row=5,column=0,sticky=W)

k150x100=Checkbutton(foodFrame,text='150(70x100)',font=('arial',10,'bold'))
k150x100.grid(row=6,column=0,sticky=W)

k150x88=Checkbutton(foodFrame,text='150(66x88)',font=('arial',10,'bold'))
k150x88.grid(row=7,column=0,sticky=W)

k170x100=Checkbutton(foodFrame,text='170(70x100)',font=('arial',10,'bold'))
k170x100.grid(row=8,column=0,sticky=W)

k170x88=Checkbutton(foodFrame,text='170(66x88)',font=('arial',10,'bold'))
k170x88.grid(row=9,column=0,sticky=W)




#Entry Fields for الكوشيه

k90x100e=Entry(foodFrame,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we9)
k90x100e.grid(row=0,column=1)

k90x88e=Entry(foodFrame,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we10)
k90x88e.grid(row=1,column=1)

k115x100e=Entry(foodFrame,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we11)
k115x100e.grid(row=2,column=1)

k115x88e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6, justify="center",textvariable=we12)
k115x88e.grid(row=3, column=1)

k130x100e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we13 )
k130x100e.grid(row=4, column=1)

k130x88e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we14 )
k130x88e.grid(row=5, column=1)

k150x100e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we15)
k150x100e.grid(row=6, column=1)

k150x88e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we16)
k150x88e.grid(row=7, column=1)

k170x100e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we17)
k170x100e.grid(row=8, column=1)

k170x88e = Entry(foodFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we18)
k170x88e.grid(row=9, column=1)

######

##2الكوشيه

k200x100=Checkbutton(foodFrame2,text='200(70x100)',font=('arial',10,'bold'))
k200x100.grid(row=0,column=0,sticky=W)

k200x88=Checkbutton(foodFrame2,text='200(66x88)',font=('arial',10,'bold'))
k200x88.grid(row=1,column=0,sticky=W)

k250x100=Checkbutton(foodFrame2,text='250(70x100)',font=('arial',10,'bold')  )
k250x100.grid(row=2,column=0,sticky=W)

k250x88=Checkbutton(foodFrame2,text='250(66x88)',font=('arial',10,'bold'))
k250x88.grid(row=3,column=0,sticky=W)

k300x100=Checkbutton(foodFrame2,text='300(70x100)',font=('arial',10,'bold'))
k300x100.grid(row=4,column=0,sticky=W)

k300x88=Checkbutton(foodFrame2,text='300(66x88)',font=('arial',10,'bold'))
k300x88.grid(row=5,column=0,sticky=W)

k350x100=Checkbutton(foodFrame2,text='350(70x100)',font=('arial',10,'bold'))
k350x100.grid(row=6,column=0,sticky=W)

k350x88=Checkbutton(foodFrame2,text='350(66x88)',font=('arial',10,'bold'))
k350x88.grid(row=7,column=0,sticky=W)






#Entry Fields for 2الكوشيه

k200x100e=Entry(foodFrame2,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we19)
k200x100e.grid(row=0,column=1)

k200x88e=Entry(foodFrame2,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we20)
k200x88e.grid(row=1,column=1)

k250x100e=Entry(foodFrame2,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we21)
k250x100e.grid(row=2,column=1)

k250x88e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6, justify="center",textvariable=we22)
k250x88e.grid(row=3, column=1)

k300x100e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we23)
k300x100e.grid(row=4, column=1)

k300x88e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we24 )
k300x88e.grid(row=5, column=1)

k350x100e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we25)
k350x100e.grid(row=6, column=1)

k350x88e = Entry(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we26)
k350x88e.grid(row=7, column=1)

textchicken = Label(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
textchicken.grid(row=8, column=1)

textchicken1 = Label(foodFrame2, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
textchicken1.grid(row=9, column=1)






##الطبع الاماراتي 

t60x100=Checkbutton(drinksFrame1,text='60(70x100)',font=('arial',10,'bold'))
t60x100.grid(row=0,column=0,sticky=W)

t60x85=Checkbutton(drinksFrame1,text='60(60x85)',font=('arial',10,'bold'),)
t60x85.grid(row=1,column=0,sticky=W)

t70x100=Checkbutton(drinksFrame1,text='70(70x100)',font=('arial',10,'bold')  )
t70x100.grid(row=2,column=0,sticky=W)

t70x85=Checkbutton(drinksFrame1,text='70(60x85)',font=('arial',10,'bold'))
t70x85.grid(row=3,column=0,sticky=W)

t80x100=Checkbutton(drinksFrame1,text='80(70x100)',font=('arial',10,'bold'))
t80x100.grid(row=4,column=0,sticky=W)

t80x85=Checkbutton(drinksFrame1,text='80(60x85)',font=('arial',10,'bold'))
t80x85.grid(row=5,column=0,sticky=W)

t100x100=Checkbutton(drinksFrame1,text='100(70x100)',font=('arial',10,'bold'))
t100x100.grid(row=6,column=0,sticky=W)

t100x85=Checkbutton(drinksFrame1,text='100(60x85)',font=('arial',10,'bold'))
t100x85.grid(row=7,column=0,sticky=W)

t120x100=Checkbutton(drinksFrame1,text='120(70x100)',font=('arial',10,'bold'))
t120x100.grid(row=8,column=0,sticky=W)

t120x85=Checkbutton(drinksFrame1,text='120(60x85)',font=('arial',10,'bold'))
t120x85.grid(row=9,column=0,sticky=W)


#Entry Fields for  الطبع الاماراتي

t60x100e=Entry(drinksFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we27)
t60x100e.grid(row=0,column=1)

t60x85e=Entry(drinksFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we28)
t60x85e.grid(row=1,column=1)

t70x100e=Entry(drinksFrame1,font=('arial',10,'bold'),bd=7,width=6,justify="center",textvariable=we29)
t70x100e.grid(row=2,column=1)

t70x85e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center",textvariable=we30)
t70x85e.grid(row=3, column=1)

t80x100e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we31)
t80x100e.grid(row=4, column=1)

t80x85e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we32 )
t80x85e.grid(row=5, column=1)

t100x100e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we33 )
t100x100e.grid(row=6, column=1)

t100x85e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we34)
t100x85e.grid(row=7, column=1)

t120x100e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we35)
t120x100e.grid(row=8, column=1)

t120x85e = Entry(drinksFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we36)
t120x85e.grid(row=9, column=1)



#Drinks الطبع

tb60x100=Checkbutton(drinksFrame,text='60(70x100)',font=('arial',10,'bold'))
tb60x100.grid(row=0,column=0,sticky=W)

tb60x85=Checkbutton(drinksFrame,text='60(60x85)',font=('arial',10,'bold'),)
tb60x85.grid(row=1,column=0,sticky=W)

tb70x100=Checkbutton(drinksFrame,text='70(70x100)',font=('arial',10,'bold')  )
tb70x100.grid(row=2,column=0,sticky=W)

tb70x85=Checkbutton(drinksFrame,text='70(60x85)',font=('arial',10,'bold'))
tb70x85.grid(row=3,column=0,sticky=W)

tb80x100=Checkbutton(drinksFrame,text='80(70x100)',font=('arial',10,'bold'))
tb80x100.grid(row=4,column=0,sticky=W)

tb80x85=Checkbutton(drinksFrame,text='80(60x85)',font=('arial',10,'bold'))
tb80x85.grid(row=5,column=0,sticky=W)

tb100x100=Checkbutton(drinksFrame,text='100(70x100)',font=('arial',10,'bold'))
tb100x100.grid(row=6,column=0,sticky=W)

tb100x85=Checkbutton(drinksFrame,text='100(60x85)',font=('arial',10,'bold'))
tb100x85.grid(row=7,column=0,sticky=W)

tb120x100=Checkbutton(drinksFrame,text='120(70x100)',font=('arial',10,'bold'))
tb120x100.grid(row=8,column=0,sticky=W)

tb120x85=Checkbutton(drinksFrame,text='120(60x85)',font=('arial',10,'bold'))
tb120x85.grid(row=9,column=0,sticky=W)

#entry fields for  الطبع

tb60x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we37)
tb60x100e.grid(row=0, column=1)

tb60x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we38)
tb60x85e.grid(row=1, column=1)

tb70x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we39)
tb70x100e.grid(row=2, column=1)

tb70x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we40)
tb70x85e.grid(row=3, column=1)

tb80x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we41)
tb80x100e.grid(row=4, column=1)

tb80x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we42 )
tb80x85e.grid(row=5, column=1)

tb100x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we43)
tb100x100e.grid(row=6, column=1)

tb100x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we44)
tb100x85e.grid(row=7, column=1)

tb120x100e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we45)
tb120x100e.grid(row=8, column=1)

tb120x85e = Entry(drinksFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we46)
tb120x85e.grid(row=9, column=1)





#الدوبلكس

d250x100=Checkbutton(cakesFrame,text='250(70x100)',font=('arial',10,'bold'))
d250x100.grid(row=0,column=0,sticky=W)

d300x100=Checkbutton(cakesFrame,text='300(70x100)',font=('arial',10,'bold'))
d300x100.grid(row=1,column=0,sticky=W)

d350x100=Checkbutton(cakesFrame,text='350(70x100)',font=('arial',10,'bold'))
d350x100.grid(row=2,column=0,sticky=W)

vanillacake=Label(cakesFrame,text='',font=('arial',10,'bold'))
vanillacake.grid(row=3,column=0,sticky=W)

bananacake=Label(cakesFrame,text='',font=('arial',10,'bold'),)
bananacake.grid(row=4,column=0,sticky=W)

browniecake=Label(cakesFrame,text='',font=('arial',10,'bold'))
browniecake.grid(row=5,column=0,sticky=W)

pineapplecake=Label(cakesFrame,text='',font=('arial',10,'bold'))
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake=Label(cakesFrame,text='',font=('arial',10,'bold'))
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Label(cakesFrame,text='',font=('arial',10,'bold'))
blackforestcake.grid(row=8,column=0,sticky=W)

blackforestcake1=Label(cakesFrame,text='',font=('arial',10,'bold'))
blackforestcake1.grid(row=9,column=0,sticky=W)

#entry fields for الدوبلكس

d250x100e = Entry(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we47)
d250x100e.grid(row=0, column=1)

d300x100e = Entry(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" ,textvariable=we48)
d300x100e.grid(row=1, column=1)

d350x100e = Entry(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we49 )
d350x100e.grid(row=2, column=1)

textvanilla = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",)
textvanilla.grid(row=3, column=1)

textbanana = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
textbanana.grid(row=4, column=1)

textbrownie = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
textbrownie.grid(row=5, column=1)

textpineapple = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center" )
textpineapple.grid(row=6, column=1)

textchocolate = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
textchocolate.grid(row=7, column=1)

textblackforest = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center")
textblackforest.grid(row=8, column=1)

textblackforest1 = Label(cakesFrame, font=('arial', 10, 'bold'), bd=7, width=6,justify="center")
textblackforest1.grid(row=9, column=1)

#الاستيكر

a25=Checkbutton(cakesFrame1,text='   25   ',font=('arial',10,'bold'),)
a25.grid(row=0,column=0,sticky=W)

a40=Checkbutton(cakesFrame1,text='   40   ',font=('arial',10,'bold'))
a40.grid(row=1,column=0,sticky=W)

a40b=Checkbutton(cakesFrame1,text='   40   ',font=('arial',10,'bold'))
a40b.grid(row=2,column=0,sticky=W)

a50=Checkbutton(cakesFrame1,text='   50   ',font=('arial',10,'bold'),)
a50.grid(row=3,column=0,sticky=W)

bananacake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
bananacake.grid(row=4,column=0,sticky=W)

browniecake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
browniecake.grid(row=5,column=0,sticky=W)

pineapplecake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
pineapplecake.grid(row=6,column=0,sticky=W)

chocolatecake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
chocolatecake.grid(row=7,column=0,sticky=W)

blackforestcake=Label(cakesFrame1,text='',font=('arial',10,'bold'))
blackforestcake.grid(row=8,column=0,sticky=W)

blackforestcake1=Label(cakesFrame1,text='',font=('arial',10,'bold'))
blackforestcake1.grid(row=9,column=0,sticky=W)

#entry fields for الاستيكر

a25e = Entry(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we50)
a25e.grid(row=0, column=1)

a40e = Entry(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we51)
a40e.grid(row=1, column=1)

a40be = Entry(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center",textvariable=we52)
a40be.grid(row=2, column=1)

a50e = Entry(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center",textvariable=we53)
a50e.grid(row=3, column=1)

textbanana = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
textbanana.grid(row=4, column=1)

textbrownie = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6,justify="center")
textbrownie.grid(row=5, column=1)

textpineapple = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
textpineapple.grid(row=6, column=1)

textchocolate = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
textchocolate.grid(row=7, column=1)

textblackforest = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
textblackforest.grid(row=8, column=1)

textblackforest1 = Label(cakesFrame1, font=('arial', 10, 'bold'), bd=7, width=6, justify="center")
textblackforest1.grid(row=9, column=1)


#costlabels & entry fields

labelCostofFood=Label(costFrame,text='البرستول',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=1,padx=41)

textCostofFood1=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=brestolvar)
textCostofFood1.grid(row=0,column=0)

labelCostofFood2=Label(costFrame,text='الكوشية',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood2.grid(row=1,column=1,padx=41)

textCostofFood3=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=kosahvar)
textCostofFood3.grid(row=1,column=0)


labelCostofFood4=Label(costFrame,text='الطبع الاماراتي',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood4.grid(row=2,column=1,padx=41)

textCostofFood5=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=tavar)
textCostofFood5.grid(row=2,column=0)


labelCostofFood6=Label(costFrame,text='الطبع البرتغالي',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood6.grid(row=0,column=3,padx=41)

textCostofFood7=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=tbvar)
textCostofFood7.grid(row=0,column=2)

labelCostofFood8=Label(costFrame,text='الدوبلكس ',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood8.grid(row=1,column=3,padx=41)

textCostofFood9=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=eldobleksvar)
textCostofFood9.grid(row=1,column=2)




labelCostofFood10=Label(costFrame,text='الاستيكر ',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood10.grid(row=2,column=3,padx=41)

textCostofFood2=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=telastekarvar)
textCostofFood2.grid(row=2,column=2)

labelCostofFood=Label(buttonFrame1,text='  ',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood.grid(row=4,column=2)

textCostofFood5=Entry(buttonFrame1,font=('arial',16,'bold'),bd=6,width=7,state='readonly',textvariable=total,justify='center')
textCostofFood5.grid(row=5,column=1)






#Buttons

buttonTotal=Button(buttonFrame1,text='الاجمــالي',font=('lithograph',15,'bold'),bg='orange',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame1,text='الفواتير ',font=('lithograph',15,'bold'),bg='GreenYellow',bd=3,padx=5
                     ,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonReset=Button(buttonFrame1,text='مسح',font=('lithograph',10,'bold'),bg='yellow',bd=3,padx=5,command=RESET
        )
buttonReset.grid(row=5,column=3)
buttonReset1=Button(buttonFrame1,text='الاسعـــار',font=('lithograph',15,'bold'),bg='red',bd=3,padx=3,command=pricelist
        )
buttonReset1.grid(row=0,column=3 )



#Calculator
operator='' #7+9
def buttonClick(numbeجنية): #9
    global operator
    operator=operator+numbeجنية
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''



calculatorField=Entry(calculatorFrame1,font=('arial',12,'bold'),width=30,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame1,text='7',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame1,text='8',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=6,
               command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame1,text='9',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame1,text='+',font=('arial',13,'bold'),fg='yellow',bg='red4',bd=6,width=6
                  ,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame1,text='4',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame1,text='5',font=('arial',12,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame1,text='6',font=('arial',12,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame1,text='ــ',font=('arial',13,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame1,text='1',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame1,text='2',font=('arial',12,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame1,text='3',font=('arial',12,'bold'),fg='red4',bg='white',bd=6,width=6
               ,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame1,text='*',font=('arial',14,'bold'),fg='yellow',bg='red4',bd=6,width=6
                  ,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame1,text='=',font=('arial',15,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                 command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame1,text='Clear',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=6
                   ,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame1,text='0',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=6
               ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame1,text='/',font=('arial',12,'bold'),fg='yellow',bg='red4',bd=6,width=6,
                 command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

###################



















root.mainloop()