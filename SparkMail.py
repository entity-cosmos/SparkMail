'''Created by Team Entity🌐
        By 1. Srajan B Shetty (Team Leader)
           2. Binod BK (Team Member)
           3. Vinay Shetty (Team Member)
    Thankyou for the support'''
    
import re
from email import message
import smtplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from turtle import right

#valcheck stores the correct email id format
valcheck = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

#submitact is send mail buttons click event
def submitact():  
    #Here email validation and sending of mail to respective destination
    #validation of email id takes place
    if(re.fullmatch(valcheck, Usermail.get())):
        inp = msg.get(1.0, "end-1c")
        print("Valid Email")
        #after successfull validation, sendmail takes From, To and Message to send mail
        #Setting SMTP server to gmail.com
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        #Connecting google account to gmail via server.login
        server.login(usId.get(),pscode.get())
        server.sendmail("srajanbshetty@gmail.com",Usermail.get(),inp)
        print("Mail sent successfully\n")          
        #popup window to displays message of sending email
        messagebox.showinfo("Attention","Your Mail has been sent successfully.")
        #clearing the entry
        Usermail.delete(0, END)
        usId.delete(0, END)
        pscode.delete(0, END)
        msg.delete('1.0', END)
        #loging out of gmail
        server.quit()
    else:
        #popup window to show invalid email id
        messagebox.showinfo("Caution","Enter the valid mail")
         
#root window 
root = Tk()
root.geometry("400x500")
root.title("Spark Mail")
root['background']='#1B1A17'
pho=PhotoImage(file="win.png")
#heading
rr = tk.Label(root, text="Email Sender")
rr.place(x=115,y=25)
rr.placeholder=0
rr.configure(foreground="#F0A500",background="#1B1A17",font=("Helvetica",18,"bold"))

From = tk.Label(root, text ="From :")
From.place(x = 70, y = 125)
From.configure(foreground="#F0A500",background="#1B1A17")

usId = tk.Entry(root, width = 35)
usId.place(x = 200, y = 125, width = 150)
usId.configure(foreground="#F0A500",background="#1B1A17")

ps = tk.Label(root, text ="Password :")
ps.place(x = 70, y = 185)
ps.configure(foreground="#F0A500",background="#1B1A17")

pscode = tk.Entry(root, width = 35,show="*")
pscode.place(x = 200, y = 185, width = 150)
pscode.configure(foreground="#F0A500",background="#1B1A17")
#textbox 1
user = tk.Label(root, text ="To :")
user.place(x = 70, y = 245)
user.configure(foreground="#F0A500",background="#1B1A17")

#entry 1
Usermail = tk.Entry(root, width = 35)
Usermail.place(x = 200, y = 245, width = 150)
Usermail.configure(foreground="#F0A500",background="#1B1A17")

#textbox 2
mail = tk.Label(root, text ="Message :")
mail.place(x = 70, y = 305)
mail.configure(foreground="#F0A500",background="#1B1A17")


#entry 2
msg = tk.Text(root, width = 35)
msg.place(x = 200, y = 295, width = 150, height = 50)
msg.configure(foreground="#F0A500",background="#1B1A17")

#button
submitbtn = tk.Button(root, text="    Send Mail", command = submitact,border=0)
submitbtn.place(x = 145, y = 375, width = 130)
submitbtn.configure(foreground="black",background="#116530",image=pho,compound="right")

#closing the mainloop
root.mainloop()
