#This program was written using Python 3.6.8
import math
import tkinter as tk
from tkinter import messagebox
class quad:
    def calc(a,b,c,s1,s2,result):#function to calculate the roots, sum of the roots, product of the roots and difference of the roots
        result.delete("all")
        result.create_rectangle(5,5,495,245)
        if s1=='' or s2=='':
            tk.messagebox.showerror("ERROR","Please select an operator")
        elif b=='':
            tk.messagebox.showerror("ERROR","Please enter a value for b")
        elif c=='':
            tk.messagebox.showerror("ERROR","Please enter a value for c")
        else:
            if s1=='-' and int(b)<0:
                s1='+'
                b=-b
            if s2=='-' and int(c)<0:
                s2='+'
                c=-c
            b=s1+b
            c=s2+c
            if a=='' or a=='0':
                x=-int(c)/int(b)
                print(x)
                if x==-0:
                    x=0
                result.create_text(20,20,text="Given equation:\t\t"+b+"x"+c, anchor="w")
                result.create_text(20,40,text="Type of equation:\t\tLinear Equation", anchor="w")
                result.create_text(20,60,text="Root (value of x):\t\t"+str(x), anchor="w")
            else:
                result.create_text(20,20,text="Given equation:\t\t"+a+"x "+b+"x"+c, anchor="w")
                result.create_text(175,13,text="2", anchor="w",font=("",6))
                result.create_text(20,40,text="Type of equation:\t\tQuadratic Equation", anchor="w")
                d=int(b)**2 - (4*int(a)*int(c))
                if d<0:
                    r=-int(b)/2*int(a)
                    i=math.sqrt(abs(d))/(2*int(a))
                    result.create_text(20,60,text="Type of roots:\t\tImaginary", anchor="w")
                    result.create_text(20,80,text="Root 1 =\t\t\t"+str(r)+" + "+str(i)+" i", anchor="w")
                    result.create_text(20,100,text="Root 2 =\t\t\t"+str(r)+" - "+str(i)+" i", anchor="w")
                    result.create_text(20,120,text="Sum of roots =\t\t"+str(-int(b)/int(a)), anchor="w")
                    result.create_text(20,140,text="Product of roots =\t"+str(int(c)/int(a)), anchor="w")
                    result.create_text(20,160,text="Difference of roots =\t"+str(math.sqrt(abs(d))/int(a))+" i", anchor="w")
                else:
                    r1=(-int(b)+math.sqrt(d))/(2*int(a))
                    r2=(-int(b)-math.sqrt(d))/(2*int(a))
                    result.create_text(20,60,text="Type of roots:\t\tReal", anchor="w")
                    result.create_text(20,80,text="Root 1 =\t\t\t"+str(r1), anchor="w")
                    result.create_text(20,100,text="Root 2 =\t\t\t"+str(r2), anchor="w")
                    result.create_text(20,120,text="Sum of roots =\t\t"+str(-int(b)/int(a)), anchor="w")
                    result.create_text(20,140,text="Product of roots =\t"+str(int(c)/int(a)), anchor="w")
                    result.create_text(20,160,text="Difference of roots =\t"+str(math.sqrt(abs(d))/int(a)), anchor="w")

    def __init__(main):
        #Creating a user interface
        root=tk.Tk()
        root.geometry("500x500")
        root.title("Quadratic Equation Solver")
        root.after(1,lambda:root.focus_force())
        canvas=tk.Canvas(root, height=500, width=500,background="#fffdf5", highlightthickness=0)
        canvas.pack()
        result=tk.Canvas(canvas, height=250, width=500, background="#fffdf5")
        result.place(x=250, y=250, anchor="n")
        result.create_rectangle(5,5,495,245)
        in1=tk.Entry(canvas, width=7,relief='groove',borderwidth=2)
        in2=tk.Entry(canvas, width=7,relief='groove',borderwidth=2)
        in3=tk.Entry(canvas, width=7,relief='groove',borderwidth=2)
        symvar1=tk.StringVar(canvas)
        symvar2=tk.StringVar(canvas)
        sym1=tk.OptionMenu(canvas,symvar1,'+','-')
        sym1.config(font=("",12))
        sym2=tk.OptionMenu(canvas,symvar2,'+','-')
        sym2.config(font=("",12))
        submit=tk.Button(canvas,text="SUBMIT",command=lambda:quad.calc(in1.get(),in2.get(),in3.get(),symvar1.get(),symvar2.get(),result))
        in1.place(x=80, y=150, anchor='center')
        in2.place(x=230, y=150, anchor='center')
        in3.place(x=380, y=150, anchor='center')
        sym1.place(x=165, y=150, anchor='center')
        sym2.place(x=315, y=150, anchor='center')
        submit.place(x=250, y=200, anchor='center')
        canvas.create_text(250,30,text="QUADRATIC EQUATION SOLVER",font=("Times New Roman",20,'bold'))
        canvas.create_text(20,80,text='''A quadratic equation is of the form ax  +bx+c=0
Enter the values for a,b,c and select the operators:''',anchor="w", font=("Times New Roman",12))
        canvas.create_text(250,67,text="2", font=("Times New Roman",8))
        canvas.create_text(430,150,text="= 0", font=("Times New Roman",18))
        canvas.create_text(80,125,text="a", font=("Times New Roman",18))
        canvas.create_text(230,125,text="b", font=("Times New Roman",18))
        canvas.create_text(380,125,text="c", font=("Times New Roman",18))
        canvas.create_text(120,150,text="x", font=("Times New Roman",18))
        canvas.create_text(130,140,text="2", font=("Times New Roman",10))
        canvas.create_text(275,150,text="x", font=("Times New Roman",18))
        
quad()