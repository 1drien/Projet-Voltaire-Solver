import difflib
from tkinter import *
import os
import sys

data = [] #global

f_CGU =  open( ".\CGU.txt" ,"r", encoding="utf-8")
data_CGU = f_CGU.read()
data_CGU = data_CGU[data_CGU.index("[Signer avec votre nom]:"):data_CGU.index("[Signer avec votre nom]:")+99]
print(data_CGU)
if data_CGU == "[Signer avec votre nom]:":
    CGU = Tk()
    CGU.title("VoltaireTaMere 1.0.0")
    CGU.geometry('180x45')
    CGU.resizable(False, False)
    CGU.iconphoto(True,PhotoImage(file = "VoltaireTaMereIcoPNG.png"))
    CGU.configure(bg='#23272A')
    Label (CGU,
                text="Vous n'avez pas lu et \napprouvé les CGU.",
                bg="#23272A",
                fg="#ffffff",
                font = 20).pack()
    CGU.mainloop()
    exit()

def data_Extract (PATH):
    print(PATH)
    Fichier_ERR = open( PATH ,"r", encoding="utf-8") 
    data_Brut = Fichier_ERR.read()+"€"
    data_Brut = data_Brut[data_Brut.index("[\"java.util.ArrayList"):data_Brut.index("€")]
    data_Clear = []
    i = 0
    extract = "a"
    while extract != "":
        extract = data_Brut[ data_Brut.find("\"",i): data_Brut.find("\"", i+data_Brut.find("\"")+1) ]
        if "\\x3C" in extract:
            data_Clear += [extract.replace("\"","").replace("\\x3CB\\x3E", "< ").replace("\\x3C/B\\x3E", " >").replace("\\x27","'").replace("\\xA0"," ").replace("\\x26#x2011;","-")]

        i += len(extract)

    Fichier_ERR.close()
    return data_Clear

def test_Str():
    global data

    if data == []:
        boiteOutPut.delete(1.0,"end")
        boiteOutPut.insert(1.0,"ERREUR Aucun fichier chargé","err")
        return 0
    
    print(boitePhrase.get(1.0,END))
    Close_Match = difflib.get_close_matches(boitePhrase.get(1.0,END), data)
    print(Close_Match)
    if Close_Match != []:
        for i in range(len(Close_Match)):
            if "<" in Close_Match[i]:
                boiteOutPut.delete(1.0,"end")
                boiteOutPut.insert(1.0,Close_Match[i],"err")
                return 0

    boiteOutPut.delete(1.0,"end")
    boiteOutPut.insert(1.0,"il n'y a pas de faute(s)","noerr")
    return 0

def auto_Work():
    if boitePhrase.get(1.0,"end").replace("\n","") != root.clipboard_get().replace("\n","") and "//OK" not in root.clipboard_get() :
        boitePhrase.delete(1.0,"end")
        boitePhrase.insert(1.0,root.clipboard_get().replace("\n",""))
        test_Str()
    root.after(500,auto_Work)

def load_Fill():
    global data
    data = []
    boiteOutPut.delete(1.0,"end")

    if extra_PATH.get() != "":
        data = data_Extract(extra_PATH.get())
    else:
        if ListBModule.curselection() == ():
            ListBModule.selection_set(0)

        if len(modules.get()) == 135:
            data = data_Extract(".\Modules\\Supérieur\\Module" + str(ListBModule.curselection()[0] + 1 ) + ".txt")
        else:
            data = data_Extract(".\Modules\\Excellence\\Module" + str(ListBModule.curselection()[0] + 1 ) + ".txt")

    if data != []:
        boiteOutPut.delete(1.0,"end")
        boiteOutPut.insert(1.0,"Fichier correctement chargé :D","noerr")

root = Tk()
root.title("VoltaireTaMere 1.1.1")
root.geometry('407x445')
root.resizable(False, False)
root.iconphoto(True,PhotoImage(file = "VoltaireTaMereIcoPNG.png"))
root.configure(bg='#23272A')

modules = StringVar()
modules_Sup = "Module\ 1 Module\ 2 Module\ 3 Module\ 4 Module\ 5 Module\ 6 Module\ 7 Module\ 8 Module\ 9 Module\ 10 Test\ Blanc" #2-8
modules_Exl = "Module\ 1 Module\ 2 Module\ 3 Module\ 4 Module\ 5 Module\ 6 Module\ 7 Module\ 8 Module\ 9 Module\ 10 Module\ 11 Module\ 12 Verbes\ Pronominaux\ II" #Verbes\ Pro\ I Verbes\ Pro\ II

extra_PATH = StringVar()
root.clipboard_append("")

#----------------------------------------------------------------
#ROOT MAIN LOOP

Label (root,
            text="Programme:",
            bg="#23272A",
            fg="#ffffff",
            font=15).place(x=10, y=10)

Label (root,
            text="Niveau:",
            bg="#23272A",
            fg="#ffffff",
            font=10).place(x=240, y=10)

Radiobutton (root,indicatoron=0,
                variable = modules,
                text = " Supérieur ",
                value = modules_Sup,
                fg = "#ffffff",
                bg = "#34393B",
                bd=0,
                selectcolor = "#8eb912",
                font=10).place(x=15,y=40)

Radiobutton (root,indicatoron=0,
                variable = modules,
                text = "Excellence",
                value = modules_Exl,
                fg = "#ffffff" ,
                bg = "#34393B",
                bd=0,
                selectcolor = "#8eb912",
                font=10).place(x=15,y=80)

ListBModule = Listbox(root,exportselection=0,
                listvariable = modules, 
                selectmode = "single",
                activestyle = "none",
                height = 8,
                width = 25,
                bd = 0,
                bg = "#2C2F33",
                fg = "#ffffff",
                selectbackground = "#8eb912")
ListBModule.place(x=240, y=40)

Label (root,
            text="Customs Module PATH:",
            bg="#23272A",
            fg="#ffffff",
            font=10).place(x=10, y=120)

Entry (root,
            textvariable = extra_PATH,
            bg="#23272A",
            fg="#ffffff",
            width = 23,
            font=10).place(x=15, y=150)

Button (root,
            text="Charger le fichier",
            command= load_Fill,
            fg="#ffffff",
            bg="#8eb912",
            font=15,
            bd=0,).place(x=15, y=190)

Label (root,
            text="Coller la phrase:",
            bg="#23272A",
            fg="#ffffff",
            font=10).place(x=10, y=230)

boitePhrase = Text (root,           
                height = 5,
                width=48,
                bg="#2C2F33",
                fg="#ffffff",
                bd=0)
boitePhrase.place(x=10, y=260)

boiteOutPut = Text (root,
                height = 5,
                width=48,
                bg="#23272A",
                fg="#ffffff",
                bd=0)
boiteOutPut.place(x=10, y=350)

boiteOutPut.tag_config("noerr",foreground = "#8eb912")
boiteOutPut.tag_config("err",foreground = "#DC143C")
root.after(500,auto_Work)

root.mainloop()