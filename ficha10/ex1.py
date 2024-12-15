import customtkinter
import os
import CTkMessagebox
from tkinter import ttk # treeview
from PIL import Image, ImageTk


def gerirPresenças():
    print("Gerir Presenças")

def consultarPresenças():
    print("Consultar Presenças")

def fecharAplicacao():
    print("Fechar Aplicação")
    app.destroy()
    

#Abrir app
app = customtkinter.CTk()
app.title("My Notepad")

#Resoluçao
appwidth = 1000
appheight = 500

screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

x = (screenWidth/2) - (appwidth/2)
y = (screenHeight/2) - (appheight/2)
app.geometry(f"{appwidth}x{appheight}+{int(x)}+{int(y)}")
app.resizable(False,False)
app.configure(fg_color = "white")

frame1 = customtkinter.CTkFrame(app, width=750, height=500, bg_color="black")
frame1.place(x=50, y=50)



#Buttons
buttonGerir = customtkinter.CTkButton(app, text="Gerir Presenças",text_color="white",
                                      fg_color="blue", width=230, height=120,
                                       image=imgConsultar, command="gerirPresenças",
                                         font=("Helvitica",14 ))
buttonGerir.place(x=20, y=30)

buttonConsultar = customtkinter.CTkButton(app, text="Consultar Presenças",text_color="white",
                                          fg_color="blue", width=230, height=120, image=imgGerir,
                                            command="consultarPresenças", font=("Helvitica",14 ))
buttonConsultar.place(x=20, y=170)

buttonSair = customtkinter.CTkButton(app, text="Sair App", text_color="white",
                                     fg_color="blue", width=230, height=120,
                                       image=imgSair, command="fecharAplicacao",
                                         font=("Helvitica",14 ))
buttonSair.place(x=20, y=310)


#Variaveis para imagens
imgGerir = ImageTk.PhotoImage(file="Ficha10/pasta/images/" + "icoOp1.png")

imgConsultar = ImageTk.PhotoImage(file="Ficha10/pasta/images/" + "icoOp2.png")

imgSair = ImageTk.PhotoImage(file="Ficha10/pasta/images/" + "icoOp4.png")

imgPresencas = ImageTk.PhotoImage(file="Ficha10/pasta/images/" + "presencas.png")

app.mainloop()