from tkinter import *
from tkinter import ttk
import random
import time
from tkinter import messagebox
import sqlite3
root=Tk()
root.geometry("1366x700+0+0") 
root.title("RASTAURANT MANAGEMENT")
text_Input=StringVar()
operator=""
root.configure(background="#3198db")
Top=Frame(root,width=1600,height=50,bg="#3198db",relief=SUNKEN)
Top.pack(side=TOP)
left=Frame(root,width=800,height=700,bg="#ffffff",relief=SUNKEN)
left.pack(side=LEFT)
right=Frame(root,width=300,bg="#3198db",relief=SUNKEN)
right.pack(side=RIGHT)
global localtime
reciept=None
localtime=time.asctime(time.localtime(time.time()))
#=====================TIME================================
lblinf=Label(Top,font=('arial',50,'bold',"italic"),text="Restaurant Billing System",fg="Black",bd=10,anchor='w')
#=======================INFO======================================
lblinf.grid(row=0,column=0)
lblinf=Label(Top,font=('arial',20,'bold'),text=localtime,fg="Black",bd=10,anchor='w')
lblinf.grid(row=1,column=0)
#======================calculator
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_Input.set(operator)
def btnClick1():
    global operator
    operator=""
    text_Input.set(operator)
def btnequals():
    global operator
    sump=str(eval(operator))
    text_Input.set(sump)
    operator=""
def Ref():
    conn=sqlite3.connect("customer.db") #for connecting to the database
    conn.execute('''create table if not exists customer(CNAME TEXT NOT NULL)''')
    biler=str(Customer.get())
    CNAME=biler
    global count
    count=0
    row=[(CNAME)]
    conn.execute("Insert into customer(CNAME)values(?)",row)
    conn.commit()
    uname=conn.execute("select * from customer")
    for row in uname:
        if row[0]==biler:
            count+=1
    x=random.randint(10908,50786)
    global randof
    randof=str(x)
    rand.set(randof)
    global Cf
    global Cc
    global Cm
    global Ck
    global Cch
    global Cr
    global Cd
    if Fries.get()=="":
        Cf=0
    else:
        Cf=int(Fries.get())
    if Cb.get()=="":
        Cc=0
    else:
        Cc=int(Cb.get())
    if Mb.get()=="":
        Cm=0
    else:
        Cm=int(Mb.get())
    if Kabab.get()=="":
        Ck=0
    else:
        Ck=int(Kabab.get())
    if Chili.get()=="":
        Cch=0
    else:
        Cch=int(Chili.get())
    if Masala.get()=="":
        Cr=0
    else:
        Cr=int(Masala.get())
    if Drinks.get()=="":
        Cd=0
    else:
        Cd=int(Drinks.get())
    CostofFried=Cf*80.00
    CostofCBiriyani=Cc*100.00
    CostofMBiriyani=Cm*120.00
    CostofKabab=Ck*250.00
    CostofChili=Cch*200.00
    CostofRani=Cr*300.00
    CostofDrinks=Cd*20.00
    for i in range (20):
        if count>=2 and count<5 :
            CostofMeal="(10%discount)₹",str('%.2f'%((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.90))
            TotalCost=((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.90)
        elif count>=5 and count<10 :
            CostofMeal="(15%discount)₹",str('%.2f'%((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.90))
            TotalCost=((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.85)
        elif count>=10 and count<15 :
            CostofMeal="(20%discount)₹",str('%.2f'%((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.90))
            TotalCost=((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.80)
        elif count>=15:
            CostofMeal="(25%discount)₹",str('%.2f'%((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.90))
            TotalCost=((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.75)
        else:
            CostofMeal="₹",str('%.2f'%(CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks))
            TotalCost=(CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)
    PayTax=((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.27)    
    Ser_Charge=((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)/99)
    service="₹",str('%.2f'%Ser_Charge)
    OverAllCost="₹",str('%.2f'%(PayTax+TotalCost+Ser_Charge))
    PaidTax="₹",str('%.2f'%PayTax)
    Service.set(service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    Subtotal.set(CostofMeal)
    Total.set(OverAllCost)
    f1=open('bill.txt','w')
    f1.write("\n\n                          SILVERSPOON RESTAURANT PAYING BILL\n")
    f1.write("-----------------------------------------------------------------------------------------------------\n")
    f1.write("\t\t\t\t\t\t\t\t\t\t\t\t")
    f1.write(localtime)
    f1.write("\n")
    f1.write("Referrence ID:                                                 ")
    f1.write(randof)
    f1.write("\n\n\n\n")
    f1.write("Customer Name:                                                 ")
    f1.write(biler)
    f1.write("\n\n\n\n")
    if count>=2:
        f1.write("Total cost of meal:                                            ")
        f1.write(str((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)*0.90))
    else:
        f1.write("Total cost of meal:                                            ")
        f1.write(str((CostofFried+CostofCBiriyani+CostofMBiriyani+CostofKabab+CostofChili+CostofRani+CostofDrinks)))
    f1.write("\n\n\n\n") 
    f1.write("All Taxes Included:                                            ")
    f1.write(str('%.2f'%PayTax))
    f1.write("\n\n\n\n")
    f1.write("Service Charge:                                                ")
    f1.write(str('%.2f'%Ser_Charge))
    f1.write("\n")
    f1.write("____________________________________________________________________________\n")
    f1.write("Total Cost:                                                    ")
    f1.write(str('%.2f'%(PayTax+TotalCost+Ser_Charge)))
    f1.write("\n\n\n")
    if count>=2 and count<5 :
        f1.write("You are our old customer Mr.")
        f1.write(biler)
        f1.write("You have come here ")
        f1.write(str(count))
        f1.write("times")
        f1.write("\n\n")
        f1.write("So,you are getting 10% discount!!!!")
        f1.write("\n\n")
    elif count>=5 and count<10 :
        f1.write("You are our old customer Mr.")
        f1.write(biler)
        f1.write(". You have come here ")
        f1.write(str(count))
        f1.write(" times.")
        f1.write("\n\n")
        f1.write("So,you are getting 15% discount!!!!")
        f1.write("\n\n")
    elif count>=10 and count<15 :
        f1.write("You are our old customer Mr.")
        f1.write(biler)
        f1.write("You have come here ")
        f1.write(str(count))
        f1.write("times")
        f1.write("\n\n")
        f1.write("So,you are getting 20% discount!!!!")
        f1.write("\n\n")
    elif count>=15 :
        f1.write("You are our old customer Mr.")
        f1.write(biler)
        f1.write("You have come here ")
        f1.write(str(count))
        f1.write("times")
        f1.write("\n\n")
        f1.write("So,you are getting 25% discount!!!!")
        f1.write("\n\n")
    else:
        f1.write("You are our brand new customer Mr.")
        f1.write(biler)
        f1.write("\n\n")
        f1.write("So,you are getting no discount!!!!")
        f1.write("\n\n")
    f1.write("HAVE A NICE DAY...........THANK YOU FOR COMING")
def Receipt():
    reciept=Tk()
    reciept.title("Reciept")
    global Cf
    global Cc
    global Cm
    global Ck
    global Cch
    global Cr
    global Cd
    txtReceipt.delete("1.0", END)
    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref.set("BILL" + randomRef)

    txtReceipt.insert(END, 'Receipt Ref: \t\t\t'+Receipt_Ref.get()+"\t\t\t"+DateofOrder.get()+"\n")
    txtReceipt.insert(END, 'Items\t\t\t'+'Quantity\t\t\t'+"Price \n\n")

    if Cf > 0:
        txtReceipt.insert(END, 'Latte:\t\t\t'+str(Cf)+'\t\t\t'+str('$%.2f'%(CostofFried))+'\n')
    if Cc > 0:
        txtReceipt.insert(END, 'Espresso:\t\t\t'+str(Cc)+'\t\t\t'+str('$%.2f'%(CostofCBiriyani))+'\n')
    if Cm > 0:
        txtReceipt.insert(END, 'Iced Latte:\t\t\t'+str(Cm)+'\t\t\t'+str('$%.2f'%(CostofMBiriyani))+'\n')
    if Ck > 0:
        txtReceipt.insert(END, 'Vale Coffee:\t\t\t'+str(Ck)+'\t\t\t'+str('$%.2f'%(CostofKabab))+'\n')
    if Cch > 0:
        txtReceipt.insert(END, 'Cappuccino:\t\t\t'+str(Cch)+'\t\t\t'+str('$%.2f'%(CostofChili))+'\n')
    if Cr > 0:
        txtReceipt.insert(END, 'African Coffee:\t\t\t'+str(Cr)+'\t\t\t'+str('$%.2f'%(CostofRani))+'\n')
    if Cd > 0:
        txtReceipt.insert(END, 'American Coffee:\t\t\t'+str(Cd)+'\t\t\t'+str('$%.2f'%(CostofDrinks))+'\n')
    txtReceipt.insert(END, '\nCost of Meals:\t'+CostofMeal+"\tTax Paid:\t"+ PaidTax.get()+"\n")
    txtReceipt.insert(END, 'Service Charge:\t'+service+"\tSubTotal:\t"+CostofMeal+"\n")
    txtReceipt.insert(END, "\tTotal Cost:\t"+OverAllCost+"\n")
def Quit():
    root.destroy()
def Reset():
    rand.set("")
    Fries.set("")
    Cb.set("")
    Mb.set("")
    Kabab.set("")
    Chili.set("")
    Customer.set("")
    Cost.set("")
    Drinks.set("")
    Masala.set("")
    Tax.set("")
    Service.set("")
    Subtotal.set("")
    Total.set("")
        
txtdisp=Entry(right,font=('arial',20,'bold'),textvariable=text_Input,bg="#2d8e9a",bd=20,insertwidth=5,justify='left')
txtdisp.grid(columnspan=7)
btn7=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="7",bg="#2d8e9a",command=lambda:btnClick(7)).grid(row=1,column=0)
btn8=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="8",bg="#2d8e9a",command=lambda:btnClick(8)).grid(row=1,column=1)
btn9=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="9",bg="#2d8e9a",command=lambda:btnClick(9)).grid(row=1,column=2)
btnplus=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="+",bg="#2d8e9a",command=lambda:btnClick("+")).grid(row=1,column=3)
btn4=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="4",bg="#2d8e9a",command=lambda:btnClick(4)).grid(row=2,column=0)
btn5=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="5",bg="#2d8e9a",command=lambda:btnClick(5)).grid(row=2,column=1)
btn6=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="6",bg="#2d8e9a",command=lambda:btnClick(6)).grid(row=2,column=2)
btnminus=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="-",bg="#2d8e9a",command=lambda:btnClick("-")).grid(row=2,column=3)
btn1=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="1",bg="#2d8e9a",command=lambda:btnClick(1)).grid(row=3,column=0)
btn2=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="2",bg="#2d8e9a",command=lambda:btnClick(2)).grid(row=3,column=1)
btn3=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="3",bg="#2d8e9a",command=lambda:btnClick(3)).grid(row=3,column=2)
btnmul=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="x",bg="#2d8e9a",command=lambda:btnClick("*")).grid(row=3,column=3)
btn0=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="0",bg="#2d8e9a",command=lambda:btnClick(0)).grid(row=4,column=0)
btncc=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="C",bg="#2d8e9a",command=btnClick1).grid(row=4,column=1)
btnpoi=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text=".",bg="#2d8e9a",command=lambda:btnClick(".")).grid(row=4,column=2)
btndiv=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),text="/",bg="#2d8e9a",command=lambda:btnClick("/")).grid(row=4,column=3)
btnequals=Button(right,padx=16,pady=16,bd=8,fg="black",font=('arial',12,'bold'),width=26,text="=",bg="#2d8e9a",command=btnequals).grid(row=5,column=0,columnspan=4)
#===========================
rand=StringVar()
Fries=StringVar()
Cb=StringVar()
Mb=StringVar()
Kabab=StringVar()
Chili=StringVar()
Customer=StringVar()
Cost=StringVar()
Drinks=StringVar()
Masala=StringVar()
Tax=StringVar()
Service=StringVar()
Subtotal=StringVar()
Total=StringVar()


lblreference=Label(left,font=('arial',12,'bold'),text="\nReffernce" ,bg="#ffffff",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
lblreference=Entry(left,font=('arial',12,'bold'),textvariable=rand, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lblreference.grid(row=0,column=1)
lbl1=Label(left,font=('arial',12,'bold'),text="Fried-Rice\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=1,column=0)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=1,column=1)
lbl1=Label(left,font=('arial',12,'bold'),text="Chicken-Biriyani\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=2,column=0)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Cb, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=2,column=1)
lbl1=Label(left,font=('arial',12,'bold'),text="Mutton-Biriyani\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=3,column=0)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Mb, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=3,column=1)
lbl1=Label(left,font=('arial',12,'bold'),text="Kabab\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=4,column=0)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Kabab, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=4,column=1)
lbl1=Label(left,font=('arial',12,'bold'),text="Chili-Chicken\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=5,column=0)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Chili, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=5,column=1)
lbl1=Label(left,font=('arial',12,'bold'),text="Chicken\nRani-Masala",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=6,column=0)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Masala, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=6,column=1)
lbl1=Label(left,font=('arial',12,'bold'),text="80₹ per plate",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=1,column=2)
lbl1=Label(left,font=('arial',12,'bold'),text="100₹ per plate",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=2,column=2)
lbl1=Label(left,font=('arial',12,'bold'),text="120₹ per plate",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=3,column=2)
lbl1=Label(left,font=('arial',12,'bold'),text="     250₹ per 8 pieces",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=4,column=2)
lbl1=Label(left,font=('arial',12,'bold'),text="     200₹ per 8 piece",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=5,column=2)
lbl1=Label(left,font=('arial',12,'bold'),text="     300₹ per 8 piece",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=6,column=2)
lbl1=Label(left,font=('arial',12,'bold'),text="Customer\nName",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=0,column=3)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Customer,bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=0,column=4)
lbl1=Label(left,font=('arial',12,'bold'),text="Drinks\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=1,column=3)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=1,column=4)
lbl1=Label(left,font=('arial',12,'bold'),text="Cost of Meal\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=2,column=3)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Cost, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=2,column=4)
lbl1=Label(left,font=('arial',12,'bold'),text="Tax\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=3,column=3)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Tax, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=3,column=4)
lbl1=Label(left,font=('arial',12,'bold'),text="Service\nCharge",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=4,column=3)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Service, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=4,column=4)
lbl1=Label(left,font=('arial',12,'bold'),text="Subtotal\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=5,column=3)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Subtotal, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=5,column=4)
lbl1=Label(left,font=('arial',12,'bold'),text="Total Cost\n",bg="#ffffff",bd=10,anchor='w')
lbl1.grid(row=6,column=3)
lbl1=Entry(left,font=('arial',12,'bold'),textvariable=Total, bd=10,insertwidth=4,bg="yellow",fg="black",justify='right')
lbl1.grid(row=6,column=4)
#========BUTTON-============================================
btnTotal=Button(left,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="#eee9a7",command=Ref).grid(row=7,column=1)
btnReceipt=Button(left,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reciept",bg="#eee9a7",command=Receipt).grid(row=7,column=2)
btnReset=Button(left,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="#eee9a7",command=Reset).grid(row=7,column=3)
btnQuit=Button(left,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Quit",bg="#eee9a7",command=Quit).grid(row=7,column=3)



root.mainloop()
