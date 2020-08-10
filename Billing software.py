from tkinter import *
import math,random
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Billing Software")
        self.root.geometry("1350x700+0+0")
        bg_color="#074463"

        title=Label(self.root,text="Billing Software",bd=10,relief=GROOVE,font=("Times New Roman",40,"bold"),bg=bg_color,fg="white")
        title.pack(side=TOP,fill=X)

        ################################## VARIABLES ###########################################

        ################ COSMETICS ############################################
        self.soap=IntVar()
        self.face_c=IntVar()
        self.face_w=IntVar()
        self.haire_s=IntVar()
        self.wax=IntVar()
        self.body_l=IntVar()

        ######################## GROCERY #########################################
        self.rice=IntVar()
        self.food_o=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()

        ########################### COLDRINKS #####################################

        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbsup=IntVar()
        self.limka=IntVar()
        self.sprite=IntVar()

        ############################# SAUCE #####################################

        self.barbeque_s=IntVar()
        self.tomato_s=IntVar()
        self.redchilly_s=IntVar()
        self.schezwan_s=IntVar()
        self.soy_s=IntVar()
        self.marinara_s=IntVar()

        ############################ TOTAL PRICE AND TAX #################################

        self.cosmetics_price=StringVar()
        self.grocery_price=StringVar()
        self.coldrinks_price=StringVar()
        self.sauce_price=StringVar()

        self.cosmetics_tax=StringVar()
        self.grocery_tax=StringVar()
        self.coldrinks_tax=StringVar()
        self.sauce_tax=StringVar()


        ############################# CUSTOMER ##############################################

        self.c_name=StringVar()
        self.c_phone=StringVar()

        self.bill_n=StringVar()
        x=random.randint(1000,9999)
        self.bill_n.set(str(x))

        self.search_bill=StringVar()


        ############################## CUSTOMER DETAILS #########################################
        F1=LabelFrame(self.root,text="Customer Details",bd=5,font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="white",font=("Times New Roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=20,textvariable=self.c_name,font="arial,18",bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphn_lbl=Label(F1,text="Phone No",bg=bg_color,fg="white",font=("Times New Roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=20,textvariable=self.c_phone,font="arial,18",bd=5,relief=SUNKEN).grid(row=0,column=3,padx=20,pady=5)

        c_billno_lbl=Label(F1,text="Bill No",bg=bg_color,fg="white",font=("Times New Roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_billno_txt=Entry(F1,width=20,textvariable=self.bill_n,font="arial,18",bd=5,relief=SUNKEN).grid(row=0,column=5,padx=20,pady=5)

        btn_bill=Button(F1,text="search",width=10,textvariable=self.search_bill,bd=5,font=("arial,12,bold")).grid(row=0,column=6,padx=10,pady=5)


        ############################# COSMETICS ##########################################################

        F2=LabelFrame(self.root,text="Cosmetics",bd=10,font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=10,y=160,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=0,column=0)
        bath_txt=Entry(F2,relief=SUNKEN,textvariable=self.soap,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        face_cream_lbl=Label(F2,text="Face Cream",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=1,column=0)
        face_cream_txt=Entry(F2,relief=SUNKEN,textvariable=self.face_c,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        face_w_lbl=Label(F2,text="Face Wash",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=2,column=0)
        face_w_txt=Entry(F2,relief=SUNKEN,textvariable=self.face_w,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        hair_s_lbl=Label(F2,text="Hair Spray",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=3,column=0)
        hair_s_txt=Entry(F2,relief=SUNKEN,textvariable=self.haire_s,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        Wax_lbl=Label(F2,text="Wax",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=4,column=0)
        Wax_txt=Entry(F2,relief=SUNKEN,textvariable=self.wax,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=4,column=1,padx=10,pady=10,sticky="w")


        body_l_lbl=Label(F2,text="Body Loshan",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=5,column=0)
        body_l_txt=Entry(F2,relief=SUNKEN,textvariable=self.body_l,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=5,column=1,padx=10,pady=10,sticky="w")

########################################## GROCERY ######################################################

        F3=LabelFrame(self.root,text="Grocery",bd=10,font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=340,y=160,width=325,height=380)

        G1_lbl=Label(F3,text="Rice",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=0,column=0)
        G1_txt=Entry(F3,relief=SUNKEN,textvariable=self.rice,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        G2_lbl=Label(F3,text="Food Oil",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=1,column=0)
        G2_txt=Entry(F3,relief=SUNKEN,textvariable=self.food_o,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        G3_lbl=Label(F3,text="Daal",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=2,column=0)
        G3_txt=Entry(F3,relief=SUNKEN,textvariable=self.daal,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        G4_lbl=Label(F3,text="Wheat",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=3,column=0)
        G4_txt=Entry(F3,relief=SUNKEN,textvariable=self.wheat,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        G5_lbl=Label(F3,text="Sugar",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=4,column=0)
        G5_txt=Entry(F3,relief=SUNKEN,textvariable=self.sugar,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=4,column=1,padx=10,pady=10,sticky="w")

        G6_lbl=Label(F3,text="Tea",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=5,column=0)
        G6_txt=Entry(F3,relief=SUNKEN,textvariable=self.tea,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=5,column=1,padx=10,pady=10,sticky="w")

########################################### coldrinks ##########################################################

        F4=LabelFrame(self.root,text="Coldrinks",bd=10,font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=670,y=160,width=325,height=380)

        p1_lbl=Label(F4,text="Maza",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=0,column=0)
        p1_txt=Entry(F4,relief=SUNKEN,textvariable=self.maza,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        p2_lbl=Label(F4,text="Cock",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=1,column=0)
        p2_txt=Entry(F4,relief=SUNKEN,textvariable=self.cock,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        p3_lbl=Label(F4,text="Frooti",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=2,column=0)
        p3_txt=Entry(F4,relief=SUNKEN,textvariable=self.frooti,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        p4_lbl=Label(F4,text="Thumbs Up",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=3,column=0)
        p4_txt=Entry(F4,relief=SUNKEN,textvariable=self.thumbsup,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        p5_lbl=Label(F4,text="Limka",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=4,column=0)
        p5_txt=Entry(F4,relief=SUNKEN,textvariable=self.limka,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=4,column=1,padx=10,pady=10,sticky="w")

        p6_lbl=Label(F4,text="Sprite",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=5,column=0)
        p6_txt=Entry(F4,relief=SUNKEN,textvariable=self.sprite,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=5,column=1,padx=10,pady=10,sticky="w")

########################################## SAUCE ##############################################################

        F5=LabelFrame(self.root,text="Sauce",bd=10,font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        F5.place(x=1000,y=160,width=325,height=380)

        c1_lbl=Label(F5,text="Barbecue Sauce",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=0,column=0)
        c1_txt=Entry(F5,relief=SUNKEN,textvariable=self.barbeque_s,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=0,column=1,padx=10,pady=10,sticky="w")

        c2_lbl=Label(F5,text="tomato sauce",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=1,column=0)
        c2_txt=Entry(F5,relief=SUNKEN,textvariable=self.tomato_s,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=1,column=1,padx=10,pady=10,sticky="w")

        c3_lbl=Label(F5,text="red chilli sauce",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=2,column=0)
        c3_txt=Entry(F5,relief=SUNKEN,textvariable=self.redchilly_s,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=2,column=1,padx=10,pady=10,sticky="w")

        c4_lbl=Label(F5,text="schezwan sauce",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=3,column=0)
        c4_txt=Entry(F5,relief=SUNKEN,textvariable=self.schezwan_s,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=3,column=1,padx=10,pady=10,sticky="w")

        c5_lbl=Label(F5,text="Soy sauce",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=4,column=0)
        c5_txt=Entry(F5,relief=SUNKEN,textvariable=self.soy_s,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=4,column=1,padx=10,pady=10,sticky="w")

        c6_lbl=Label(F5,text="Marinara sauce",bg=bg_color,fg="Lightgreen",font=("Times New Roman",16,"bold")).grid(row=5,column=0)
        c6_txt=Entry(F5,relief=SUNKEN,textvariable=self.marinara_s,font=("Times New Roman",15,"bold"),bd=5,width=13).grid(row=5,column=1,padx=10,pady=10,sticky="w")

############################################## BILL ####################################################################

        F6=Frame(self.root,bd=10,relief=GROOVE)
        F6.place(x=1340,y=160,width=380,height=380)

        bill_title=Label(F6,text="Bill Area",bd=5,relief=GROOVE,font=("arial 15 bold")).pack(fill=X)
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

#########################  BUTTION FRAME ##################################################################

        F7=LabelFrame(self.root,text="Bill Menu",bd=10,font=("Times New Roman",15,"bold"),fg="gold",bg=bg_color)
        F7.place(x=0,y=543,relwidth=1,height=175)

        m1_lbl=Label(F7,text="Total Cosmetics Price",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F7,width=18,bd=7,textvariable=self.cosmetics_price,relief=SUNKEN,font=("areal 10 bold")).grid(row=0,column=1,padx=10,pady=1,sticky="w")

        m2_lbl=Label(F7,text="Total Grocery Price",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F7,width=18,bd=7,textvariable=self.grocery_price,relief=SUNKEN,font=("areal 10 bold")).grid(row=1,column=1,padx=10,pady=1,sticky="w")

        m3_lbl=Label(F7,text="Total Coldrinks Price",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F7,width=18,bd=7,textvariable=self.coldrinks_price,relief=SUNKEN,font=("areal 10 bold")).grid(row=2,column=1,padx=10,pady=1,sticky="w")

        m4_lbl=Label(F7,text="Total Sauce Price",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky="w")
        m4_txt=Entry(F7,width=18,bd=7,textvariable=self.sauce_price,relief=SUNKEN,font=("areal 10 bold")).grid(row=3,column=1,padx=10,pady=1,sticky="w")

######################### TAX ################################################################

        C1_lbl=Label(F7,text="Cosmetics Tax",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        C1_txt=Entry(F7,width=18,bd=7,textvariable=self.cosmetics_tax,relief=SUNKEN,font=("areal 10 bold")).grid(row=0,column=3,padx=10,pady=1,sticky="w")

        C2_lbl=Label(F7,text="Grocery Tax",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        C2_txt=Entry(F7,width=18,bd=7,textvariable=self.grocery_tax,relief=SUNKEN,font=("areal 10 bold")).grid(row=1,column=3,padx=10,pady=1,sticky="w")

        C3_lbl=Label(F7,text="Coldrinks Tax",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        C3_txt=Entry(F7,width=18,bd=7,textvariable=self.coldrinks_tax,relief=SUNKEN,font=("areal 10 bold")).grid(row=2,column=3,padx=10,pady=1,sticky="w")

        C4_lbl=Label(F7,text="Sauce Tax",bg=bg_color,fg="white",font=("Times New Roman",14,"bold")).grid(row=3,column=2,padx=20,pady=1,sticky="w")
        C4_txt=Entry(F7,width=18,bd=7,textvariable=self.sauce_tax,relief=SUNKEN,font=("areal 10 bold")).grid(row=3,column=3,padx=10,pady=1,sticky="w")

        btn_f=Frame(F7,bd=7,relief=GROOVE)
        btn_f.place(x=720,width=580,height=140)

############################### BUTTON #############################################################

        total_btn=Button(btn_f,command=self.total,text="Total",bd=2,bg="cadetblue",fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=5,pady=5)
        Bill_btn=Button(btn_f,text="Bill",command=self.welcome_bill,bd=2,bg="cadetblue",fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=5,pady=5)
        Clear_btn=Button(btn_f,text="Clear",bd=2,bg="cadetblue",fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=5)
        Exit_btn=Button(btn_f,text="Exit",bd=2,bg="cadetblue",fg="white",pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()

    def total(self):
            self.total_cosmetics_price=float(
                                        (self.soap.get()*40)+
                                        (self.face_c.get()*120)+
                                        (self.face_w.get()*100)+
                                        (self.haire_s.get()*180)+
                                        (self.wax.get()*30)+
                                        (self.body_l.get()*55)
                                        )

            self.cosmetics_price.set("Rs. "+str(self.total_cosmetics_price))
            self.cosmetics_tax.set("Rs. "+str(round((self.total_cosmetics_price*0.05),2)))




            self.total_grocery_price=float(
                                        (self.rice.get()*60)+
                                        (self.food_o.get()*120)+
                                        (self.daal.get()*100)+
                                        (self.wheat.get()*80)+
                                        (self.sugar.get()*78)+
                                        (self.tea.get()*52)
                                        )

            self.grocery_price.set("Rs. "+str(self.total_grocery_price))
            self.grocery_tax.set("Rs. " + str(round((self.total_grocery_price*0.05),2)))




            self.total_coldrinks_price = float(
                                        (self.maza.get()*60) +
                                        (self.cock.get()*60) +
                                        (self.frooti.get()*55) +
                                        (self.thumbsup.get()*60) +
                                        (self.limka.get()*50) +
                                        (self.sprite.get()*60)
                                        )

            self.coldrinks_price.set("Rs. "+str(self.total_coldrinks_price))
            self.coldrinks_tax.set("Rs. " + str(round((self.total_coldrinks_price*0.05),2)))




            self.total_sauce_price=float(
                                        (self.barbeque_s.get()*60)+
                                        (self.tomato_s.get()*40)+
                                        (self.redchilly_s.get()*45)+
                                        (self.schezwan_s.get()*30)+
                                        (self.soy_s.get()*40)+
                                        (self.marinara_s.get()*60)
                                        )

            self.sauce_price.set("Rs. "+str(self.total_sauce_price))
            self.sauce_tax.set("Rs. " + str(round((self.total_sauce_price*0.05),2)))

    def welcome_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\twelcome webcode retail\n")
            self.txtarea.insert(END, f"\n Bill Number:{self.bill_n.get()}")
            self.txtarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
            self.txtarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
            self.txtarea.insert(END, f"\n=======================================")
            self.txtarea.insert(END, f"\n Products\t\tQTY\t\tprice")
            self.txtarea.insert(END, f"\n=======================================")




    def Bill_Area(self):
            pass










root=Tk()
obj=Bill_App(root)
root.mainloop()
