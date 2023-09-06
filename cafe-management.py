from tkinter import *
import tkinter as tk
from datetime import datetime

class cafe_management():

        # ============== Total Bill Code =================

        def Total_Bill(self):
                self.Text_Receipt.delete(1.0,"end")
                self.tea_price = 10
                self.coffee_price = 20
                self.sandwitch_price = 50
                self.cake_price = 100
                self.burger_price = 50
                self.pizza_price = 150
                self.fries_price = 80
                self.pepsi_price = 80
                
                self.Text_Receipt.insert(tk.END,"  ***Receipt*** ")
                self.Text_Receipt.insert(tk.END,"\n\n Item      Price")

                if self.tea_item.get() != "":
                        self.tea_cost = self.tea_price * int(self.tea_item.get())
                        self.Text_Receipt.insert(tk.END,"\n Tea        ")
                        self.Text_Receipt.insert(tk.END,self.tea_cost)
                else:
                        self.tea_cost = 0
                if self.coffee_item.get() != "":
                        self.coffee_cost = self.coffee_price * int(self.coffee_item.get())
                        self.Text_Receipt.insert(tk.END,"\n Coffee     ")
                        self.Text_Receipt.insert(tk.END,self.coffee_cost)
                else:
                        self.coffee_cost = 0
                if self.sandwitch_item.get() != "":
                        self.sandwitch_cost = self.sandwitch_price * int(self.sandwitch_item.get())
                        self.Text_Receipt.insert(tk.END,"\n Sandwitch  ")
                        self.Text_Receipt.insert(tk.END,self.sandwitch_cost)
                else:
                        self.sandwitch_cost = 0
                if self.cake_item.get() != "":
                        self.cake_cost = self.cake_price * int(self.cake_item.get())
                        self.Text_Receipt.insert(tk.END,"\n Cake       ")
                        self.Text_Receipt.insert(tk.END,self.cake_cost)
                else:
                        self.cake_cost = 0
                if self.burger_item.get() != "":
                        self.burger_cost = self.burger_price * int(self.burger_item.get())
                        self.Text_Receipt.insert(tk.END,"\n Burger     ")
                        self.Text_Receipt.insert(tk.END,self.burger_cost)
                else:
                        self.burger_cost = 0
                if self.pizza_item.get() != "":
                        self.pizza_cost = self.pizza_price * int(self.pizza_item.get())
                        self.Text_Receipt.insert(tk.END,"\n Pizza      ")
                        self.Text_Receipt.insert(tk.END,self.pizza_cost)
                else:
                        self.pizza_cost = 0
                if self.fries_item.get() != "":
                        self.fries_cost = self.fries_price * int(self.fries_item.get())
                        self.Text_Receipt.insert(tk.END,"\n Fries      ")
                        self.Text_Receipt.insert(tk.END,self.fries_cost)
                else:
                        self.fries_cost = 0
                if self.pepsi_item.get() != "":
                        self.pepsi_cost = self.pepsi_price * int(self.pepsi_item.get())
                        self.Text_Receipt.insert(tk.END,"\n Pepsi      ")
                        self.Text_Receipt.insert(tk.END,self.pepsi_cost)
                else:
                        self.pepsi_cost = 0


                self.Total_Bill = self.pepsi_cost + self.fries_cost + self.pizza_cost +  self.burger_cost + self.cake_cost + self.sandwitch_cost + self.coffee_cost + self.tea_cost 
                
                if self.items_cost != "":
                        self.items_cost.delete(0,END)
                        self.items_cost.insert(END,self.Total_Bill)
                else:
                        self.items_cost.insert(END,self.Total_Bill)
                if self.service_cost != "":
                        self.service_cost.delete(0,END)
                        self.service_cost.insert(END,10.0)
                else:
                        self.service_cost.insert(END,10.0)
                if self.sub_cost != "":
                        self.sub_cost.delete(0,END)
                        self.sub_cost.insert(END,int(self.items_cost.get()) + float(self.service_cost.get()))
                else:
                        self.sub_cost.insert(END,int(self.items_cost.get()) + float(self.service_cost.get()))
                if self.paid_tax != "":
                        self.paid_tax.delete(0,END)
                        self.paid_tax.insert(END,float(self.sub_cost.get())*8/100)
                else:
                        self.paid_tax.insert(END,float(self.sub_cost.get())*8/100)

                if self.total_bill != "":
                        self.total_bill.delete(0,END)
                        self.total_bill.insert(END,float(self.sub_cost.get())+float(self.paid_tax.get()))
                else:
                        self.total_bill.insert(END,float(self.sub_cost.get())+float(self.paid_tax.get()))
                

                self.Text_Receipt.insert(tk.END,"\n\n ***Thank You***   visit again ")
                



        # =================== Clear Fields =============== 
        def clear(self):
                self.delete(0,"end")
        def Clear(self):
                self.tea_item.delete(0,"end")
                self.coffee_item.delete(0,"end")
                self.sandwitch_item.delete(0,"end")
                self.burger_item.delete(0,"end")
                self.cake_item.delete(0,"end")
                self.fries_item.delete(0,"end")
                self.pizza_item.delete(0,"end")
                self.pepsi_item.delete(0,"end")
                self.items_cost.delete(0,"end")
                self.service_cost.delete(0,"end")
                self.sub_cost.delete(0,"end")
                self.paid_tax.delete(0,"end")
                self.total_bill.delete(0,"end")
                self.Text_Receipt.delete(1.0,"end")

                #========== end ========================


        def __init__(self):
                self.root = tk.Tk()
                self.root.geometry('500x300')
                self.root.title("Cafe Management System")
                self.root.maxsize(500,300)
                self.root.minsize(500,300)
                self.root['bg'] = "white"

                self.heading = Label(self.root,text="Cafe Management System",font=('verdana',20,'bold'),fg="maroon",bg="white")
                self.heading.place(x=60,y=5)
                
                self.style1 = Label(self.root,bg="maroon",height=1,width=17)
                self.style1.place(x=0,y=50)
                self.style2 = Label(self.root,bg="maroon",height=1,width=30)
                self.style2.place(x=380,y=50)
                self.date = Label(self.root,text=datetime.now(),font=('verdana',10,'bold'),bg="white")
                self.date.place(x=140,y=50)

                # ================== Items ===================
                self.frame1 = LabelFrame(self.root,text="Cafe Items",width=150,height=200,font=('verdana',10,'bold'),borderwidth=3,relief=RIDGE,highlightthickness=4,bg="white",highlightcolor="white",highlightbackground="white",fg="maroon")
                self.frame1.place(x=20,y=90)
                
                self.tea = Label(self.frame1,text="Tea",font=('verdana',10,'bold'),bg="white")
                self.tea.place(x=3,y=1)
                self.tea_item = Entry(self.frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
                self.tea_item.place(y=1,x=85)

                self.coffee = Label(self.frame1,text="Coffee",font=('verdana',10,'bold'),bg="white")
                self.coffee.place(x=3,y=20)
                self.coffee_item = Entry(self.frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
                self.coffee_item.place(y=20,x=85)

                self.sandwitch = Label(self.frame1,text="Sandwitch",font=('verdana',10,'bold'),bg="white")
                self.sandwitch.place(x=3,y=40)
                self.sandwitch_item = Entry(self.frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
                self.sandwitch_item.place(y=40,x=85)

                self.cake = Label(self.frame1,text="Cake",font=('verdana',10,'bold'),bg="white")
                self.cake.place(x=3,y=60)
                self.cake_item = Entry(self.frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
                self.cake_item.place(y=60,x=85)

                self.burger = Label(self.frame1,text="Burger",font=('verdana',10,'bold'),bg="white")
                self.burger.place(x=3,y=80)
                self.burger_item = Entry(self.frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
                self.burger_item.place(y=80,x=85)

                self.pizza = Label(self.frame1,text="Pizza",font=('verdana',10,'bold'),bg="white")
                self.pizza.place(x=3,y=100)
                self.pizza_item = Entry(self.frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
                self.pizza_item.place(y=100,x=85)

                self.fries = Label(self.frame1,text="Fries",font=('verdana',10,'bold'),bg="white")
                self.fries.place(x=3,y=120)
                self.fries_item = Entry(self.frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
                self.fries_item.place(y=120,x=85)

                self.pepsi = Label(self.frame1,text="Pepsi",font=('verdana',10,'bold'),bg="white")
                self.pepsi.place(x=3,y=140)
                self.pepsi_item = Entry(self.frame1,width=7,borderwidth=4,relief=SUNKEN,bg="grey")
                self.pepsi_item.place(y=140,x=85)

                # ============ Items Bill =================

                self.frame2 = LabelFrame(self.root,text="Cafe Items Bills",width=180,height=160,font=('verdana',10,'bold'),borderwidth=3,relief=RIDGE,highlightthickness=4,bg="white",highlightcolor="white",highlightbackground="white",fg="maroon")
                self.frame2.place(x=170,y=120)

                self.item_cost_lb = Label(self.frame2,text="Items Cost",font=('verdana',10,'bold'),bg="white")
                self.item_cost_lb.place(x=3,y=1)
                self.items_cost = Entry(self.frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
                self.items_cost.place(y=1,x=100)

                self.service_cost_lb = Label(self.frame2,text="Service Cost",font=('verdana',10,'bold'),bg="white")
                self.service_cost_lb.place(x=3,y=20)
                self.service_cost = Entry(self.frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
                self.service_cost.place(y=20,x=100)

                self.sub_cost_lb = Label(self.frame2,text="Sub Cost",font=('verdana',10,'bold'),bg="white")
                self.sub_cost_lb.place(x=3,y=40)
                self.sub_cost = Entry(self.frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
                self.sub_cost.place(y=40,x=100)

                self.paid_tax_lb = Label(self.frame2,text="Paid Tax",font=('verdana',10,'bold'),bg="white")
                self.paid_tax_lb.place(x=3,y=80)
                self.paid_tax = Entry(self.frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
                self.paid_tax.place(y=80,x=100)

                self.total_bill_lb = Label(self.frame2,text="Total Bill",font=('verdana',10,'bold'),bg="white")
                self.total_bill_lb.place(x=3,y=100)
                self.total_bill = Entry(self.frame2,width=9,borderwidth=4,relief=SUNKEN,bg="grey")
                self.total_bill.place(y=100,x=100)

               #receipt

                self.Text_Receipt = Text(self.root,width=16,height=9,relief=SUNKEN,borderwidth=3)
                self.Text_Receipt.place(x=355,y=105)

                self.Total_Bills_btn = Button(self.root,text="Total",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='maroon',fg="white",command=self.Total_Bill)
                self.Total_Bills_btn.place(x=370,y=260)
                
                self.Clear_btn = Button(self.root,text="Clear",relief=RAISED,borderwidth=2,font=('verdana',10,'bold'),bg='maroon',fg="white",command=self.Clear)
                self.Clear_btn.place(x=420,y=260)

                self.root.mainloop()

cafe_management()
    


