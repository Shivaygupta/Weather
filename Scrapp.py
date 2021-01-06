import requests
import sqlite3
from bs4 import BeautifulSoup
from tkinter import messagebox


def req1():
    s_id=1
    c_id=-1
    z=0
    val=[]
    
    #Request and acessing the information

    page = requests.get("http://hydro.imd.gov.in/hydrometweb/(S(xdcvtz5521tdjjub1ejwgoes))/landing.aspx")
    soup=BeautifulSoup(page.content,'html5lib')
    a=soup.find(id='marqueecontainer')
    d=a.div.table

    #Storing information into database 

    conn=sqlite3.connect("Information_weather.sqlite3")
    cur=conn.cursor()
    cur.execute('drop table if exists States')
    cur.execute('drop table if exists Cities')

    cur.execute('''create table States(
                                State_id Integer Primary key ,
                                State_name Text unique      )''')
    conn.commit()

    cur.execute('''create table Cities(
                                City_Id Integer Primary key ,
                                City_Name Text ,
                                State_id Integer ,
                                Rainfall Text              )''')
    conn.commit()

    for tr in d.find_all('tr'):
        c_id+=1
        
        for td  in tr.find_all('td'):
            tds=td.font.span.string
            val.append(tds)
            a=0

        if(a==0):
            
            try:
                cur.execute('insert into States values (?,?) ' ,(s_id,val[0]))
                
            except sqlite3.IntegrityError :
                z+=0
        
            else:
                s_id+=1
                conn.commit()

            cur.execute('insert into Cities values (?,?,?,?) ' ,(c_id,val[1],(s_id-1),val[2]))
            conn.commit()

        val.clear()
        
    messagebox.showinfo(" DataBase "," Successfully Updated! ")
