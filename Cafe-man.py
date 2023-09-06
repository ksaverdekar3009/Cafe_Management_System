from tkinter import *
import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.geometry('500x300')
root.title("Cafe Management System")
root.maxsize(500,300)
root.minsize(500,300)
root['bg'] = "white"

heading = Label(root,text="Cafe Management System",font=('verdana',20,'bold'),fg="maroon",bg="white")
heading.place(x=60,y=5)
                
style1 = Label(root,bg="maroon",height=1,width=17)
style1.place(x=0,y=50)
style2 = Label(root,bg="maroon",height=1,width=30)
style2.place(x=380,y=50)
date = Label(root,text=datetime.now(),font=('verdana',10,'bold'),bg="white")
date.place(x=140,y=50)
        # ============== Total Bill Code =================

def Total_Bill():
    Text_Receipt.delete(1.0,"end")
    tea_price = 10
    coffee_price = 20
    sandwitch_price = 50
    cake_price = 100
    burger_price = 50
    pizza_price = 150
    fries_price = 80
    pepsi_price = 80
              
    Text_Receipt.insert(tk.END,"  ***Receipt*** ")
    Text_Receipt.insert(tk.END,"\n\n Item      Price")

    if tea_item.get() != "":
        tea_cost = tea_price * int(tea_item.get())
        Text_Receipt.insert(tk.END,"\n Tea        ")
        Text_Receipt.insert(tk.END,tea_cost)
    else:
        tea_cost = 0
    if coffee_item.get() != "":
        coffee_cost = coffee_price * int(coffee_item.get())
        Text_Receipt.insert(tk.END,"\n Coffee     ")
        Text_Receipt.insert(tk.END,coffee_cost)
    else:
        coffee_cost = 0
    if sandwitch_item.get() != "":
        sandwitch_cost = sandwitch_price * int(sandwitch_item.get())
        Text_Receipt.insert(tk.END,"\n Sandwitch  ")
        Text_Receipt.insert(tk.END,sandwitch_cost)
    else:
        sandwitch_cost = 0
    if cake_item.get() != "":
        cake_cost = cake_price * int(cake_item.get())
        Text_Receipt.insert(tk.END,"\n Cake       ")
        Text_Receipt.insert(tk.END,cake_cost)
    else:
        cake_cost = 0
    if burger_item.get() != "":
        burger_cost = burger_price * int(burger_item.get())
        Text_Receipt.insert(tk.END,"\n Burger     ")
        Text_Receipt.insert(tk.END,burger_cost)
    else:
        burger_cost = 0
    if pizza_item.get() != "":
        pizza_cost = pizza_price * int(pizza_item.get())
        Text_Receipt.insert(tk.END,"\n Pizza      ")
        Text_Receipt.insert(tk.END,pizza_cost)
    else:
        pizza_cost = 0
    if fries_item.get() != "":
        fries_cost = fries_price * int(fries_item.get())
        Text_Receipt.insert(tk.END,"\n Fries      ")
        Text_Receipt.insert(tk.END,fries_cost)
    else:
        fries_cost = 0
    if pepsi_item.get() != "":
        pepsi_cost = pepsi_price * int(pepsi_item.get())
        Text_Receipt.insert(tk.END,"\n Pepsi      ")
        Text_Receipt.insert(tk.END,pepsi_cost)
    else:
        pepsi_cost = 0


    Total_Bill = pepsi_cost + fries_cost + pizza_cost +  burger_cost + cake_cost + sandwitch_cost + coffee_cost + tea_cost 
                
    if items_cost != "":
        items_cost.delete(0,END)
        items_cost.insert(END,Total_Bill)
    else:
        items_cost.insert(END,Total_Bill)
    if service_cost != "":
        service_cost.delete(0,END)
        service_cost.insert(END,10.0)
    else:
        service_cost.insert(END,10.0)
    if sub_cost != "":
        sub_cost.delete(0,END)
        sub_cost.insert(END,int(items_cost.get()) + float(service_cost.get()))
    else:
        sub_cost.insert(END,int(items_cost.get()) + float(service_cost.get()))
    if paid_tax != "":
        paid_tax.delete(0,END)
        paid_tax.insert(END,float(sub_cost.get())*8/100)
    else:
        paid_tax.insert(END,float(sub_cost.get())*8/100)

    if total_bill != "":
        total_bill.delete(0,END)
        total_bill.insert(END,float(sub_cost.get())+float(paid_tax.get()))
    else:
        total_bill.insert(END,float(sub_cost.get())+float(paid_tax.get()))
                

    Text_Receipt.insert(tk.END,"\n\n ***Thank You***   visit again ")
                



        # =================== Clear Fields =============== 

def Clear():
        tea_item.delete(0,"end")
        coffee_item.delete(0,"end")
        sandwitch_item.delete(0,"end")
        burger_item.delete(0,"end")
        cake_item.delete(0,"end")
        fries_item.delete(0,"end")
        pizza_item.delete(0,"end")
        pepsi_item.delete(0,"end")
        items_cost.delete(0,"end")
        service_cost.delete(0,"end")
        sub_cost.delete(0,"end")
        paid_tax.delete(0,"end")
        total_bill.delete(0,"end")
        Text_Receipt.delete(1.0,"end")

    #========== end ========================
                

    # ================== Items ===================
frame1 = LabelFrame(root,text="Cafe Items",width=150,height=200,font=('verdana',10,'bold'),borderwidth=3,relief=RIDGE,highlightthickness=4,bg="white",highlightcolor="white",highlightbackground="white",fg="maroon")
frame1.place(x=20,y=90)
                
tea = Label(frame1,text="Tea",font=('verdana',10,'bold'),bg="white")
tea.place(x=3,y=1)
tea_item = Entry(frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
tea_item.place(y=1,x=85)

coffee = Label(frame1,text="Coffee",font=('verdana',10,'bold'),bg="white")
coffee.place(x=3,y=20)
coffee_item = Entry(frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
coffee_item.place(y=20,x=85)

sandwitch = Label(frame1,text="Sandwitch",font=('verdana',10,'bold'),bg="white")
sandwitch.place(x=3,y=40)
sandwitch_item = Entry(frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
sandwitch_item.place(y=40,x=85)

cake = Label(frame1,text="Cake",font=('verdana',10,'bold'),bg="white")
cake.place(x=3,y=60)
cake_item = Entry(frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
cake_item.place(y=60,x=85)

burger = Label(frame1,text="Burger",font=('verdana',10,'bold'),bg="white")
burger.place(x=3,y=80)
burger_item = Entry(frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
burger_item.place(y=80,x=85)

pizza = Label(frame1,text="Pizza",font=('verdana',10,'bold'),bg="white")
pizza.place(x=3,y=100)
pizza_item = Entry(frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
pizza_item.place(y=100,x=85)

fries = Label(frame1,text="Fries",font=('verdana',10,'bold'),bg="white")
fries.place(x=3,y=120)
fries_item = Entry(frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
fries_item.place(y=120,x=85)

pepsi = Label(frame1,text="Pepsi",font=('verdana',10,'bold'),bg="white")
pepsi.place(x=3,y=140)
pepsi_item = Entry(frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
pepsi_item.place(y=140,x=85)

    # ============ Items Bill =================

frame2 = LabelFrame(root,text="Cafe Items Bills",width=180,height=160,font=('verdana',10,'bold'),borderwidth=3,relief=RIDGE,highlightthickness=4,bg="white",highlightcolor="white",highlightbackground="white",fg="maroon")
frame2.place(x=170,y=120)

item_cost_lb = Label(frame2,text="Items Cost",font=('verdana',10,'bold'),bg="white")
item_cost_lb.place(x=3,y=1)
items_cost = Entry(frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
items_cost.place(y=1,x=100)

service_cost_lb = Label(frame2,text="Service Cost",font=('verdana',10,'bold'),bg="white")
service_cost_lb.place(x=3,y=20)
service_cost = Entry(frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
service_cost.place(y=20,x=100)

sub_cost_lb = Label(frame2,text="Sub Cost",font=('verdana',10,'bold'),bg="white")
sub_cost_lb.place(x=3,y=40)
sub_cost = Entry(frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
sub_cost.place(y=40,x=100)

paid_tax_lb = Label(frame2,text="Paid Tax",font=('verdana',10,'bold'),bg="white")
paid_tax_lb.place(x=3,y=80)
paid_tax = Entry(frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
paid_tax.place(y=80,x=100)

total_bill_lb = Label(frame2,text="Total Bill",font=('verdana',10,'bold'),bg="white")
total_bill_lb.place(x=3,y=100)
total_bill = Entry(frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
total_bill.place(y=100,x=100)

    #receipt

Text_Receipt = Text(root,width=16,height=9,relief=SUNKEN,borderwidth=3)
Text_Receipt.place(x=355,y=105)

Total_Bills_btn = Button(root,text="Total",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='maroon',fg="white",command=Total_Bill)
Total_Bills_btn.place(x=370,y=260)
                
Clear_btn = Button(root,text="Clear",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='maroon',fg="white",command=Clear)
Clear_btn.place(x=420,y=260)

root.mainloop()
