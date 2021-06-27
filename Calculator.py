#import tkinter as t
from tkinter import *
from math import *
win=Tk()


o="Orange"
r="Red"
w="White"



e1=Entry(win,width=10)
e2=Entry(win,width=10)
e1.grid(column=1,row=1,ipady=10)
e2.grid(column=1,row=2,ipady=10)



print=Label(text="",padx=0,pady=0)
print.grid(column=3,row=3)



def addclick():
	add=float(e1.get())+float(e2.get())
	#print=Label(win,text="="+str(add))
	print.config(text="= "+str(add),padx=0,pady=0)
	print.grid(column=1,row=51)
def subclick():
	sub=float(e1.get())-float(e2.get())
	#print=Label(win,text="="+str(sub))
	print.config(text="= "+str(sub),padx=0,pady=0)
	print.grid(column=1,row=51)
def mulclick():
	mul=float(e1.get())*float(e2.get())
	#print=Label(win,text="="+str(mul))
	print.config(text="= "+str(mul),padx=0,pady=0)
	print.grid(column=1,row=51)
	
def divclick():
	div=float(e1.get())/float(e2.get())
	#print=Label(win,text="="+str(div))
	print.config(text="= "+str(round(div,7)),padx=0,pady=0)
	print.grid(column=1,row=51)
def remainder():
	rem=int(e1.get())%int(e2.get())
	print.config(text="= "+str(rem),padx=0,pady=0)
	print.grid(column=1,row=51)
def nlog():
	rem=log(int(e1.get()))
	print.config(text="= "+str(rem),padx=0,pady=0)
	print.grid(column=1,row=51)
def expe():
	rem=exp(float(e1.get()))
	print.config(text="= "+str(rem),padx=0,pady=0)
	print.grid(column=1,row=51)
def upar():
	rem=float(e1.get())**float(e2.get())
	print.config(text="= "+str(rem),padx=0,pady=0)
	print.grid(column=1,row=51)
def log():
	rem=log10(int(e1.get()))
	print.config(text="= "+str(rem),padx=0,pady=0)
	print.grid(column=1,row=51)
def clear():
		print.config(text="",padx=0,pady=0)
	
	
	

bt1=Button(text="+",command=addclick,bg=o,fg=w)
bt1.grid(column=10,row=1)
bt2=Button(text="-",command=subclick,bg=o,fg=w)
bt2.grid(column=11,row=1)
bt3=Button(text="x",command=mulclick,bg=o,fg=w)
bt3.grid(column=10,row=2)
bt4=Button(text="÷",command=divclick,bg=o,fg=w)
bt4.grid(column=11,row=2)
bt5=Button(text="%",command=remainder,bg=o,fg=w)
bt5.grid(column=10,row=3)

bt6=Button(text="lnx",command=nlog,bg=o,fg=w)
bt6.grid(column=11,row=3)


bt7=Button(text="e^x",command=expe,bg=o,fg=w)
bt7.grid(column=10,row=5)


bt8=Button(text="x^y",command=upar,bg=o,fg=w)
bt8.grid(column=11,row=4)

bt9=Button(text="logx",command=log,bg=o,fg=w)
bt9.grid(column=10,row=4)

btclear=Button(text="Clear",command=clear,bg=r,fg=w)
btclear.grid(column=1,row=10)


win.title("Calculator by Anand Kumar")



steps=Label(text="*Enter 1st and 2nd numbers \nin desired place and choose\n desired operation.\nAnswer will be displayed",fg="Red",font=("Algerian",5),padx=0,pady=0,relief="sunken")
steps.grid(column=1,row=50)




win.mainloop()