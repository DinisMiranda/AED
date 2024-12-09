import customtkinter
import os


#Abrir app
app = customtkinter.CTk()
app.title("My Notepad")

#Resoluçao
appwidth = 300
appheight = 600

screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

x = (screenWidth/2) - (appwidth/2)
y = (screenHeight/2) - (appheight/2)
app.geometry(f"{appwidth}x{appheight}+{int(x)}+{int(y)}")
app.resizable(False,False)
app.configure(fg_color = "white")

#Label
labelPaís = customtkinter.CTkLabel(app, text="Indique as suas notas.", text_color="blue", font=("Helvetica",14))
labelPaís.place(x=80, y=5)

#Textbox
textboxNotas = customtkinter.CTkTextbox(app, width=250, height=300, border_color="grey")
textboxNotas.place(x=30, y=30)

#Buttons
buttonGuardar = customtkinter.CTkButton(app, width=250, height=50, bg_color="black", text="Guardar", text_color="blue", command=guardarTexto)
buttonGuardar.place(x=30, y=350)

buttonLimpar = customtkinter.CTkButton(app, width=250, height=50, bg_color="black", text="Limpar", text_color="red",  command=limparTexto)
buttonLimpar.place(x=30, y=420)

buttonLer = customtkinter.CTkButton(app, width=250, height=50, bg_color="black", text="Ler bloco de notas", text_color="blue",  command=lerTexto)
buttonLer.place(x=30, y=490)

app.mainloop()