from tkinter import *
from tkinter import messagebox
import math,random,os
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1250x1100+0+0")
        self.root.title("Billing Software")
        bg_color="black"
        title=Label(self.root,text="Billing Software",bd=12,relief=FLAT,bg=bg_color,fg="white",font=("times new roman",25,"bold"),pady=2).pack(fill=X)
    
        #=============Variables======================
        #=============Clothes======================
        self.jeans=IntVar()
        self.shirt=IntVar()
        self.skirt=IntVar()
        self.top=IntVar()
    
        #=============Grocery========================
        self.rice=IntVar()
        self.food_oil=IntVar() 
        self.daal=IntVar()
        self.wheat=IntVar()
        #=============Toys========================
        self.ball=IntVar()
        self.carrom=IntVar() 
        self.bat=IntVar()
        self.chess=IntVar()
        #=============Cold Drink========================
        self.slice=IntVar()
        self.coco_cola=IntVar() 
        self.sprite=IntVar()
        self.mango_juice=IntVar()
        
        #=============Total Product Price and Tax variables====================
        self.clothes_toys_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drink_price=StringVar()
	
        self.clothes_toys_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()
        #=============Customer Detail================
        self.c_name=StringVar()
        self.c_phon=StringVar()
        self.bill_no=StringVar()
        self.address=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()
        #=============Customer Detail================
        F1=LabelFrame(self.root,bd=10,relief=FLAT,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=70,relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",fg="white",bg=bg_color,font=("times new roman",12,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=11,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="Phone No.",fg="white",bg=bg_color,font=("times new roman",12,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=11,textvariable=self.c_phon,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        cadd_lbl=Label(F1,text="Address.",fg="white",bg=bg_color,font=("times new roman",12,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cadd_txt=Entry(F1,width=11,textvariable=self.address,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        
        cbill_lbl=Label(F1,text="Bill Number",fg="white",bg=bg_color,font=("times new roman",12,"bold")).grid(row=0,column=6,padx=20,pady=5)
        cbill_txt=Entry(F1,width=11,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=7,pady=5,padx=10)

        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=8,padx=50,pady=10)
        
        #=============Cold drink Frame================
        F2=LabelFrame(self.root,bd=10,relief=FLAT,text="Cold drink",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=0,y=175,width=325,height=240)
        bath_lbl=Label(F2,text="slice",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.slice,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        face_crm_lbl=Label(F2,text="coco cola",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_crm_txt=Entry(F2,width=10,textvariable=self.coco_cola,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        face_w_lbl=Label(F2,text="sprite",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.sprite,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        hair_s_lbl=Label(F2,text="mango juice",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.mango_juice,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
         #=============Clothes Frame================
        F3=LabelFrame(self.root,bd=10,relief=FLAT,text="Clothes",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=0,y=410,width=325,height=240)
        bath_lbl=Label(F3,text="Jeans",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F3,width=10,textvariable=self.jeans,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        face_crm_lbl=Label(F3,text="Shirt",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_crm_txt=Entry(F3,width=10,textvariable=self.shirt,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        face_w_lbl=Label(F3,text="Skirt",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F3,width=10,textvariable=self.skirt,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        hair_s_lbl=Label(F3,text="Top",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F3,width=10,textvariable=self.top,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)

        #=============Grocery Frame================
        F4=LabelFrame(self.root,bd=10,relief=FLAT,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=320,y=175,width=285,height=240)
        g1_lbl=Label(F4,text="Rice",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F4,width=10,textvariable=self.rice,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        g2_lbl=Label(F4,text="Food Oil",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F4,width=10,textvariable=self.food_oil,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        g3_lbl=Label(F4,text="Daal",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F4,width=10,textvariable=self.daal,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        g4_lbl=Label(F4,text="Wheat",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F4,width=10,textvariable=self.wheat,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        #=============Toys Frame================
        F5=LabelFrame(self.root,bd=10,relief=FLAT,text="Toys",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F5.place(x=320,y=410,width=285,height=240)
        g1_lbl=Label(F5,text="Ball",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F5,width=10,textvariable=self.ball,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        g2_lbl=Label(F5,text="Carrom",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F5,width=10,textvariable=self.carrom,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        g3_lbl=Label(F5,text="Bat",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F5,width=10,textvariable=self.bat,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        g4_lbl=Label(F5,text="Chess",font=("times new roman",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F5,width=10,textvariable=self.chess,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)

        #=============Bill Area Frame================
        F6=Frame(self.root,bd=10,relief=FLAT)
        F6.place(x=800,y=175,width=640,height=500)
        bill_title=Label(F6,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F6,orient=VERTICAL)
        self.textarea=Text(F6,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=============Button Frame================
        F7=LabelFrame(self.root,bd=10,relief=FLAT,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F7.place(x=3,y=660,relwidth=1,height=140)
        m1_lbl=Label(F7,text="Total Clothes\Toys Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F7,width=15,textvariable=self.clothes_toys_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F7,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F7,width=15,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F7,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F7,width=15,textvariable=self.cold_drink_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F7,text="GST on Clothes\Toys",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=3,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F7,width=15,textvariable=self.clothes_toys_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=1)

        c2_lbl=Label(F7,text="GST on Grocery ",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=3,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F7,width=15,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=1)

        c3_lbl=Label(F7,text="GST on Cold Drink",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=3,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F7,width=15,textvariable=self.cold_drink_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=1)
        btn_f=Frame(F7,bd=7,relief=RAISED)
        btn_f.place(x=920,width=510,height=180)
        total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    def total(self):
        self.c_s_p=self.slice.get()*40
        self.c_fc_p=self.coco_cola.get()*120
        self.c_fw_p=self.sprite.get()*80
        self.c_spr_p=self.mango_juice.get()*110
        self.total_cold_drink_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_spr_p
                                  )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.c_tax=round(self.total_cold_drink_price*0.28,2)
        self.cold_drink_tax.set("Rs. "+str(self.c_tax))
        self.g_r_p=self.jeans.get()*800
        self.g_fo_p=self.shirt.get()*800
        self.g_w_p=self.skirt.get()*60
        self.g_d_p=self.top.get()*240
        self.dp_m_p=self.ball.get()*60
        self.dp_c_p=self.carrom.get()*600
        self.dp_f_p=self.bat.get()*500
        self.dp_th_p=self.chess.get()*245
        self.total_clothes_toys_price=float(
                                    self.g_r_p+
                                    self.g_fo_p+
                                    self.g_w_p+
                                    self.g_d_p+
                                    self.dp_m_p+
                                    self.dp_c_p+
                                    self.dp_f_p+
                                    self.dp_th_p
                                  )
        self.clothes_toys_price.set("Rs. "+str(self.total_clothes_toys_price))
        self.g_tax=round(self.total_clothes_toys_price*0.28,2)
        self.clothes_toys_tax.set("Rs. "+str(self.g_tax))
        self.cd_m_p=self.rice.get()*60
        self.cd_c_p=self.food_oil.get()*60
        self.cd_f_p=self.daal.get()*50
        self.cd_th_p=self.wheat.get()*45
        self.total_grocery_price=float(
                                    self.cd_m_p+
                                    self.cd_c_p+
                                    self.cd_f_p+
                                    self.cd_th_p
                                   )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.cd_tax=round(self.total_grocery_price*0.18,2)
        self.grocery_tax.set("Rs. "+str(self.cd_tax))
        self.total_bill=float(
            self.total_cold_drink_price+
            self.total_clothes_toys_price+
            self.total_grocery_price+
            self.c_tax+
            self.g_tax+
            self.cd_tax
        )
        self.total_bill_withoutGST=float(
            self.total_clothes_toys_price+
            self.total_grocery_price+
            self.total_cold_drink_price
        )
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome lPU Retail")
        self.textarea.insert(END,f"\n Bill Number :{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name :{self.c_name.get()}")
        self.textarea.insert(END,f"\n Customer Address :{self.address.get()}")
        self.textarea.insert(END,f"\n Phone Number :{self.c_phon.get()}")
        
        self.textarea.insert(END,f"\n======================================")
        self.textarea.insert(END,f"\n Product\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n======================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phon.get()=="":
            messagebox.showerror("Error","Customer Details are Required")
        elif self.clothes_toys_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drink_price.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Product Selected")
        else:
            self.welcome_bill()
            #===Grocery=====
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice   \t\t{self.rice.get()}\t\t{self.cd_m_p}")
            if self.food_oil.get()!=0:
                self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.cd_c_p}")
            if self.daal.get()!=0:
                self.textarea.insert(END,f"\n Daal   \t\t{self.daal.get()}\t\t{self.cd_f_p}")
            if self.wheat.get()!=0:
                self.textarea.insert(END,f"\n Wheat  \t\t{self.wheat.get()}\t\t{self.cd_th_p}")
            #===clothes=====
            if self.jeans.get()!=0:
                self.textarea.insert(END,f"\n Jeans   \t\t{self.jeans.get()}\t\t{self.g_r_p}")
            if self.shirt.get()!=0:
                self.textarea.insert(END,f"\n Shirt \t\t{self.shirt.get()}\t\t{self.g_fo_p}")
            if self.skirt.get()!=0:
                self.textarea.insert(END,f"\n Skirt   \t\t{self.skirt.get()}\t\t{self.g_w_p}")
            if self.top.get()!=0:
                self.textarea.insert(END,f"\n Top  \t\t{self.top.get()}\t\t{self.g_d_p}")

            #===Toys=====
            if self.ball.get()!=0:
                self.textarea.insert(END,f"\n Ball  \t\t{self.ball.get()}\t\t{self.dp_m_p}")
            if self.carrom.get()!=0:
                self.textarea.insert(END,f"\n Carrom \t\t{self.carrom.get()}\t\t{self.dp_c_p}")
            if self.bat.get()!=0:
                self.textarea.insert(END,f"\n Bat   \t\t{self.bat.get()}\t\t{self.dp_f_p}")
            if self.chess.get()!=0:
                self.textarea.insert(END,f"\n Chess  \t\t{self.chess.get()}\t\t{self.dp_th_p}")
            #===Cold Drink=====
            if self.slice.get()!=0:
                self.textarea.insert(END,f"\n Slice   \t\t{self.slice.get()}\t\t{self.c_s_p}")
            if self.coco_cola.get()!=0:
                self.textarea.insert(END,f"\n Coco cola   \t\t{self.coco_cola.get()}\t\t{self.c_fc_p}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite  \t\t{self.sprite.get()}\t\t{self.c_fw_p}")
            if self.mango_juice.get()!=0:
                self.textarea.insert(END,f"\n Mango Juice  \t\t{self.mango_juice.get()}\t\t{self.c_spr_p}")
            self.textarea.insert(END,f"\n--------------------------------------")
            if self.clothes_toys_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Clothes\Toys Tax \t\t\t{self.clothes_toys_tax.get()}")
            
            if self.grocery_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n Grocery Tax \t\t\t{self.grocery_tax.get()}")
                
            if self.cold_drink_tax.get()!="Rs. 0.0":
                self.textarea.insert(END,f"\n ColdDrink Tax\t\t\t{self.cold_drink_tax.get()}")
            self.textarea.insert(END,f"\n Total Bill without GST  \t\t\t Rs. {self.total_bill_withoutGST}")
            self.textarea.insert(END,f"\n Total Bill  \t\t\t Rs. {self.total_bill}")
            self.textarea.insert(END,f"\n------------------------------------")
        self.save_bill()
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("D:\\project\\bill_app\\invoice\\"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved successfullt")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("D:\\project\\bill_app\\invoice\\"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"D:\\project\\bill_app\\invoice\\{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")
    def clear_data(self):
        op=messagebox.askyesno("clear","Do you want to Reset Entries?")
        if op>0:
            #=============Grocery========================
            self.rice.set(0)
            self.food_oil.set(0) 
            self.daal.set(0)
            self.wheat.set(0)
            #=============Clothes========================
            self.jeans.set(0)
            self.shirt.set(0) 
            self.skirt.set(0)
            self.top.set(0)
            #=============Cold Drinka====================
            self.slice.set(0)
            self.coco_cola.set(0)
            self.sprite.set(0)
            self.mango_juice.set(0)
            #=============Toys========================
            self.ball.set(0)
            self.carrom.set(0) 
            self.bat.set(0)
            self.chess.set(0)
            #=============Total Product Price and Tax variables====================
            self.clothes_toys_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.clothes_toys_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #=============Customer Detail================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            self.address.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()





root=Tk()
obj=Bill_App(root)

root.mainloop()
