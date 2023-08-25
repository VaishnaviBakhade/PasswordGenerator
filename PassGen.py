from tkinter import*
from tkinter import font
import random
import string
root = Tk()
root.geometry('500x450+500+200')
root.title("Password Generator")
root.configure(background='white')

t1=Label(root,text='Password Generator',font=('times new roman',20,'bold','underline'),fg='blue')
t1.place(x=200,y=0)

t2=Label(root,text='Enter user name:',font=('times new roman',15,))
t2.place(x=65,y=80)
t2=Entry(root,font=('times new roman',15))
t2.place(x=255,y=80)

#Length
t3=Label(root,text='Enter password length:',font=('times new roman',15))
t3.place(x=20,y=140)
t_len=IntVar()
t3=Entry(root,textvariable=t_len,font=('times new roman',15))
t3.place(x=255,y=140)

t4=Label(root,text='Generated password:',font=('times new roman',15))
t4.place(x=35,y=200)
t_str=StringVar()
t4=Entry(root,textvariable=t_str,font=('times new roman',15),fg='green')
t4.place(x=255,y=200)

def gen():
    length = t3.get()
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*_+=-'
    characters = alpha + numbers + symbols
    password ="".join(random.sample(characters,int(length)))
    t_str.set(password)



#Button
b=Button(root,text="Generate Password", command=gen,font=('times new roman',18,'bold'),background='blue',fg='white')
b.place(x=250,y=250)

b1=Button(root,text="Accept",font=('times new roman',15,'bold'),fg='blue')
b1.place(x=300,y=320)

b2=Button(root,text="Reset",font=('times new roman',15,'bold'),fg='blue')
b2.place(x=305,y=380)

root.mainloop()