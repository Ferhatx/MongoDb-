# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import messagebox
import pymongo

def insert_user():
    con = pymongo.MongoClient('localhost', 27017) #Veri Tabanı bağlantısını için  ip ve port ayarları
    mydb = con["teleskop"] #Kullanılacak veri tabananın adı
    mytbl = mydb["user"] # Kullanılacak Colection
    newuser = {"name": user_text.get(), "surname": surname_text.get(), "email": email_text.get(),"username": username_text.get(), "pass": pass_text.get()}
    insrt = mytbl.insert_one(newuser)
    if (insrt):
        messagebox.showinfo("New User", "Başarıyla Eklendi")
    else:
        messagebox.showerror("Hata", "Bilgileriniz Yanlış")
    text_delete()



def text_delete():
    user_text.delete("0", "end")
    surname_text.delete("0", "end")
    email_text.delete("0", "end")
    username_text.delete("0", "end")
    pass_text.delete("0", "end")
ekran = tk.Tk()

ekran.title("New User Panel")
ekran.geometry("300x200")
user_label = tk.Label(ekran, text="Adınız :").grid(row=1, )
surname_label = tk.Label(ekran, text="Soyadınız :").grid(row=2)
email_label = tk.Label(ekran, text="E-posta :").grid(row=3)
username_label = tk.Label(ekran, text="Kullanıcı Adınız :").grid(row=4)
pass_label = tk.Label(ekran, text="Şifreniz :").grid(row=5)

user_text = tk.Entry(ekran)
surname_text = tk.Entry(ekran)
email_text = tk.Entry(ekran)
username_text = tk.Entry(ekran)
pass_text = tk.Entry(ekran)

user_text.grid(row=1, column=1)
surname_text.grid(row=2, column=1)
email_text.grid(row=3, column=1)
username_text.grid(row=4, column=1)
pass_text.grid(row=5, column=1)

tk.Button(ekran, text="Giriş", command=insert_user).grid(row=6, column=1, sticky=tk.W, pady=4)

ekran.mainloop()