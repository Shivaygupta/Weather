from tkinter import *
import sqlite3
from tkinter import ttk
from matplotlib import style , pyplot as plt
from Scrapp import req1

state=[]

def xyz(i):
    i+=1
    i=str(i)
    l=i
    city=cur.execute("Select City_name,City_id from Cities where State_id = " + i)
    print(i)
    for row in city:
        print(row)
    abc(i)

def abc(i):
    rain_c=[]
    rain_v=[]
    data3=cur.execute('select City_id,Rainfall from Cities where State_id = '+i)

    for row in data3:
        rain_c.append(int(row[0]))
        rain_v.append(float(row[1]))

    plt.bar( rain_c, rain_v , width=0.5)

    plt.xlabel='CITIES ID'
    plt.ylabel='in mm'
    plt.title('information')
    plt.show()

def bye():
    exit()
    
def refresh():
    req1()
    
conn=sqlite3.connect("Information_weather.sqlite3")
cur=conn.cursor()
s_data=cur.execute("Select State_name from States")
for row in s_data:
    state.append(row)
    
hs=Tk()
hs.title("Rainfall Information System")
hs.geometry("450x300")

l1=Label(text=""" Welcome To
Rainfall Information System""" , font=("Agency" , 25))
l1.pack()

l2=Label(text="""
Select State
then the data will come in graphical form
""" , font=("Agency" , 10))
l2.pack()

combo1 = ttk.Combobox(values=state)
combo1.pack()
combo1.bind("<<ComboboxSelected>>", lambda _ : xyz(combo1.current()))
    
b1=Button(text="REFRESH", command=refresh)
b1.pack()
    
b2=Button(text="Exit", command=bye)
b2.pack()

hs.mainloop()
