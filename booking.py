import xlrd
import smtplib
import gmplot
import os
import webbrowser
import random
from datetime import date
from tkinter import *
import tkinter as tk
# from firebase import firebase
#Creating object 'root' of Tk()
root = Tk()

#Providing Geometry to the form
root.geometry("500x820")
root.resizable(False,False)
#Providing title to the form
root.title('Booking Tab')

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

# def data(name, receiver_email, start_date, end_date, car_model, fuel_choice,car_rate, no_of_km, price_per_km, total_cost, start_city, end_city):
#     fb = firebase.FirebaseApplication('https://car-rental-a090d-default-rtdb.firebaseio.com/', None)
#     data =  { 'Name': name,
#     'Email': receiver_email,
#     'start date': start_date,
#     'end date': end_date,
#     'start city': start_city,
#     'end city': end_city,
#     'car model': car_model,
#     'fuel choice': fuel_choice,
#     'car rate': car_rate,
#     'no of km': no_of_km,
#     'price per km': price_per_km,
#     'total cost': total_cost}
#     send = '/car-rental-a090d-default-rtdb/'+name
#     result = fb.post(send,data)
#     print(result)

def email(name, receiver_email, start_date, end_date, car_model, fuel_choice, car_rate, no_of_km, price_per_km, total_cost,start_city,end_city):
    email_adress = os.environ.get("my_email_adress")
    email_password = os.environ.get("my_email_password")
    subject = "Your booking has been confirmed"
    body = "Hi "+str(name)+",\nYour Booking has been confirmed\nstart date: "+str(start_date)+"\nend date: "+str(end_date)+"\nstart city: "+str(start_city)+"\nend city: "+str(end_city)+"\nSegment of  the car: "+str(car_model)+"\n\nFARE DETAILS\nBase price: Rupees "+str(car_rate)+"\nDoorstep Delivery and Pickup: Rupees 500/- \nInsurance & GST: Included\nRefundable Security Deposit: Rupees 1000/-  \nTotal: Rupees "+str(total_cost)+"/-"+"\n\nTotal traveling distance in km: "+str(no_of_km)+"km\nPrice per km as per your traveling distance is: Rupees "+str(price_per_km)+"/km  \nFuel charges: "+str(fuel_choice)+"\nTolls & Parking: To be paid by you\nThank you. Have a  safe journey"
    body = body.encode('ascii', 'ignore').decode('ascii')
    if subject != None or body != None:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(email_adress, email_password)
            msg = f"Subject: {subject}\n\n{body}"
            smtp.sendmail(email_adress, receiver_email, msg)
            label_name =Label(root,text="Order Confirmation Details Sent To Your Email",bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
            label_name.place(x=80,y=680)

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

def add_vertex(v):
  global graph
  global vertices_no
  global vertices
  if v in vertices:
    print("Vertex ", v, " already exists")
  else:
    vertices_no = vertices_no + 1
    vertices.append(v)
    if vertices_no > 1:
        for vertex in graph:
            vertex.append(0)
    temp = []
    for i in range(vertices_no):
        temp.append(0)
    graph.append(temp)

# Add an edge between vertex v1 and v2 with edge weight e
def add_edge(v1, v2, e):
    global graph
    global vertices_no
    global vertices
    # Check if vertex v1 is a valid vertex
    if v1 not in vertices:
        print("Vertex ", v1, " does not exist.")
    # Check if vertex v1 is a valid vertex
    elif v2 not in vertices:
        print("Vertex ", v2, " does not exist.")
    # Since this code is not restricted to a directed or
    # an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e

def print_graph():
  global graph
  global vertices_no
  for i in range(vertices_no):
    for j in range(vertices_no):
      if graph[i][j] != 0:
        print(vertices[i], " -> ", vertices[j], \
        " edge weight: ", graph[i][j],"\n")

# Print the internal graph/adjacency matrix
def print_gadjacency_matrix():
  global graph
  global vertices_no
  global I
  for i in range(vertices_no):
    for j in range(vertices_no):
        if i != j:
            if graph[i][j] == 0:
                graph[i][j] = I

# Recursive function to print the path of given vertex `u` from source vertex `v`
def printPath(path, v, u):

    if path[v][u] == v:
        return

    printPath(path, v, path[v][u])
    #print(path[v][u], end=' ')
    f = open("data.txt", "a")
    f.write(str(path[v][u]) + "\n")
    f.close()

# Function to print the shortest cost with path
# information between all pairs of vertices
def printSolution(path, v, u):
    if u != v and path[v][u] != -1:
        print(f"The shortest path from {v} —> {u} is ({v}", end=' ')
        f = open("data.txt", "a")
        f.write(f"{v}\n")
        f.close()
        printPath(path, v, u)
        print(f"{u})")
        f = open("data.txt", "a")
        f.write(f"{u}")
        f.close()

# Function to run the Floyd–Warshall algorithm
def floydWarshall(adjMatrix, N):

    # cost and parent matrix stores shortest path
    # (shortest-cost/shortest route) information

    # initially, cost would be the same as the weight of an edge
    global cost
    global path
    cost = adjMatrix.copy()
    path = [[None for x in range(N)] for y in range(N)]

    # initialize cost and parent
    for v in range(N):
        for u in range(N):
            if v == u:
                path[v][u] = 0
            elif cost[v][u] != float('inf'):
                path[v][u] = v
            else:
                path[v][u] = -1

    # run Floyd–Warshall
    for k in range(N):
        for v in range(N):
            for u in range(N):
                # If vertex `k` is on the shortest path from `v` to `u`,
                # then update the value of `cost[v][u]` and `path[v][u]`
                if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                        and (cost[v][k] + cost[k][u] < cost[v][u]):
                    cost[v][u] = cost[v][k] + cost[k][u]
                    path[v][u] = path[k][u]

            # if diagonal elements become negative, the
            # graph contains a negative-weight cycle
            if cost[v][v] < 0:
                print("Negative-weight cycle found")
                return

    #ask_anything(cost,path,N)
    booking_gui(cost,path,N)



def calculate_price_per_km(no_of_km):
    if no_of_km >= 900:
        return 6

    elif no_of_km >= 700:
        return 8

    elif no_of_km >= 500:
        return 10

    elif no_of_km >= 300:
        return 12

    else:
        return 13

def printPath(path, v, u):

    if path[v][u] == v:
        return

    printPath(path, v, path[v][u])
    print(path[v][u], end=' ')
    f = open("data.txt", "a")
    f.write(str(path[v][u]) + "\n")
    f.close()

# Function to print the shortest cost with path
# information between all pairs of vertices
def printSolution(path, v, u):
    if u != v and path[v][u] != -1:
        print(f"The shortest path from {v} —> {u} is ({v}", end=' ')
        f = open("data.txt", "a")
        f.write(f"{v}\n")
        f.close()
        printPath(path, v, u)
        print(f"{u})")
        f = open("data.txt", "a")
        f.write(f"{u}")
        f.close()

def locate(lat,lang):
    gmapOne = gmplot.GoogleMapPlotter(14.4661266,75.9206361,7)
    gmapOne.scatter(lat,lang,"#FF0000" , size =50, marker = False)
    gmapOne.plot(lat,lang,'cornflowerblue', edge_width=2.5)
    gmapOne.draw("map.html")

def verify_email(otp,name, receiver_email, start_date, end_date, car_model, fuel_choice,car_rate, no_of_km, price_per_km, total_cost,start_city,end_city):
    input_otp = otp_var.get()
    if int(input_otp) == otp:
        label_name =Label(root,text="OTP varified Succsessfully...",bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=650)
        email(name, receiver_email, start_date, end_date, car_model, fuel_choice,car_rate, no_of_km, price_per_km, total_cost,start_city,end_city)
        # data(name, receiver_email, start_date, end_date, car_model, fuel_choice,car_rate, no_of_km, price_per_km, total_cost,start_city,end_city)
        label_name =Label(root,text="Thank you for choosing us.",bg = "#c6d7eb",foreground="black",width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=710)
        label_name =Label(root,text="Wishing you a safe and joyfull journey ahead...",bg = "#c6d7eb",foreground="black",width=0,font=("Comic Sans MS",10,"bold"))
        label_name.place(x=80,y=740)
    else:
        print("Invalid OTP")




def booking_work(cost,path,N):
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

    #name
    a,b,c = start_time.split("/")
    d,e,f = end_time.split("/")
    f_date = date(int(c), int(b), int(a))
    l_date = date(int(f), int(e), int(d))
    delta = l_date - f_date
    days_used = delta.days
    #days_used
    #car_choice
    if car_choice == "HATCHBACK":
        if fuel_choice == 1:
            car_rate,fuel = 2100,"Included"
        else:
            car_rate,fuel = 1200,"Not Included"
    elif car_choice == "SUV":
        if fuel_choice == 1:
            car_rate,fuel = 2400,"Included"
        else:
            car_rate,fuel = 1700,"Not Included"
    elif car_choice == "SEDAN":
        if fuel_choice == 1:
            car_rate,fuel = 2500,"Included"
        else:
            car_rate,fuel = 1900,"Not Included"
    elif car_choice == "LUXURY":
        if fuel_choice == 1:
            car_rate,fuel = 14300,"Included"
        else:
            car_rate,fuel = 10800,"Not Included"
    #car_rate
    #fuel
    my_city_list = []
    loc = ("daa location.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in range(sheet.nrows):
        city = sheet.cell_value(i, 1)
        my_city_list.append(city)
    first_city = my_city_list.index(start_city)
    second_city = my_city_list.index(end_city)
    v = first_city
    u = second_city
    printSolution(path, v, u)
    no_of_km = cost[v][u]
    print(no_of_km)

    if map == 1:
        location = ("daa location.xlsx")
        wb = xlrd.open_workbook(location)
        sheet_location = wb.sheet_by_index(0)
        latitude = []
        longitude= []
        f = open("data.txt", "r")
        numbers = f.read()
        numbers = numbers.split()
        for i in numbers:
            lat = float(sheet_location.cell_value(int(i), 2))
            lang = float(sheet_location.cell_value(int(i), 3))
            latitude.append(lat)
            longitude.append(lang)
        locate(latitude,longitude)
        webbrowser.open(r'file://C:\Users\USER\Desktop\daa\map.html')

    else:
        pass

    otp = random.randint(1000,9999)
    confirmation_email(name, email, otp)
    label_name =Label(root,text="Verify OTP sent to Email",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",10,"bold"))
    label_name.place(x=80,y=380)
    entry_name=Entry(root,textvariable = otp_var,bg="white",foreground="black")
    entry_name.place(x=270,y=380)
    #this will accept the input string text from the user.
    Button(root, text='Verify OTP' , width=20,bg="#1868ae",fg='white',
                command = lambda: verify_email(otp,name, email, start_time, end_time, car_choice, fuel,car_rate, no_of_km, price_per_km, total_cost,start_city,end_city)).place(x=180,y=410)
    c =Canvas(root,bg = "#1868ae", width=400, height = 50)
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    c.place(x=50,y=440)
    details_title =Label(root,text="Details",bg="#1868ae",foreground="white",width=0,font=("Comic Sans MS", 20, "bold"))
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    details_title.place(x=200,y=445)

    total_distance_statement = "Total Distance is: "+ str(no_of_km) +" KM\n"
    price_per_km = calculate_price_per_km(no_of_km)
    label_name =Label(root,text=total_distance_statement,bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
    label_name.place(x=80,y=500)

    price_per_km_statement = "Price per KM is: Rupees "+str(price_per_km)+"/km\n"
    total_cost = (price_per_km * no_of_km) + (days_used * 500) + car_rate + 1500
    label_name =Label(root,text=price_per_km_statement,bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
    label_name.place(x=80,y=530)

    doorstep_delivery_statement = "Doorstep Delivery and Pickup: Rupees 500/-\n"
    label_name =Label(root,text=doorstep_delivery_statement,bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
    label_name.place(x=80,y=560)

    Refundable_statement = "Refundable Security Deposit: Rupees 1000/-\n"
    label_name =Label(root,text=Refundable_statement,bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
    label_name.place(x=80,y=590)

    total_cost_statement = "Total Cost of fare is: Rupees "+str(total_cost)+"/-\n"
    label_name =Label(root,text=total_cost_statement,bg = "#c6d7eb",foreground="black", width=0,font=("Comic Sans MS",10,"bold"))
    label_name.place(x=80,y=620)

def booking_gui(cost,path,N):
    Font_tuple = ("Comic Sans MS", 20, "bold")
    c =Canvas(root,bg = "#1868ae", width=500, height = 820)
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    c.place(x=0,y=10)
    c =Canvas(root,bg = "#c6d7eb", width=400, height = 720)
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    c.place(x=50,y=60)
    #this creates 'Label' widget for Registration Form and uses place() method.
    label_0 =Label(root,text="Booking form",bg="#1868ae",foreground="white",width=0,font=("bold",20))
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

    #this creates 'Label' widget for Email and uses place() method.
    label_start_date =Label(root,text="Staring Date",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",10,"bold"))
    label_start_date.place(x=80,y=140)

    entry_start_date=Entry(root,textvariable = start_time_var,bg="white",foreground="black")
    entry_start_date.place(x=270,y=140)

    #this creates 'Label' widget for Email and uses place() method.
    label_end_date =Label(root,text="Ending Date",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",10,"bold"))
    label_end_date.place(x=80,y=170)

    entry_end_date=Entry(root,textvariable = end_time_var,bg="white",foreground="black")
    entry_end_date.place(x=270,y=170)

    ##this creates 'Label' widget for country and uses place() method.
    label_car_choice=Label(root,text="Car",bg = "#c6d7eb",foreground="black",width=20,font=("Comic Sans MS",10,"bold"))
    label_car_choice.place(x=80,y=200)

    #this creates list of countries available in the dropdownlist.
    list_of_car=['HATCHBACK' ,'SUV' , 'SEDAN' ,'LUXURY']

    #the variable 'c' mentioned here holds String Value, by default ""
    car_choice_var.set('Select your Car')
    droplist=OptionMenu(root,car_choice_var, *list_of_car)
    droplist.config(width=13,bg="white",foreground="black")
    droplist.place(x=270,y=190)

    #this creates 'Label' widget for Gender and uses place() method.
    label_fuel =Label(root,text="Fuel",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",10,"bold"))
    label_fuel.place(x=80,y=230)

    #the variable 'var' mentioned here holds Integer Value, by deault 0

    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,text="Yes",padx= 5, variable= fuel_choice_var, value=1,bg = "#c6d7eb").place(x=265,y=230)
    Radiobutton(root,text="No",padx= 20, variable= fuel_choice_var, value=2,bg = "#c6d7eb").place(x=320,y=230)

    ##this creates 'Label' widget for country and uses place() method.
    label_start_city=Label(root,text="Starting City",bg = "#c6d7eb",foreground="black",width=20,font=("Comic Sans MS",10,"bold"))
    label_start_city.place(x=80,y=260)
    list_of_city=[]
    loc = ("daa location.xlsx")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    for i in range(sheet.nrows):
        city = sheet.cell_value(i, 1)
        list_of_city.append(city)
    #this creates list of countries available in the dropdownlist.

    #the variable 'c' mentioned here holds String Value, by default ""

    droplist=OptionMenu(root,start_city_var, *list_of_city)
    droplist.config(width=13,bg="white",foreground="black")
    start_city_var.set('Select your City')
    droplist.place(x=270,y=260)

    label_5=Label(root,text="End City",bg = "#c6d7eb",foreground="black",width=20,font=("Comic Sans MS",10,"bold"))
    label_5.place(x=80,y=290)
    #this creates list of countries available in the dropdownlist.

    #the variable 'c' mentioned here holds String Value, by default ""

    droplist=OptionMenu(root,end_city_var, *list_of_city)
    droplist.config(width=13,bg = "white",foreground="black")
    end_city_var.set('Select your City')
    droplist.place(x=270,y=290)

    #this creates 'Label' widget for Gender and uses place() method.

    #the variable 'var' mentioned here holds Integer Value, by deault 0
    label_fuel =Label(root,text="View Map",bg = "#c6d7eb",foreground="black", width=20,font=("Comic Sans MS",10,"bold"))
    label_fuel.place(x=80,y=320)

    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,text="Yes",padx= 5, variable= map_var, value=1,bg = "#c6d7eb").place(x=265,y=320)
    Radiobutton(root,text="No",padx= 20, variable= map_var, value=2,bg = "#c6d7eb").place(x=320,y=320)

    Button(root, text='Submit' , width=20,bg="#1868ae",fg='white',
            command = lambda: booking_work(cost,path,N)).place(x=180,y=350)



if __name__ == '__main__':
    try:
        f = open("data.txt", "x")
    except:
        pass
    f = open("data.txt","r+")
    f.truncate(0)
    f.close()
    # Driver code
    # stores the vertices in the graph
    vertices = []
    # stores the number of vertices in the graph
    vertices_no = 0
    graph = []

    I = float('inf')
    # Total number of vertices in the `adjMatrix`
    loc = ("data.xlsx")

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    no_of_vertices = wb.sheet_by_index(1)

    N = int(no_of_vertices.cell_value(0, 0))
    #N =int(input("Enter Number of vertices:"))
    # Add vertices to the graph
    for i in range(N):
        add_vertex(i)

    # Add the edges between the vertices by specifying
    # the from and to vertex along with the edge weights.
    Done = True

    # For row 0 and column 0
    for i in range(sheet.nrows):
        From = int(sheet.cell_value(i, 0))
        To = int(sheet.cell_value(i, 1))
        Weights = int(sheet.cell_value(i, 2))
        add_edge(From, To, Weights)
        add_edge(To, From, Weights)
    #print_graph()
    print_gadjacency_matrix()
    #print("Internal representation: ", graph,"\n")
    # given adjacency representation of the matrix
    adjMatrix = graph
    # Run Floyd–Warshall algorithm
    floydWarshall(adjMatrix, N)

#this will run the mainloop.
root.mainloop()
