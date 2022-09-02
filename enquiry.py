import xlrd
import smtplib
import gmplot
import os
import webbrowser
import random
from datetime import date
from tkinter import *
import tkinter as tk
import xlrd
import firebase
#Creating object 'root' of Tk()
root = Tk()

#Providing Geometry to the form
root.geometry("500x820")
root.resizable(False,False)
#Providing title to the form
root.title('Enquiry Tab')

name_var=tk.StringVar()
email_var=tk.StringVar()
start_time_var=tk.StringVar()
end_time_var=tk.StringVar()
car_choice_var=StringVar()
fuel_choice_var=IntVar()
start_city_var=StringVar()
end_city_var=StringVar()
fuel_var=IntVar()
map_var=IntVar()
otp_var=StringVar()

elements_title = []
elements = []

def data_retrive(name, receiver_email):
    fb = firebase.FirebaseApplication('https://car-rental-a090d-default-rtdb.firebaseio.com/', None)
    result = fb.get('/car-rental-a090d-default-rtdb/'+name,'')
    for p_id, p_info in result.items():
        for key in p_info:
            elements_title.append(key)
            elements.append(p_info[key])

def confirmation_email(name, receiver_email, otp_number):
    email_adress = os.environ.get("my_email_adress")
    email_password = os.environ.get("my_email_password")
    subject = "Email Varification"
    body = f"Your OTP is {otp_number}"
    body = body.encode('ascii', 'ignore').decode('ascii')
    if subject != None or body != None:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email_adress, email_password)
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(email_adress, receiver_email, msg)

def verify_email(otp,name, receiver_email):
    input_otp = otp_var.get()
    if int(input_otp) == otp:
        label_name =Label(root,text="OTP varified Succsessfully...",bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=230)

        data_retrive(name, receiver_email)

        elements_title
        elements
        c =Canvas(root,bg = "#1868ae", width=400, height = 50)
        #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
        c.place(x=50,y=260)
        details_title =Label(root,text="Details",bg="#1868ae",foreground="white",width=0,font=("Comic Sans MS", 20, "bold"))
        #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
        details_title.place(x=200,y=265)

        label_name =Label(root,text=elements_title[0]+" : " + str(elements[0]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=320)

        label_name =Label(root,text=elements_title[1]+" : " + str(elements[1]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=350)

        label_name =Label(root,text=elements_title[2]+" : " + str(elements[2]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=380)

        label_name =Label(root,text=elements_title[3]+" : " + str(elements[3]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=410)

        label_name =Label(root,text=elements_title[4]+" : " + str(elements[4]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=440)

        label_name =Label(root,text=elements_title[5]+" : " + str(elements[5]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=470)

        label_name =Label(root,text=elements_title[6]+" : " + str(elements[6]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=500)

        label_name =Label(root,text=elements_title[7]+" : " + str(elements[7]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=530)

        label_name =Label(root,text=elements_title[8]+" : " + str(elements[8]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=560)

        label_name =Label(root,text=elements_title[9]+" : " + str(elements[9]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=590)

        label_name =Label(root,text= elements_title[10] + " : "+ str(elements[10]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=620)

        label_name =Label(root,text= elements_title[11] + " : "+ str(elements[11]),bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=650)

        label_name =Label(root,text="Thank you for choosing us.",bg = "#c6d7eb",foreground="black",width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=700)
    else:
        print("Invalid OTP")

def enquiry_work():
    name = name_var.get()
    email = email_var.get()
    start_time = start_time_var.get()
    end_time = end_time_var.get()
    car_choice = car_choice_var.get()
    fuel_choice = fuel_choice_var.get()
    start_city = start_city_var.get()
    end_city = end_city_var.get()
    fuel = fuel_var.get()
    map = map_var.get()

    otp = random.randint(1000,9999)
    confirmation_email(name, email, otp)
    label_name =Label(root,text="Verify OTP sent to Email",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",10,"bold"))
    label_name.place(x=80,y=170)
    entry_name=Entry(root,textvariable = otp_var,bg="white",foreground="black")
    entry_name.place(x=270,y=170)
    #this will accept the input string text from the user.
    Button(root, text='Verify OTP' , width=20,bg="#1868ae",fg='white',
                command = lambda: verify_email(otp,name, email)).place(x=180,y=200)

def enquiry_gui():
    Font_tuple = ("Comic Sans MS", 20, "bold")
    c =Canvas(root,bg = "#1868ae", width=500, height = 820)
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    c.place(x=0,y=10)
    c =Canvas(root,bg = "#c6d7eb", width=400, height = 720)
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    c.place(x=50,y=60)
    Font_tuple = ("Comic Sans MS", 20, "bold")
    #this creates 'Label' widget for Registration Form and uses place() method.
    label_0 =Label(root,text="Enquiry form",bg="#1868ae",foreground="white",width=0,font=("bold",20))
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.configure(font = Font_tuple)
    label_0.place(x=162,y=15)

    #this creates 'Label' widget for Fullname and uses place() method.
    label_name =Label(root,text="FullName",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",10,"bold"))
    label_name.place(x=80,y=80)

    #this will accept the input string text from the user.
    entry_name=Entry(root,textvariable = name_var,bg="white",foreground="black")
    entry_name.place(x=270,y=80)

    #this creates 'Label' widget for Email and uses place() method.
    label_email =Label(root,text="Email",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",10,"bold"))
    label_email.place(x=80,y=110)

    entry_email=Entry(root,textvariable = email_var,bg="white",foreground="black")
    entry_email.place(x=270,y=110)

    Button(root, text='Submit' , width=20,bg="#1868ae",fg='white',
            command = lambda: enquiry_work()).place(x=180,y=140)


enquiry_gui()

#this will run the mainloop.
root.mainloop()
