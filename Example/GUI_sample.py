import tkinter

class Program(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.geometry("300x300-50+50")
        self.title("Test Program")
        self.iconbitmap("1.ico")
        self.resizable(False,False)

    def clear_form(self):
        self.textbox_first_name.delete(0,tkinter.END)
        self.textbox_last_name.delete(0,tkinter.END)
        self.textbox_age.delete(0,tkinter.END)
        self.textbox_height.delete(0,tkinter.END)
        self.textbox_weight.delete(0,tkinter.END)
        self.textbox_bmi.config(state="normal")
        self.textbox_bmi.delete(0,tkinter.END)
        self.textbox_bmi.config(state="disabled")
        self.btn_save.config(state="disabled")
        self.textbox_first_name.focus_set()

    def save_to_file(self):
        self.first_name=self.textbox_first_name.get()
        self.last_name=self.textbox_last_name.get()
        self.age=int(self.textbox_age.get())
        self.height=float(self.textbox_height.get())
        self.weight=int(self.textbox_weight.get())
        self.textbox_bmi.config(state="normal")
        self.bmi=float(self.textbox_bmi.get())
        self.textbox_bmi.config(state="disabled") 
        content=f"""First Name:{self.first_name}
Last Name:{self.last_name}  
Age:{self.age}      
Height:{self.height}       
Weight:{self.weight}
BMI:{self.bmi}\n\n"""

        with open("Persons.txt",mode="a") as file:
           file.write(content)

        self.clear_form()
    
    def bmi_calculate(self):
        if len(self.textbox_height.get())==0:
            print("Please Fill  Height Field")
        elif len(self.textbox_weight.get())==0:
            print("Please Fill weight Feild")
        else:
            self.bmi=int(self.textbox_weight.get())/(float(self.textbox_height.get())**2)
            self.bmi=round(self.bmi,2)
            self.textbox_bmi.config(state="normal")
            self.textbox_bmi.delete(0,tkinter.END)
            self.textbox_bmi.insert(0,self.bmi)
            self.textbox_bmi.config(state="disabled")
            self.btn_save.config(state="normal")
            

        
    def create_widgets(self):
        self.label_first_name=tkinter.Label(self,text="First Name",font=("Arial",10))
        self.label_last_name=tkinter.Label(self,text="Last Name",font=("Arial",10))
        self.label_age=tkinter.Label(self,text="Age",font=("Arial",10))
        self.label_height=tkinter.Label(self,text="Height",font=("Arial",10))
        self.label_weight=tkinter.Label(self,text="Weight",font=("Arial",10))
        self.label_bmi=tkinter.Label(self,text="BMI",font=("Arial",10))

        self.textbox_first_name=tkinter.Entry(self,width=25,border=1,relief="solid")
        self.textbox_last_name=tkinter.Entry(self,width=25,border=1,relief="solid")
        self.textbox_age=tkinter.Entry(self,width=25,border=1,relief="solid")
        self.textbox_height=tkinter.Entry(self,width=25,border=1,relief="solid")
        self.textbox_weight=tkinter.Entry(self,width=25,border=1,relief="solid")
        self.textbox_bmi=tkinter.Entry(self,width=25,border=1,relief="solid",state="disabled",disabledbackground="#bbb",disabledforeground="#333")

        self.btn_save=tkinter.Button(self,text="Save",padx=24,pady=4,border=1,relief="solid",bg="#ddd",fg="#222",activebackground="#000",activeforeground="#fff",state="disabled",command=self.save_to_file)
        self.btn_reset=tkinter.Button(self,text="Reset",padx=24,pady=4,border=1,relief="solid",bg="#ddd",fg="#222",activebackground="#000",activeforeground="#fff",command=self.save_to_file)
        self.btn_calculate=tkinter.Button(self,text="calculate",width=32,padx=20,border=1,relief="solid",bg="#ddd",fg="#222",activebackground="#000",activeforeground="#fff",command=self.bmi_calculate)

    def locate_widgets(self):
        self.label_first_name.grid(row=0,column=0,sticky="w",padx=(10,25),pady=5)
        self.label_last_name.grid(row=1,column=0,sticky="w",padx=(10,25),pady=5)
        self.label_age.grid(row=2,column=0,sticky="w",padx=(10,25),pady=5)
        self.label_height.grid(row=3,column=0,sticky="w",padx=(10,25),pady=5)
        self.label_weight.grid(row=4,column=0,sticky="w",padx=(10,25),pady=5)
        self.label_bmi.grid(row=5,column=0,sticky="w",padx=(10,25),pady=5)

        self.textbox_first_name.grid(row=0,column=1)
        self.textbox_last_name.grid(row=1,column=1)
        self.textbox_age.grid(row=2,column=1)
        self.textbox_height.grid(row=3,column=1)
        self.textbox_weight.grid(row=4,column=1)
        self.textbox_bmi.grid(row=5,column=1)

        self.btn_save.grid(row=6,column=0,pady=5,sticky="w",padx=(10,5))
        self.btn_reset.grid(row=6,column=1,pady=5,sticky="e")
        self.btn_calculate.grid(row=7,column=0,padx=(10,0),pady=5,sticky="w",columnspan=2)
       



    def show_program(self):
        self.mainloop()


my_program=Program()
my_program.create_widgets()
my_program.locate_widgets()
my_program.show_program()