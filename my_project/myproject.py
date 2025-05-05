#ساحت ماشین حساب-question1,parta,solution first
#aynaz ansari
import tkinter
import math


class Program(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.geometry("400x400-50+50")
        self.title("calculater")
        self.iconbitmap("1.ico")
        self.resizable(False,False)

        
        self.display = tkinter.Entry(self, font=("Arial", 18), relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, sticky="we", padx=20, pady=20)

        

    
    def show(self, value):
        current = self.display.get()
        if value == "." and "." in current:
            return
        self.display.insert(tkinter.END, value)

    def clear(self):
        self.display.delete(0, tkinter.END)
    
    def calculate(self):
     expression = self.display.get()
     result = eval(expression)
     self.display.delete(0, tkinter.END)
     self.display.insert(0, result)

    def sqrt_function(self):
      value = self.display.get()
      if value:
        result = math.sqrt(float(value))
        self.display.delete(0, tkinter.END)
        self.display.insert(0, result)

    
    def create_widgets(self):
        self.btn_1 = tkinter.Button(self, text="1", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("1"))
        self.btn_2 = tkinter.Button(self, text="2", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("2"))
        self.btn_3 = tkinter.Button(self, text="3", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("3"))
        self.btn_4 = tkinter.Button(self, text="4", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("4"))
        self.btn_5 = tkinter.Button(self, text="5", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("5"))
        self.btn_6 = tkinter.Button(self, text="6", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("6"))
        self.btn_7 = tkinter.Button(self, text="7", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("7"))
        self.btn_8 = tkinter.Button(self, text="8", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("8"))
        self.btn_9 = tkinter.Button(self, text="9", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("9"))
        self.btn_0 = tkinter.Button(self, text="0", padx=72, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("0"))
        self.btn_clear = tkinter.Button(self, text="C", font=("arial", 10, "bold"), bd=1, padx=30, pady=15, bg="#3697f5", command=self.clear)
        self.btn_add = tkinter.Button(self, text="+", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("+"))
        self.btn_minus = tkinter.Button(self, text="-", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("-"))
        self.btn_divide = tkinter.Button(self, text="÷", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("/"))
        self.btn_multiply = tkinter.Button(self, text="×", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("*"))
        self.btn_dot = tkinter.Button(self, text=".", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("."))
        self.btn_power = tkinter.Button(self, text="^", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("^"))
        self.btn_factorial = tkinter.Button(self, text="!", width=10, fg="white", bg="#2a2d36", bd=1, command=lambda: self.show("!"))
        self.btn_sqrt = tkinter.Button(self, text="√", width=10, fg="white", bg="#2a2d36", bd=1, command=self.sqrt_function)
        self.btn_equal = tkinter.Button(self, text="=", width=10, pady=45, fg="black", bg="#fe9037", bd=1, command=self.calculate)
        
    def locate_widgets(self):
        self.btn_7.grid(row=1, column=0, padx=2, pady=2)
        self.btn_8.grid(row=1, column=1, padx=2, pady=2)
        self.btn_9.grid(row=1, column=2, padx=2, pady=2)
        self.btn_divide.grid(row=1, column=3, padx=2, pady=2)
        self.btn_4.grid(row=2, column=0, padx=2, pady=2)
        self.btn_6.grid(row=2, column=2, padx=2, pady=2)
        self.btn_5.grid(row=2, column=1, padx=2, pady=2)
        self.btn_multiply.grid(row=2, column=3, padx=2, pady=2)

        self.btn_1.grid(row=3, column=0, padx=2, pady=2)
        self.btn_2.grid(row=3, column=1, padx=2, pady=2)
        self.btn_3.grid(row=3, column=2, padx=2, pady=2)
        self.btn_minus.grid(row=3, column=3, padx=2, pady=2)

        self.btn_0.grid(row=4, column=0, padx=2, pady=2)
        self.btn_dot.grid(row=4, column=1, padx=2, pady=2)
        self.btn_equal.grid(row=4, column=2, padx=2, pady=2)
        self.btn_add.grid(row=4, column=3, padx=2, pady=2)
        self.btn_clear.grid(row=5, column=0, padx=2, pady=2)
        self.btn_power.grid(row=5, column=1, padx=2, pady=2)
        self.btn_sqrt.grid(row=5, column=2, padx=2, pady=2)
        self.btn_factorial.grid(row=5, column=3, padx=2, pady=2)

    




    def show_program(self):
        self.mainloop()


my_program=Program()
my_program.create_widgets()
my_program.locate_widgets()
my_program.show_program()
