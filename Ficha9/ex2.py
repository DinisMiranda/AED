import customtkinter
import os

def calc():
    entryAlturaValue = entryAltura.get()
    radioVarValue = radioVar.get()

    print(entryAlturaValue)
    print(radioVarValue)

    PesoIdial = (int(entryAlturaValue )- 100) - (int(entryAlturaValue) - 150) / int(radioVarValue)
    print(PesoIdial)
    labelPesoIdealValue.configure(text=str(PesoIdial))

#Abrir app
app = customtkinter.CTk()
app.title("My Notepad")

#Resoluçao
appwidth = 370
appheight = 430

screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

x = (screenWidth/2) - (appwidth/2)
y = (screenHeight/2) - (appheight/2)
app.geometry(f"{appwidth}x{appheight}+{int(x)}+{int(y)}")
app.resizable(False,False)
app.configure(fg_color = "white")


#Labels
labelAlturaEmCm = customtkinter.CTkLabel(app, text="Altura (cm):", font= ("Arial", 12), fg_color="transparent", text_color="blue");
labelAlturaEmCm.place(x=20, y=40)         

labelGenero = customtkinter.CTkLabel(app, text="Género:", font= ("Arial", 12), fg_color="transparent", text_color="blue");
labelGenero.place(x=20, y=80) 

labelPesoIdeal = customtkinter.CTkLabel(app, text="Peso Ideal:", font= ("Arial", 20), fg_color="transparent", text_color="red");
labelPesoIdeal.place(x=135, y=300)

labelPesoIdealValue = customtkinter.CTkLabel(app, text="", font= ("Arial", 20), fg_color="transparent", text_color="red");
labelPesoIdealValue.place(x=135, y=330)

#caixas de texto
entryAltura = customtkinter.CTkEntry(app, placeholder_text="Insira a sua altura", width=150);
entryAltura.place(x=120, y=40)

#radio buttons
radioVar = customtkinter.StringVar(value="Masculino")
radiobutton1 = customtkinter.CTkRadioButton(app,text="Masculino", 
                                            variable=radioVar, value=4)
radiobutton1.place(x=120, y=80)

radiobutton2 = customtkinter.CTkRadioButton(app,text="Feminino", 
                                            variable=radioVar, value=2)
radiobutton2.place(x=120, y=120)

#BUTTONS
btnCalcular = customtkinter.CTkButton(app, text="Calcular",command=calc, width=330, height=80, bg_color="blue", fg_color="black")
btnCalcular.place(x=20, y=160)

app.mainloop()