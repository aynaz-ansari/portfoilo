import tkinter
from tkinter import ttk
from tkinter import messagebox
import database

class Product(tkinter.Tk):

    def define_brand(self,x):
        brands={
            "Mobile":["Apple","Google","Honor","Huawei","Samsung","Xiaomi"],
            "Laptop":["Acer","Apple","Asus","Dell","HP","Lenovo","MSI"],
            "Keyboard":["Corsair","Logitec","Razer","Redragon","T-Dagger"],
            "Tablet":["Apple","Asus","Huawei","Lenovo","Microsoft","Samsung","Xiaomi"],
            "Mouse":["Apple","Asus","Huawei","Logitec","Razer","Redragon","T-Dagger"],
            "Monitor":["Apple","Asus","HP","LG","MSI","Samsung"]
        }
        self.dropdown_brand.config(state="normal")
        self.dropdown_brand.config(values=brands[self.variable_category.get()])
        self.dropdown_brand.current(0)

    def define_total_price(self):
        self.textbox_total_price.config(state="normal")
        waranty=self.variable_waranty.get()
        if waranty==0:
            self.textbox_total_price.delete(0,tkinter.END)
            self.textbox_total_price.insert(0,self.textbox_price.get())
        else:
            self.textbox_total_price.delete(0,tkinter.END)
            self.textbox_total_price.insert(0,round(int(self.textbox_price.get())*1.15))

        self.textbox_total_price.config(state="disabled")

    def clear(self):
        self.variable_category.set("")
        self.variable_brand.set("")
        self.dropdown_brand.config(state="disabled")
        self.textbox_model.delete(0,tkinter.END)
        self.textbox_color.delete(0,tkinter.END)
        self.textbox_price.delete(0,tkinter.END)
        self.variable_waranty.set(-1)
        self.textbox_total_price.config(state="normal")
        self.textbox_total_price.delete(0,tkinter.END)
        self.textbox_total_price.config(state="disabled")
        self.dropdown_category.focus_set()

    def save(self):
        category=self.variable_category.get()
        brand=self.variable_brand.get()
        model=self.textbox_model.get()
        color=self.textbox_color.get()
        price=self.textbox_price.get()
        waranty=self.variable_waranty.get()
        self.textbox_total_price.config(state="normal")
        total_price=self.textbox_total_price.get()
        self.textbox_total_price.config(state="disabled")

        if category=="":
            messagebox.showerror("Error","Please Select Category!")
        elif brand=="":
            messagebox.showerror("Error","Please Select Brand!")
        elif model=="":
            messagebox.showerror("Error","Please Enter a Valid Model!")
        elif color=="":
            messagebox.showerror("Error","Please Enter a Valid Color!")
        elif price.isnumeric()==False or int(price)<0:
            messagebox.showerror("Error","Please Enter a Valid Price!")
        elif waranty==-1:
            messagebox.showerror("Error","Please Select Waranty Status!")
        else:
            price=int(price)
            total_price=int(total_price)
            self.database.add_product(category,brand,model,color,price,waranty,total_price)
            messagebox.showinfo("Successful","Your Information Saved to Database Successfully!")
            self.clear()

    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Product Information")
        self.geometry("260x300-50+50")
        self.resizable(False,False)
        self.database=database.Database()

    def create_widgets(self):
        self.label_category=tkinter.Label(self,text="Category")
        self.label_brand=tkinter.Label(self,text="Brand")
        self.label_model=tkinter.Label(self,text="Model")
        self.label_color=tkinter.Label(self,text="Color")
        self.label_price=tkinter.Label(self,text="Price")
        self.label_waranty=tkinter.Label(self,text="Waranty")
        self.label_total_price=tkinter.Label(self,text="Total Price")

        self.variable_category=tkinter.StringVar()
        self.category_values=["Mobile","Laptop","Keyboard","Tablet","Mouse","Monitor"]
        self.category_values.sort()
        self.dropdown_category=ttk.Combobox(self,textvariable=self.variable_category,values=self.category_values,width=25)
        self.dropdown_category.bind("<<ComboboxSelected>>",self.define_brand)

        self.variable_brand=tkinter.StringVar()
        self.dropdown_brand=ttk.Combobox(self,textvariable=self.variable_brand,state="disabled",width=25)

        self.textbox_model=tkinter.Entry(self,width=28,border=1,relief="solid")
        self.textbox_color=tkinter.Entry(self,width=28,border=1,relief="solid")
        self.textbox_price=tkinter.Entry(self,width=28,border=1,relief="solid")

        self.variable_waranty=tkinter.IntVar()
        self.variable_waranty.set(-1)
        self.radio_waranty_1=ttk.Radiobutton(self,text="No",variable=self.variable_waranty,value=0,command=self.define_total_price)
        self.radio_waranty_2=ttk.Radiobutton(self,text="Yes",variable=self.variable_waranty,value=1,command=self.define_total_price)

        self.textbox_total_price=tkinter.Entry(self,width=28,border=1,relief="solid",state="disabled",disabledbackground="#bbb",disabledforeground="#444")


        self.btn_clear=tkinter.Button(self,text="Clear",width=33,border=1,relief="solid",bg="#ddd",fg="#000",activebackground="#000",activeforeground="#fff",command=self.clear)
        self.btn_save=tkinter.Button(self,text="Save",width=33,border=1,relief="solid",bg="#ddd",fg="#000",activebackground="#000",activeforeground="#fff",command=self.save)

    def locate_widgets(self):
        self.label_category.grid(row=0,column=0,sticky="w",pady=(10,0),padx=5)
        self.label_brand.grid(row=1,column=0,sticky="w",pady=(10,0),padx=5)
        self.label_model.grid(row=2,column=0,sticky="w",pady=(10,0),padx=5)
        self.label_color.grid(row=3,column=0,sticky="w",pady=(10,0),padx=5)
        self.label_price.grid(row=4,column=0,sticky="w",pady=(10,0),padx=5)
        self.label_waranty.grid(row=5,column=0,sticky="w",pady=(10,0),padx=5)
        self.label_total_price.grid(row=6,column=0,sticky="w",pady=(10,0),padx=5)

        self.dropdown_category.grid(row=0,column=1,columnspan=2,pady=(10,0))
        self.dropdown_brand.grid(row=1,column=1,columnspan=2,pady=(10,0))

        self.textbox_model.grid(row=2,column=1,columnspan=2,pady=(10,0))
        self.textbox_color.grid(row=3,column=1,columnspan=2,pady=(10,0))
        self.textbox_price.grid(row=4,column=1,columnspan=2,pady=(10,0))

        self.radio_waranty_1.grid(row=5,column=1,sticky="w",pady=(10,0))
        self.radio_waranty_2.grid(row=5,column=2,sticky="e",pady=(10,0))

        self.textbox_total_price.grid(row=6,column=1,columnspan=2,pady=(10,0))

        self.btn_clear.grid(row=7,column=0,columnspan=3,padx=(5,0),pady=(10,0),sticky="w")
        self.btn_save.grid(row=8,column=0,columnspan=3,padx=(5,0),pady=(10,0),sticky="w")

    def show_program(self):
        self.mainloop()


my_program=Product()
my_program.create_widgets()
my_program.locate_widgets()
my_program.show_program()