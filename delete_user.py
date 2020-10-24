import tkinter as tk
from tkinter import *
import pymongo

ekran=tk.Tk()

ekran.title("DELETE USER")
ekran.geometry("600x180")

objectid_label=tk.Label(ekran,text="Object_id",relief=RIDGE).grid(row=0)
name_label=tk.Label(ekran,text="Adı",relief=RIDGE).grid(row=0,column=1)
surname_label=tk.Label(ekran,text="Soyadı",relief=RIDGE).grid(row=0,column=2)
email_label=tk.Label(ekran,text="Email",relief=RIDGE).grid(row=0,column=3)
username_label=tk.Label(ekran,text="User Name",relief=RIDGE).grid(row=0,column=4)
pass_label=tk.Label(ekran,text="Parola",relief=RIDGE).grid(row=0,column=5)
def kullanicilari_getir():
    con = pymongo.MongoClient('localhost', 27017)  # Veri Tabanı bağlantısını için  ip ve port ayarları
    mydb = con["teleskop"]  # Kullanılacak veri tabananın adı
    mytbl = mydb["user"]  # Kullanılacak Colection

    getir=mytbl.find()
    getir2=mytbl.count()
    print(getir2)
    var = IntVar()

    for i in range(1,getir2):
        j=0
        for x in getir:
            print(x['name'])
            print(x['surname'])
            print(x['email'])
            print(x['pass'])

            Radiobutton(ekran, text=x['_id'],variable=var, value=i, relief=RIDGE).grid(row=i, column=j)
            j=j+1
            tk.Label(ekran, text=x['name'], relief=RIDGE).grid(row=i, column=j)
            j=j+1
            tk.Label(ekran, text=x['surname'], relief=RIDGE).grid(row=i, column=j)
            j = j + 1
            tk.Label(ekran, text=x['email'], relief=RIDGE).grid(row=i, column=j)
            j = j + 1
            tk.Label(ekran, text=x['username'], relief=RIDGE).grid(row=i, column=j)
            j = j + 1
            tk.Label(ekran, text=x['pass'], relief=RIDGE).grid(row=i, column=j)
            i=i+1
            j=0

def sil():
	con = pymongo.MongoClient('localhost', 27017)  # Veri Tabanı bağlantısını için  ip ve port ayarları
	mydb = con["teleskop"]  # Kullanılacak veri tabananın adı
	mytbl = mydb["user"]  # Kullanılacak Colection
	tst=kullanicilari_getir()
	mytbl.delete_one({"_id":tst.var.get()})
	
    



kullanicilari_getir()
tk.Button(ekran,text="Kullanıcı Sil",command=sil).grid(row=6,column=1,sticky=tk.W,pady=4)
ekran.mainloop()
