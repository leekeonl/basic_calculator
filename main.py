#import tkinter
# -*- coding: utf-8 -*-
from tkinter import *
import math


root = Tk()

class Calculator:
    def click_button(self,numbers):
        global operator
        global var
        self.operator = self.operator + str(numbers)
        self.var.set(self.operator)

    def clear(self):
        self.entry.delete(0,END)
        self.operator =""

    def delete(self):
#        if not self.entry.empty:
        self.operator = str(self.entry.delete(len(self.entry.get())-1))    

    def evaluate(self):
        self.answer =eval(self.entry.get())
        self.var.set(self.answer)
        self.operator = str(self.answer)
        
    def sign(self):
        self.answer =eval(self.entry.get())
        self.var.set(-(float(self.answer)))
        self.operater = str(self.answer)

    def sin(self):
        self.answer =eval(self.entry.get())
        self.var.set(math.sin(self.answer))
        self.operater = str(self.answer)
        
    def cos(self):
        self.answer =eval(self.entry.get())
        self.var.set(math.cos(self.answer))
        self.operater = str(self.answer)
        
    def tan(self):
        self.answer =eval(self.entry.get())
        self.var.set(math.tan(self.answer))
        self.operater = str(self.answer) 
    
    def fact(self):
        self.answer =eval(self.entry.get())
        self.var.set(math.factorial(int(self.answer)))
        self.operater = str(self.answer)
        
    def sqrt(self):
        self.answer =eval(self.entry.get())
        self.var.set(math.sqrt(self.answer))
        self.operater = str(self.answer)
        
    def log(self):
        self.answer =eval(self.entry.get())
        self.var.set(math.log(self.answer))
        self.operater = str(self.answer)
        
    def square(self):
        self.answer =eval(self.entry.get())
        self.var.set(math.pow(self.answer, 2))
        self.operater = str(self.answer)
    
    def inverse(self):
        self.answer =eval(self.entry.get())
        self.var.set(float(1/float(self.answer)))
        self.operater = str(self.answer)
        
    def __init__(self,master):

        #Entry field and answer field that can views the answer
        
        self.operator = ""
        self.var = StringVar()
        frame_s = Frame(master, height=600, width=45 )
        frame_s.pack(side=TOP, fill=BOTH, expand=True)
        self.entry = Entry(frame_s,textvariable=self.var,bg='white',width=45,bd=20,insertwidth=4,justify='right',font=('arial',15,'bold'))
        self.entry.pack()
        self.t = Text(self.entry,height=40)

        label_key = Label(root, height=15, width=30,bd=10,bg='gray50')
        label_key.pack(side=LEFT, fill=BOTH, expand=True)

        label_fkey = Label(root, height=15, width=300, bg='gray25')
        label_fkey.pack(fill=BOTH, expand=True)

        #Make buttons from 0 - 9
        #first row, label key
        label_7 = Label(label_key, bg='black')
        label_7.grid(row=0, column=0)
        button_7 = Button(label_7, text='7', font=('Helvetica', '16'),command= lambda : self.click_button(7),bg='black',fg='cyan')
        button_7.pack()

        label_8 = Label(label_key, bg='black')
        label_8.grid(row=0, column=1, padx=20)
        button_8 = Button(label_8, text='8', font=('Helvetica', '16'),command= lambda: self.click_button(8),bg='black',fg='cyan')
        button_8.pack()

        label_9 = Label(label_key, bg='black')
        label_9.grid(row=0, column=2, padx=10)
        button_9 = Button(label_9, text='9', font=('Helvetica', '16'),command= lambda: self.click_button(9),bg='black',fg='cyan')
        button_9.pack()

        #second row, label key
        label_4 = Label(label_key, bg='black')
        label_4.grid(row=1, column=0, padx=10, pady=10)
        button_4 = Button(label_4, text='4', font=('Helvetica', '16'),command= lambda: self.click_button(4),bg='black',fg='cyan')
        button_4.pack()

        label_5 = Label(label_key, bg='black')
        label_5.grid(row=1, column=1, padx=10, pady=10)
        button_5 = Button(label_5, text='5', font=('Helvetica', '16'),command= lambda: self.click_button(5),bg='black',fg='cyan')
        button_5.pack()

        label_6 = Label(label_key, bg='black')
        label_6.grid(row=1, column=2, padx=10, pady=10)
        button_6 = Button(label_6, text='6', font=('Helvetica', '16'),command= lambda: self.click_button(6),bg='black',fg='cyan')
        button_6.pack()

        #third row, label key
        label_1 = Label(label_key, bg='black')
        label_1.grid(row=2, column=0, padx=10)
        button_1 = Button(label_1, text='1', font=('Helvetica', '16'),command= lambda: self.click_button(1),bg='black',fg='cyan')
        button_1.pack()

        label_2 = Label(label_key, bg='black')
        label_2.grid(row=2, column=1, padx=10)
        button_2 = Button(label_2, text='2', font=('Helvetica', '16'),command= lambda: self.click_button(2),bg='black',fg='cyan')
        button_2.pack()

        label_3 = Label(label_key, bg='black')
        label_3.grid(row=2, column=2, padx=10)
        button_3 = Button(label_3, text='3', font=('Helvetica', '16'),command= lambda: self.click_button(3),bg='black',fg='cyan')
        button_3.pack()

        
        #fourth row, label key
        label_0 = Label(label_key, bg='black')
        label_0.grid(row=3, column=0, padx=10, pady=10)
        button_0 = Button(label_0, text='0', font=('Helvetica', '16'),command= lambda: self.click_button(0),bg='black',fg='cyan')
        button_0.pack()
        
        label_lbrace = Label(label_key, bg='black')
        label_lbrace.grid(row=3, column=1, padx=10)
        button_lbrace = Button(label_lbrace, text='(', font=('Helvetica', '16'),command= lambda: self.click_button('('),bg='black',fg='cyan')
        button_lbrace.pack()

        label_rbrace = Label(label_key, bg='black')
        label_rbrace.grid(row=3, column=2, padx=10)
        button_rbrace = Button(label_rbrace, text=')', font=('Helvetica', '16'),command= lambda: self.click_button(')'),bg='black',fg='cyan')
        button_rbrace.pack()



        #fifth row, label key
        label_pi = Label(label_key, bg='black')
        label_pi.grid(row=4, column=0, padx=10, pady=10)
        button_pi = Button(label_pi, text='𝝿', font=('Helvetica', '16'),command= lambda: self.click_button(math.pi),bg='black',fg='cyan')
        button_pi.pack()
        
        label_deci = Label(label_key, bg='black')
        label_deci.grid(row=4, column=1, padx=10, pady=10)
        button_deci = Button(label_deci, text='.', font=('Helvetica', '16'),command= lambda: self.click_button('.'),bg='black',fg='cyan')
        button_deci.pack()
        
        label_equal = Label(label_key, bg='black')
        label_equal.grid(row=4, column=2, padx=10, pady=10)
        button_equal = Button(label_equal, text='=', font=('Helvetica', '16'),command= self.evaluate,bg='black',fg='cyan')
        button_equal.pack()
        
        #Make calculation sign such as division

   
        
        # first row, function key
        label_C = Label(label_fkey, bg='black')
        label_C.grid(row=0, column=0,sticky=W)
        button_C = Button(label_C, text='C', font=('Helvetica', '16'), height=1, width=3,command=  self.clear,bg='black',fg='cyan')
        button_C.pack(side=LEFT)

        label_del = Label(label_fkey, bg ='black')
        label_del.grid(row=0,column=1,sticky=E)
        button_del = Button(label_del, text='del', font=('Helvetica', '16'),bd=3, height=1, width=3,command=  self.delete)
        button_del.pack()
        
        label_sign = Label(label_fkey, bg ='black')
        label_sign.grid(row=0,column=2,sticky=E)
        button_sign = Button(label_sign, text='+/-', font=('Helvetica', '16'),bd=3, height=1, width=3,command= self.sign)
        button_sign.pack()
        
        
        # second row, function key

        label_sub = Label(label_fkey, bg='black')
        label_sub.grid(row=1, column=0, sticky=W, pady=10)
        button_sub = Button(label_sub, text='-', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('-'),bg='black',fg='cyan')
        button_sub.pack(side=LEFT)

        label_mul = Label(label_fkey, bg='black')
        label_mul.grid(row=1, column=1, sticky=E)
        button_mul = Button(label_mul, text='x', font=('Helvetica', '16'), bd=3, height=1, width=3,command= lambda: self.click_button('*'),bg='black',fg='cyan')
        button_mul.pack()
        
        label_sin = Label(label_fkey, bg ='black')
        label_sin.grid(row=1,column=2,sticky=W)
        button_sin = Button(label_sin, text='sin', font=('Helvetica', '16'),bd=3, height=1, width=3,command= self.sin)
        button_sin.pack()

        # Third row, function key     

        label_div = Label(label_fkey, bg='black')
        label_div.grid(row=2, column=0, sticky=W)
        button_div = Button(label_div, text='/', font=('Helvetica', '16'), height=1, width=3,command= lambda: self.click_button('/'),bg='black',fg='cyan')
        button_div.pack()

        label_add = Label(label_fkey, bg='black')
        label_add.grid(row=2, column=1, sticky=E)
        button_add = Button(label_add, text='+', font=('Helvetica', '16'),bd=3, height=1, width=3,command= lambda: self.click_button('+'),bg='black',fg='cyan')
        button_add.pack()
        
        label_cos = Label(label_fkey, bg ='black')
        label_cos.grid(row=2,column=2,sticky=E)
        button_cos = Button(label_cos, text='cos', font=('Helvetica', '16'),bd=3, height=1, width=3,command= self.cos)
        button_cos.pack()
        
        #Fourth Row, function key

        label_sqrt = Label(label_fkey, bg ='black')
        label_sqrt.grid(row=3,column=0,sticky=W, pady=10)
        button_sqrt = Button(label_sqrt, text='√', font=('Helvetica', '16'), height=1, width=3,command= self.sqrt)
        button_sqrt.pack()
    
        label_log = Label(label_fkey, bg ='black')
        label_log.grid(row=3,column=1,sticky=W, pady=10)
        button_log = Button(label_log, text='log', font=('Helvetica', '16'), height=1, width=3,command= self.log)
        button_log.pack()


        label_tan = Label(label_fkey, bg ='black')
        label_tan.grid(row=3,column=2,sticky=W)
        button_tan = Button(label_tan, text='tan', font=('Helvetica', '16'),bd=3, height=1, width=3,command= self.tan)
        button_tan.pack()
        
        #Fifth Row, function key
        label_square = Label(label_fkey, bg ='black')
        label_square.grid(row=4,column=0,sticky=W)
        button_square = Button(label_square, text='sq2', font=('Helvetica', '16'), height=1, width=3,command= self.square)
        button_square.pack()
    
        label_inverse = Label(label_fkey, bg ='black')
        label_inverse.grid(row=4,column=1,sticky=W)
        button_inverse = Button(label_inverse, text='1/x ', font=('Helvetica', '16'), height=1, width=3,command= self.inverse)
        button_inverse.pack()
#        
        label_fact = Label(label_fkey, bg ='black')
        label_fact.grid(row=4,column=2,sticky=E)
        button_fact = Button(label_fact, text='!', font=('Helvetica', '16'),bd=3, height=1, width=3,command= self.fact)
        button_fact.pack()
        

# run calculator     
if __name__ == '__main__':
    c = Calculator(root)
    root.title("Matthew\'s Calculator")
    root.mainloop()