

from tkinter import *
root=Tk()
root.geometry("400x600")
root.title("Calculator")

root.configure(background="yellow")



Label(root,text=" EMI CALCULATOR",bg="yellow",relief="solid",font=("Helvetica",20,"bold")).pack(side=TOP)
Label(root,text="Application Version1.0",bg="yellow",fg="red").pack(side=BOTTOM)

Label(root,text="Loan Amount",bg="yellow",font=12,width=15,relief="solid").place(x=30,y=250)
Label(root,text="Loan Rate",bg="yellow",font=12,width=15,relief="solid").place(x=30,y=290)
Label(root,text="Loan Tenure",bg="yellow",font=12,width=15,relief="solid").place(x=30,y=330)
Label(root,text="Loan Emi",bg="yellow",font=12,width=15,relief="solid").place(x=30,y=370)


la=StringVar()
lr=StringVar()
lt=StringVar()
Entry(root,textvariable=la).place(x=220,y=250)
Entry(root,textvariable=lr).place(x=220,y=290)
Entry(root,textvariable=lt).place(x=220,y=330)

def chootabhim():
    root.destroy()
    
def submit():
    p=float(la.get())
    r=float(lr.get())
    t=float(lt.get()) 
    R=r/(12*100)
    T=t*12
    emi=((p*r*(1+r)**t)/((1+r)**t)-1)
    Label(root,text=" "*10,font=10,bg="yellow").place(x=220,y=370)
    Label(root,text=str(round(emi)),font=10,bg="yellow").place(x=220,y=370)
    
          
Button(root,text="Calculate Emi",width=15,command=submit).place(x=50,y=450)
Button(root,text="Termination",width=15,command=chootabhim).place(x=240,y=450)
          


root.resizable(0,0)
root.mainloop()

