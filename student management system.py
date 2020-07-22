from tkinter import *
from tkinter import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("Times New Roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X)

############################### ALL VARIBLES #####################################################
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.dob_var=StringVar()
        self.contact_var=StringVar()








  ############################ MANAGE_FRAME ######################################
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Student",bg="crimson",fg="white",font=("Times New Roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)


        lbl_roll=Label(Manage_Frame,text="Roll No",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="W")

        text_roll=Entry(Manage_Frame,textvariable= self.Roll_No_var,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        text_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="W")

        text_name=Entry(Manage_Frame,textvariable=self.name_var,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        text_name.grid(row=2,column=1,pady=10,padx=20,sticky="W")

        lbl_email=Label(Manage_Frame,text="Email_Id",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="W")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="W")

        lbl_gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("TImes New Roman",20,"bold"))
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="W")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("Times New Roman",13,"bold"),state="readonly")
        combo_gender['values']=('Male','Female',"Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20)


        lbl_contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("Tiems New Roman",20,"bold"))
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="W")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="W")

        lbl_dob=Label(Manage_Frame,text="DOB",bg="crimson",fg="white",font=("TImes New Roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="W")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("Times New Roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="W")

        lbl_add=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("Times New Roman",20,"bold"))
        lbl_add.grid(row=7,column=0,pady=10,padx=20,sticky="W")

        self.txt_add=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_add.grid(row=7,column=1,pady=10,padx=20,sticky="W")

       ########################## BUTTUON FRAME #########################

        Btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        Btn_Frame.place(x=15,y=520,width=580)

        addbtn=Button(Btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(Btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        delbtn=Button(Btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        clerbtn=Button(Btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)






############################ DETAIL_FRAME ######################################
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=580)


        lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("Times New Roman",18,"bold"))
        lbl_search.grid(row=0,column=0,padx=20,pady=10,sticky="W")

        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("Times New Roman",13,"bold"),state="readonly")
        combo_search["values"]=("Roll No","Name","Contact")
        combo_search.grid(row=0,column=1,pady=10,padx=10,sticky="W")

        txt_serch=Entry(Detail_Frame,width=20,font=("Times New Roman",10,"bold"),bd=5,relief=GROOVE)
        txt_serch.grid(row=0,column=2,pady=10,padx=20,sticky="W")

        Search_btn=Button(Detail_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=20,pady=10,sticky="w")
        showall_btn=Button(Detail_Frame,text="Show All",width=10,pady=5).grid(row=0,column=4,padx=20,pady=10,sticky="w")

###################### TABLE FRAME #################################################

        table_frame=Frame(Detail_Frame,bd=4,relief=GROOVE,bg="crimson")
        table_frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        Student_table=ttk.Treeview(table_frame,columns=("roll no","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("roll no",text="Roll No")
        Student_table.heading("name",text="Name")
        Student_table.heading("email",text="Email Id")
        Student_table.heading("gender",text="Gender")
        Student_table.heading("contact",text="Contact")
        Student_table.heading("dob",text="DOB")
        Student_table.heading("address",text="Address")
        Student_table['show']='headings'

        Student_table.column("roll no",width=100)
        Student_table.column("name",width=120)    
        Student_table.column("email",width=120)
        Student_table.column("gender",width=100)
        Student_table.column("contact",width=100)
        Student_table.column("dob",width=100)
        Student_table.column("address",width=150)


        Student_table.pack(fill=BOTH,expand=1)
    def add_students(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                           self.name_var.get(),
                                                                           self.email_var.get(),
                                                                           self.gender_var.get(),
                                                                           self.contact_var.get(),
                                                                           self.dob_var.get(),
                                                                           self.txt_add.get('1.0',END)
                                                                           ))
            con.commit()
            con.close()




root=Tk()
obj=Student(root)
root.mainloop()
