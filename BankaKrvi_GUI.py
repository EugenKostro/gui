import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import tkinter as tk

#konekcija

def connection():
    conn=pymysql.connect(host='localhost',user='root',password='root',database="Projekt_Banka_Krvi-2")
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)
        
    for array in read():
        my_tree.insert(parent='',index='end',iid=array,text="",values=(array),tag='orow')
        
    my_tree.tag_configure('orow',background='#EEEEEE',font=('Arial',12))
    my_tree.grid(row=8,column=0,columnspan=5,rowspan=11,padx=10,pady=20)
    
#GUI

root = Tk()
root.title("Banka krvi")
root.geometry("1700x900")
root.iconbitmap("krv.ico")
my_tree = ttk.Treeview(root)

#funkcije

def read():
    conn=connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM zaposlenik")
    rez=cursor.fetchall()
    conn.commit()
    conn.close()
    return rez

#GUI

label = Label(root, text = "Sustav upravljanja zaposlenicima", font=('Arial Bold',30))
label.grid(row=0,column=0,columnspan=8,rowspan=2,padx=50,pady=40)

zaposlenikIDLabel = Label(root,text = "id",font=('Arial',15))
zaposlenikImeLabel = Label(root,text = "Ime zaposlenika",font=('Arial',15)) 
zaposlenikPrezimeLabel = Label(root,text = "Prezime zaposlenika",font=('Arial',15)) 
zaposlenikDatumRodenjaLabel = Label(root,text = "Datum rođenja zaposlenika",font=('Arial',15)) 
zaposlenikAdresaLabel = Label(root,text = "Adresa zaposlenika",font=('Arial',15)) 
zaposlenikGradLabel = Label(root,text = "Grad zaposlenika",font=('Arial',15)) 
zaposlenikKontaktLabel = Label(root,text = "Kontakt zaposlenika",font=('Arial',15)) 
zaposlenikEmailLabel = Label(root,text = "Email zaposlenika",font=('Arial',15)) 
zaposlenikDatumZaposlenjaLabel = Label(root,text = "Datum zaposlenja zaposlenika",font=('Arial',15))  

zaposlenikIDLabel.grid(row=3,column=0,columnspan=1,padx=50,pady=5)
zaposlenikImeLabel.grid(row=4,column=0,columnspan=1,padx=50,pady=5)
zaposlenikPrezimeLabel.grid(row=5,column=0,columnspan=1,padx=50,pady=5)
zaposlenikDatumRodenjaLabel.grid(row=6,column=0,columnspan=1,padx=50,pady=5)
zaposlenikAdresaLabel.grid(row=7,column=0,columnspan=1,padx=50,pady=5)
zaposlenikGradLabel.grid(row=8,column=0,columnspan=1,padx=50,pady=5)
zaposlenikKontaktLabel.grid(row=9,column=0,columnspan=1,padx=50,pady=5)
zaposlenikEmailLabel.grid(row=10,column=0,columnspan=1,padx=50,pady=5)
zaposlenikDatumZaposlenjaLabel.grid(row=11,column=0,columnspan=1,padx=50,pady=5)

zaposlenikIDEntry=Entry(root,width=55,bd=5,font=('Arial',15))
zaposlenikImeEntry=Entry(root,width=55,bd=5,font=('Arial',15))
zaposlenikPrezimeEntry=Entry(root,width=55,bd=5,font=('Arial',15))
zaposlenikDatumRodenjaEntry=Entry(root,width=55,bd=5,font=('Arial',15))
zaposlenikAdresaEntry=Entry(root,width=55,bd=5,font=('Arial',15))
zaposlenikGradEntry=Entry(root,width=55,bd=5,font=('Arial',15))
zaposlenikKontaktEntry=Entry(root,width=55,bd=5,font=('Arial',15))
zaposlenikEmailEntry=Entry(root,width=55,bd=5,font=('Arial',15))
zaposlenikDatumZaposlenjaEntry=Entry(root,width=55,bd=5,font=('Arial',15))

zaposlenikIDEntry.grid(row=3,column=1,columnspan=4,padx=5,pady=0)
zaposlenikImeEntry.grid(row=4,column=1,columnspan=4,padx=5,pady=0)
zaposlenikPrezimeEntry.grid(row=5,column=1,columnspan=4,padx=5,pady=0)
zaposlenikDatumRodenjaEntry.grid(row=6,column=1,columnspan=4,padx=5,pady=0)
zaposlenikAdresaEntry.grid(row=7,column=1,columnspan=4,padx=5,pady=0)
zaposlenikGradEntry.grid(row=8,column=1,columnspan=4,padx=5,pady=0)
zaposlenikKontaktEntry.grid(row=9,column=1,columnspan=4,padx=5,pady=0)
zaposlenikEmailEntry.grid(row=10,column=1,columnspan=4,padx=5,pady=0)
zaposlenikDatumZaposlenjaEntry.grid(row=11,column=1,columnspan=4,padx=5,pady=0)


addBtn=Button(root, text="Dodaj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red")
updateBtn=Button(root, text="Ažuriraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red")
deleteBtn=Button(root, text="Izbriši",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red")
searchBtn=Button(root, text="Pretraži",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red")
resetBtn=Button(root, text="Resetiraj",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red")
selectBtn=Button(root, text="Izaberi",padx=65,pady=25,width=10,bd=5,font=('Arial',15),bg="white",fg="red")

addBtn.grid(row=3,column=5,columnspan=1,rowspan=2)
updateBtn.grid(row=5,column=5,columnspan=1,rowspan=2)
deleteBtn.grid(row=7,column=5,columnspan=1,rowspan=2)
searchBtn.grid(row=9,column=5,columnspan=1,rowspan=2)
resetBtn.grid(row=11,column=5,columnspan=1,rowspan=2)
selectBtn.grid(row=13,column=5,columnspan=1,rowspan=2)

style=ttk.Style()
style.configure("Treeview.Heading",font=('Arial Bold',15))
my_tree['columns']=("id","ime","prezime","datum_rodenja","adresa","grad","kontakt","email","datum_zaposlenja")
my_tree.column('#0',width=0,stretch=NO)

my_tree.column("id",anchor=W,width=170)
my_tree.column("ime",anchor=W,width=170)
my_tree.column("prezime",anchor=W,width=170)
my_tree.column("datum_rodenja",anchor=W,width=170)
my_tree.column("adresa",anchor=W,width=170)
my_tree.column("grad",anchor=W,width=170)
my_tree.column("kontakt",anchor=W,width=170)
my_tree.column("email",anchor=W,width=170)
my_tree.column("datum_zaposlenja",anchor=W,width=170)

my_tree.heading("id",text="id",anchor=W)
my_tree.heading("ime",text="ime",anchor=W)
my_tree.heading("prezime",text="prezime",anchor=W)
my_tree.heading("datum_rodenja",text="datum_rodenja",anchor=W)
my_tree.heading("adresa",text="adresa",anchor=W)
my_tree.heading("grad",text="grad",anchor=W)
my_tree.heading("kontakt",text="kontakt",anchor=W)
my_tree.heading("email",text="email",anchor=W)
my_tree.heading("datum_zaposlenja",text="datum_zaposlenja",anchor=W)

refreshTable()

root.mainloop()