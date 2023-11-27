'''Created by Team Entity🌐
        By 1. Srajan B Shetty (Team Leader)
           2. Binod BK (Team Member)
           3. Vinay Shetty (Team Member)
    Thankyou for the support'''
    
import re
import smtplib
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from dotenv import load_dotenv
load_dotenv()
import os

mail_id = os.getenv("mail_id")
password = os.getenv("app_password")

valcheck = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def submitact():  
    sender_name = sender_name_entry.get()
    sender_email = sender_email_entry.get()
    recipient_name = recipient_name_entry.get()
    recipient_email = recipient_email_entry.get()
    subject = subject_entry.get()
    message_body = msg.get(1.0, "end-1c")

    if re.fullmatch(valcheck, sender_email) and re.fullmatch(valcheck, recipient_email):
        print("Valid Email")
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        #use mail id and password from .env file
        server.login(mail_id, password)

        email_content = f"From: {sender_name} <{sender_email}>\n"
        email_content += f"To: {recipient_name} <{recipient_email}>\n"
        email_content += f"Subject: {subject}\n\n"
        email_content += message_body

        server.sendmail(sender_email, recipient_email, email_content)
        print("Mail sent successfully\n")          
        messagebox.showinfo("Attention", "Your Mail has been sent successfully.")
        server.quit()
        #clear the fields
        sender_name_entry.delete(0, END)
        sender_email_entry.delete(0, END)
        recipient_name_entry.delete(0, END)
        recipient_email_entry.delete(0, END)
        subject_entry.delete(0, END)
        msg.delete(1.0, END)
    else:
        messagebox.showinfo("Caution", "Enter valid email addresses")

root = Tk()
root.geometry("400x500")
root.title("Spark Mail")
root['background'] = '#1B1A17'
pho = PhotoImage(file="win.png")

rr = tk.Label(root, text="Email Sender")
rr.place(x=115, y=25)
rr.placeholder = 0
rr.configure(foreground="#F0A500", background="#1B1A17", font=("Helvetica", 18, "bold"))

# Entry fields for sender's information
sender_name_label = tk.Label(root, text="Your Name:")
sender_name_label.place(x=70, y=65)
sender_name_label.configure(foreground="#F0A500", background="#1B1A17")
sender_name_entry = tk.Entry(root, width=35)
sender_name_entry.place(x=200, y=65, width=150)
sender_name_entry.configure(foreground="#F0A500", background="#1B1A17")

sender_email_label = tk.Label(root, text="Your Email:")
sender_email_label.place(x=70, y=95)
sender_email_label.configure(foreground="#F0A500", background="#1B1A17")
sender_email_entry = tk.Entry(root, width=35)
sender_email_entry.place(x=200, y=95, width=150)
sender_email_entry.configure(foreground="#F0A500", background="#1B1A17")

# Entry fields for recipient's information
recipient_name_label = tk.Label(root, text="Recipient's Name:")
recipient_name_label.place(x=70, y=125)
recipient_name_label.configure(foreground="#F0A500", background="#1B1A17")
recipient_name_entry = tk.Entry(root, width=35)
recipient_name_entry.place(x=200, y=125, width=150)
recipient_name_entry.configure(foreground="#F0A500", background="#1B1A17")

recipient_email_label = tk.Label(root, text="Recipient's Email:")
recipient_email_label.place(x=70, y=155)
recipient_email_label.configure(foreground="#F0A500", background="#1B1A17")
recipient_email_entry = tk.Entry(root, width=35)
recipient_email_entry.place(x=200, y=155, width=150)
recipient_email_entry.configure(foreground="#F0A500", background="#1B1A17")

# Entry field for the subject
subject_label = tk.Label(root, text="Subject:")
subject_label.place(x=70, y=185)
subject_label.configure(foreground="#F0A500", background="#1B1A17")
subject_entry = tk.Entry(root, width=35)
subject_entry.place(x=200, y=185, width=150)
subject_entry.configure(foreground="#F0A500", background="#1B1A17")

# Entry field for the message
msg_label = tk.Label(root, text="Message:")
msg_label.place(x=70, y=215)
msg_label.configure(foreground="#F0A500", background="#1B1A17")
msg = tk.Text(root, width=35)
msg.place(x=200, y=215, width=150, height=50)
msg.configure(foreground="#F0A500", background="#1B1A17")

# Button to send the email
submitbtn = tk.Button(root, text="Send Mail", command=submitact, border=0)
submitbtn.place(x=145, y=275, width=130)
submitbtn.configure(foreground="black", background="#116530", image=pho, compound="right")

root.mainloop()
