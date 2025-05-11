#ساخت فرم -question1,parta,first-solution
import tkinter
from tkinter import ttk


class Program(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.geometry("350x500-50+50")
        self.title("Test Program")
        self.resizable(False,False)

        self.gender=tkinter.IntVar()
        self.matrial_status=tkinter.IntVar()

    def clear_form(self):
        self.textbox_first_name.delete(0,tkinter.END)
        self.textbox_last_name.delete(0,tkinter.END)
        self.textbox_year_of_birth.delete(0,tkinter.END)
        self.textbox_gross_salary.delete(0,tkinter.END)
        self.textbox_tax.delete(0,tkinter.END)
        self.textbox_insurance.delete(0,tkinter.END)
        self.textbox_net_salary.config(state="normal")
        self.textbox_num_of_children.delete(0,tkinter.END)
        self.textbox_net_salary.config(state="disabled")
        self.btn_save.config(state="disabled")
        self.textbox_first_name.focus_set()
        self.gender.set(0)
        self.matrial_status.set(0)

    def fields(self):
        first_name=self.textbox_first_name.get()
        last_name=self.textbox_last_name.get()
        year=self.textbox_year_of_birth.get()
        salary=self.textbox_gross_salary.get()
        tax=self.textbox_tax.get()
        insurance=self.textbox_insurance.get()
        net_salary=self.textbox_net_salary.get()
        children=self.textbox_num_of_children.get()
        gender=self.gender.get()
        status=self.matrial_status.get()

        if self.matrial_status.get()==1:
            children=0
        else:
            children=int(self.textbox_num_of_children.get())


        if not first_name.isalpha():
            print("First name must contain only letters.")
            return
        if not last_name.isalpha():
            print("Last name must contain only letters.")
            return
        if not year.isdigit() or len(year)!=4 or int(year)<=0:
            print("Year of Birth must be a valid integer.")
            return
        if not salary.isdigit() or int(salary)<=0:
            print("Gross Salary must be a valid integer.")
            return
        if not tax.isdigit() or  int(tax)<0:
            print("Tax% must be a valid integer.")
            return
        if not insurance.isdigit() or  int(insurance)<0:
            print("Insurance% must be a valid integer.")
            return
        if status == 1:  
            children = 0
        else:
            children_str = self.textbox_num_of_children.get()
            if not children_str.isdigit() or int(children_str) < 0:
                print("Number of Children must be a non-negative integer.")
                return
            children = int(children_str)
        
        self.save_to_file(first_name,last_name,year,salary,tax,insurance,net_salary,children,gender,status)
    
    def save_to_file(self,first_name,last_name,year,salary,tax,insurance,net_salary,children,gender,status):
        gender_text={1:"male",2:"female",3:"other"}.get(gender,"Unknown")
        status_text={1:"single",2:"married"}.get(status,"Unknown")
        with open("form_data.txt",mode="a") as file:
            file.write(f"First Name:{first_name}\n")
            file.write(f"Last Name:{last_name}\n")
            file.write(f"Gender:{gender_text}\n")
            file.write(f"Year of Birth:{year}\n")
            file.write(f"Gross Salary:{salary}\n")
            file.write(f"Tax:{tax}\n")
            file.write(f"Insurance:{insurance}\n")
            file.write(f"Net Salary:{net_salary}\n")
            file.write(f"Matrial status:{status_text}\n")
            file.write(f"Number of  children :{children}\n")
            self.clear_form()
    


    def calculate(self):
        gross = self.textbox_gross_salary.get()
        tax = self.textbox_tax.get()
        insurance = self.textbox_insurance.get()

        if gross.isdigit() and tax.isdigit() and insurance.isdigit():
           gross = float(gross)
           tax = float(tax)
           insurance = float(insurance)

        if gross <= 0:
            print("Error: Gross salary must be a positive number.")
            return
        if tax < 0 or tax > 100:
            print("Error: Tax must be between 0 and 100.")
            return
        if insurance < 0 or insurance > 100:
            print("Error: Insurance must be between 0 and 100.")
            return
        if tax + insurance > 100:
            print("Error: The total of tax and insurance must not exceed 100%.")
            return

        total_deduction = (tax + insurance) / 100
        net_salary = gross * (1 - total_deduction)

        self.textbox_net_salary.config(state="normal")
        self.textbox_net_salary.delete(0, tkinter.END)
        self.textbox_net_salary.insert(0, str(round(net_salary, 2)))
        self.textbox_net_salary.config(state="disabled")

        self.btn_save.config(state="normal")
    


      

    def number_children(self):
        if self.matrial_status.get() == 2:  
           self.textbox_num_of_children.config(state='normal')
        else:
           self.textbox_num_of_children.delete(0, tkinter.END)
           self.textbox_num_of_children.config(state='disabled')

    
    def matrial_status_change(self):
        self.show_matrialstatus()
        self.number_children()

    def show_matrialstatus(self):
        print(self.matrial_status.get())



    def show_gender(self):
        print(self.gender.get())


    def create_widgets(self):
        self.label_first_name=tkinter.Label(self,text="First Name",fg="black")
        self.label_last_name=tkinter.Label(self,text="Last Name",fg="black" )
        self.label_gender=tkinter.Label(self,text="Gender",fg="black" )
        self.label_year_of_birth=tkinter.Label(self,text="Year of Birth",fg="black" )
        self.label_gross_salary=tkinter.Label(self,text="Gross Salary",fg="black" )
        self.label_tax=tkinter.Label(self,text="Tax(%)",fg="black" )
        self.label_insurance=tkinter.Label(self,text="Insurance(%)",fg="black" )
        self.label_net_salary=tkinter.Label(self,text="Net Salary",fg="black",state="disabled")
        self.label_matrial_status=tkinter.Label(self,text="Matrial Status",fg="black" )
        self.label_num_of_children=tkinter.Label(self,text="Num of Children",fg="black" )

        self.btn_save=tkinter.Button(self,text="Save",padx=24,pady=4,border=1,relief="solid",bg="#ddd",fg="#222",activebackground="#000",activeforeground="#fff",command=self.fields)
        self.btn_clear=tkinter.Button(self,text="Clear",padx=24,pady=4,border=1,relief="solid",bg="#ddd",fg="#222",activebackground="#000",activeforeground="#fff",command=self.clear_form)
        self.btn_calculate=tkinter.Button(self,text="Calculate",width=42,pady=4,border=1,relief="solid",bg="#ddd",fg="#222",activebackground="#000",activeforeground="#fff",command=self.calculate)


        self.textbox_first_name=tkinter.Entry(self,width=35,border=1,relief="solid")
        self.textbox_last_name=tkinter.Entry(self,width=35,border=1,relief="solid")
        self.textbox_year_of_birth=tkinter.Entry(self,width=35,border=1,relief="solid")
        self.textbox_gross_salary=tkinter.Entry(self,width=35,border=1,relief="solid")
        self.textbox_tax=tkinter.Entry(self,width=35,border=1,relief="solid")
        self.textbox_insurance=tkinter.Entry(self,width=35,border=1,relief="solid")
        self.textbox_net_salary=tkinter.Entry(self,width=35,border=1,relief="solid",state="disabled")
        self.textbox_num_of_children=tkinter.Entry(self,width=35,border=1,relief="solid")
        self.textbox_num_of_children.config(state="disabled")

        self.gender=tkinter.IntVar()

        self.radio_male=ttk.Radiobutton(self,text="Male",variable=self.gender,value=1,command=self.show_gender)
        self.radio_female=ttk.Radiobutton(self,text="Female",variable=self.gender,value=2,command=self.show_gender)
        self.radio_other=ttk.Radiobutton(self,text="other",variable=self.gender,value=3,command=self.show_gender)

        self.matrial_status=tkinter.IntVar()
        self.radio_single=ttk.Radiobutton(self,text="single",variable=self.matrial_status,value=1,command=self.matrial_status_change)
        self.radio_married=ttk.Radiobutton(self,text="married",variable=self.matrial_status,value=2,command=self.matrial_status_change)



    def locate_widgets(self):
        self.label_first_name.grid(row=0,column=0,sticky="w",pady=(5,0))
        self.label_last_name.grid(row=1,column=0,sticky="w",pady=(5,0))
        self.label_gender.grid(row=2,column=0,sticky="w",pady=(5,0))
        self.label_year_of_birth.grid(row=3,column=0,sticky="w",pady=(5,0))
        self.label_gross_salary.grid(row=4,column=0,sticky="w",pady=(5,0))
        self.label_tax.grid(row=5,column=0,sticky="w",pady=(5,0))
        self.label_insurance.grid(row=6,column=0,sticky="w",pady=(5,0))
        self.label_net_salary.grid(row=7,column=0,sticky="w",pady=(5,0))
        self.label_matrial_status.grid(row=8,column=0,sticky="w",pady=(5,0))
        self.label_num_of_children.grid(row=9,column=0,sticky="w",pady=(5,0))
        
      
        self.btn_save.grid(row=10,column=0,pady=5,sticky="w",padx=(10,0))
        self.btn_clear.grid(row=10,column=1,pady=5,sticky="e")
        self.btn_calculate.grid(row=11,column=0,padx=(10,0),pady=5,sticky="w",columnspan=2)

        self.textbox_first_name.grid(row=0,column=1,pady=10)
        self.textbox_last_name.grid(row=1,column=1,pady=10)
        self.textbox_year_of_birth.grid(row=3,column=1,pady=10)
        self.textbox_gross_salary.grid(row=4,column=1,pady=10)
        self.textbox_tax.grid(row=5,column=1,pady=10)
        self.textbox_insurance.grid(row=6,column=1,pady=10)
        self.textbox_net_salary.grid(row=7,column=1,pady=10)
        self.textbox_num_of_children.grid(row=9,column=1,pady=10)

        self.radio_male.grid(row=2,column=1,sticky="w")
        self.radio_female.grid(row=2,column=1,sticky="w",padx=(50,0))
        self.radio_other.grid(row=2,column=1,sticky="w",padx=(110,0))

        self.radio_single.grid(row=8,column=1,sticky="w")
        self.radio_married.grid(row=8,column=1,sticky="w",padx=(70,0))


    def show_program(self):
        self.mainloop()


my_program=Program()
my_program.create_widgets()
my_program.locate_widgets()
my_program.show_program()