from tkinter import *
import tkinter as tk
import subprocess

root = Tk()

#Providing Geometry to the form
root.geometry("500x820")
root.resizable(False,False)
#Providing title to the form
root.title('Main Menu')

def opt1():
    s = subprocess.check_call("python booking.py", shell = True)

def opt2():
    s = subprocess.check_call("python enquiry.py", shell = True)

def main_gui():
    Font_tuple = ("Comic Sans MS", 20, "bold")
    c =Canvas(root,bg = "#1868ae", width=500, height = 820)

    c.place(x=0,y=10)
    c =Canvas(root,bg = "#c6d7eb", width=400, height = 720)

    c.place(x=50,y=60)
    Font_tuple = ("Comic Sans MS", 20, "bold")

    label_0 =Label(root,text="Main menu",bg="#1868ae",foreground="white",width=0,font=("Comic Sans MS", 20, "bold"))
    label_0.place(x=190,y=15)

    title =Label(root,text="Cost calculation of rental cars using",bg="#c6d7eb",foreground="black",width=0,font=("Comic Sans MS", 15, "bold"))
    title.place(x=70,y=80)

    title =Label(root,text="Floyd’s warshall algorithm",bg="#c6d7eb",foreground="black",width=0,font=("Comic Sans MS", 15, "bold"))
    title.place(x=120,y=120)


    label_name =Label(root,text="Booking",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",20,"bold"))
    label_name.place(x=80,y=300)

    Button(root, text='Click To Book' , width=20,bg="#1868ae",fg='white',
    command = lambda: opt1()).place(x=180,y=360)

    label_email =Label(root,text="Enquiry",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",20,"bold"))
    label_email.place(x=80,y=500)

    Button(root, text='Click To Enquire' , width=20,bg="#1868ae",fg='white',
            command = lambda: opt2()).place(x=180,y=560)


main_gui()
#this will run the mainloop.
root.mainloop()
