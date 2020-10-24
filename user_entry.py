2import tkinter as tk
from tkinter import messagebox
import pymongo

ekran=tk.Tk()

ekran.title("User Entry")
ekran.geometry("220x100")

def kontrol():
    con = pymongo.MongoClient('localhost', 27017)  # Veri Tabanı bağlantısını için  ip ve port ayarları
    mydb = con["teleskop"]  # Kullanılacak veri tabananın adı
    mytbl = mydb["user"]  # Kullanılacak Colection
    
    if(mytbl.count_documents({"username":user_text.get(),"pass":sifre_text.get()})):
        messagebox.showinfo("Tebrikler","Hoş Geldiniz")
    else:
        messagebox.showerror("Hata","Bilgileriniz Yanlış")
    



user_label=tk.Label(ekran,text="Kullanıcı Adı :").grid(row=0)
user_label=tk.Label(ekran,text="Şifre :").grid(row=1)

user_text=tk.Entry(ekran)
sifre_text=tk.Entry(ekran)

user_text.grid(row=0,column=1)
sifre_text.grid(row=1,column=1)

tk.Button(ekran,text="Giriş",command=kontrol).grid(row=3,column=1,sticky=tk.W,pady=4)
ekran.mainloop()