import customtkinter
import os
import CTkMessagebox
from tkinter import ttk # treeview
from PIL import Image, ImageTk

  #Funçoes



def gerirPresenças():
  frameGerir = customtkinter.CTkFrame(app, width=750, height=500, fg_color="grey")
  frameGerir.place(x=250)

  #caixas de texto
  entryNum = customtkinter.CTkEntry(app, placeholder_text="Número de estudante", width=150);
  entryNum.place(x=450, y=60)
  #entryType = customtkinter.CTkEntry(app, placeholder_text="Tipo de movimento", width=150);
  #entryType.place(x=320, y=120)
  #entry1 = customtkinter.CTkEntry(app, placeholder_text="Histórico de movimento", width=150);
  #entry1.place(x=750, y=40)
  
  #Labels
  labelNum = customtkinter.CTkLabel(app, text="Número de estudante:", font= ("Arial", 12),
                                     fg_color="transparent", text_color="white");
  labelNum.place(x=320, y=60)
  label1 = customtkinter.CTkLabel(app, text="Histórico de movimento:", font= ("Arial", 12),
                                  fg_color="transparent", text_color="white");
  label1.place(x=750, y=40)
  label2 = customtkinter.CTkLabel(app, text="Tipo de movimento:", font= ("Arial", 12),
                                  fg_color="transparent", text_color="white");
  label2.place(x=320, y=120)



  frameTree = customtkinter.CTkFrame(frameGerir, width = 320, height = 300)
  frameTree.place(x=400, y=70)

  # TreeView para consulta de movimentos
  treeConsulta = ttk.Treeview(frameTree, height = 16, selectmode = "browse", columns = ("Número", "Data", "Hora", "Movimento"), show = "headings")

  treeConsulta.column("Número", width = 80, anchor="c")
  treeConsulta.column("Data", width = 80, anchor="c")            # C - center
  treeConsulta.column("Hora", width = 80, anchor="c")            # E - direita
  treeConsulta.column("Movimento", width = 80, anchor="c")       # W - esquerda

  treeConsulta.heading("Número", text = "Número")
  treeConsulta.heading("Data", text = "Data")
  treeConsulta.heading("Hora", text = "Hora")
  treeConsulta.heading("Movimento", text = "Movimento")
  treeConsulta.pack()


  #Button
  buttonLer = customtkinter.CTkButton(frameGerir, text="Ler Ficheiro",
                                       text_color="white", bg_color="blue",
                                         width=250, height=50)
  buttonLer.place(x=450, y=400)

  buttonRegistar = customtkinter.CTkButton(frameGerir, text="Registar Movimento em Ficheiro",
                                            fg_color="black", text_color="blue",
                                              width=250, height=150)
  buttonRegistar.place(x=75, y=250)


  #CheckBox
  checkVar1 = customtkinter.StringVar(value="on")
  checkVar2 = customtkinter.StringVar(value="off")

  checkboxEntrada = customtkinter.CTkCheckBox(app, text="Entrada", variable=checkVar1, onvalue="on",
                                               offvalue="off", bg_color="black")
  checkboxSaida = customtkinter.CTkCheckBox(app, text="Saida", variable=checkVar2, onvalue="on",
                                             offvalue="off", bg_color="black")

  checkboxEntrada.place(x=500, y=120)
  checkboxSaida.place(x=500, y=170)






def consultarPresenças():
    
    # Frame
    frameConsultar = customtkinter.CTkFrame(app, width=750, height=500, fg_color="black")
    frameConsultar.place(x=250)

    frameMovimento = customtkinter.CTkFrame(frameConsultar, width=220, height=100, fg_color="grey")
    frameMovimento.place(x=20)

    frameNumero = customtkinter.CTkFrame(frameConsultar, width=220, height=100, fg_color="grey")
    frameNumero.place(x=250)

    # Button
    buttonMovimento = customtkinter.CTkButton(frameConsultar, text="", image=imgLupa, width=220, height=100)
    buttonMovimento.place(x=480)

    # CheckBox
    checkVar1 = customtkinter.StringVar(value="on")
    checkVar2 = customtkinter.StringVar(value="off")

    checkboxEntrada = customtkinter.CTkCheckBox(frameConsultar, text="Entrada", variable=checkVar1, onvalue="on", offvalue="off", bg_color="grey")
    checkboxSaida = customtkinter.CTkCheckBox(frameConsultar, text="Saida", variable=checkVar2, onvalue="on", offvalue="off", bg_color="grey")

    checkboxEntrada.place(x=40, y=40)
    checkboxSaida.place(x=40, y=70)

    # Label
    labelMovimento = customtkinter.CTkLabel(frameConsultar, text="Tipo do Movimento", fg_color="grey", bg_color="grey", text_color="white", font=("Helvitica",14))
    labelMovimento.place(x=40, y=10)

    labelNumero = customtkinter.CTkLabel(frameConsultar, text="Numero", fg_color="grey", text_color="white", font=("Helvitica",14))
    labelNumero.place(x=330, y=10)

    # EntryBox
    entryNumero = customtkinter.CTkEntry(frameConsultar, fg_color="white", width=150, text_color="black")
    entryNumero.place(x=280, y=50)

    # Treeview
    frameTree = customtkinter.CTkFrame(frameConsultar, width = 690, height = 500)
    frameTree.place(x=20, y=170)

    # TreeView para consulta de movimentos
    tree = ttk.Treeview(frameTree, height = 16, selectmode = "browse", columns = ("Número", "Data", "Hora", "Movimento"), show = "headings")

    tree.column("Número", width = 160,  anchor="c")
    tree.column("Data", width = 160,     anchor="c")        # C- center
    tree.column("Hora", width = 160,     anchor="c")        # E - direita
    tree.column("Movimento", width = 200, anchor="c")       # W- esquerda
    tree.heading("Número", text = "Número")
    tree.heading("Data", text = "Data")
    tree.heading("Hora", text = "Hora")
    tree.heading("Movimento", text = "Movimento")
    tree.place(x= 5, y=5)

    # Scrollbar Vertical
    verscrlbar = ttk.Scrollbar(frameTree, orient ="vertical", command = tree.yview)
    # CallinPlace da Scrollbar
    verscrlbar.place(x=735, y=16, height=330)
    # Adicionar scrollbar à  treeview
    tree.configure(yscrollcommand = verscrlbar.set)


def lerPresenças():
  caminho="AED git/Ficha10/"
  f = open(caminho+"presenças.txt", "r")
  limpar=textboxNotas.delete("0.0", "end")
  lines = f.readlines()
  f.close()
  for line in lines: 
      textboxNotas.insert("end", line)


def fecharAplicacao():
  #Formatar messagebox
    mensagem = CTkMessagebox.CTkMessagebox(title="Sair da Aplicação?",
                                 message="Deseja sair da aplicação?",
                                   option_1="Sim", option_2="Não",
                                     option_3="Cancelar")
    resposta = mensagem.get()
    if resposta == "Sim":
        app.destroy()
#-------------------#

#Abrir app
app = customtkinter.CTk()
app.title("My Notepad")
#-------------------#

#Resoluçao
appwidth = 1000
appheight = 500

screenWidth = app.winfo_screenwidth()
screenHeight = app.winfo_screenheight()

x = (screenWidth/2) - (appwidth/2)
y = (screenHeight/2) - (appheight/2)
app.geometry(f"{appwidth}x{appheight}+{int(x)}+{int(y)}")
app.resizable(False,False)
app.configure(fg_color = "black")
#-------------------#




#Variaveis para imagens
imgGerir = ImageTk.PhotoImage(file="images/" + "icoOp1.png")

imgConsultar = ImageTk.PhotoImage(file="images/" + "icoOp2.png")

imgSair = ImageTk.PhotoImage(file="images/" + "icoOp4.png")

imgPresencas = ImageTk.PhotoImage(file="images/" + "presencas.png")

imgLupa = ImageTk.PhotoImage(file="images/" + "lupa.png")

#-------------------#

#Labels
labelPresencas = customtkinter.CTkLabel(app, text="" , width=750, height=500,
                                        image=imgPresencas)
labelPresencas.place(x=250, y=0)
#-------------------#








#Buttons
buttonGerir = customtkinter.CTkButton(app, text="Gerir Presenças",text_color="white",
                                      fg_color="blue", width=230, height=120,
                                       image=imgConsultar, command=gerirPresenças,
                                         font=("Helvitica",14 ))
buttonGerir.place(x=20, y=30)

buttonConsultar = customtkinter.CTkButton(app, text="Consultar Presenças",text_color="white",
                                          fg_color="blue", width=230, height=120, image=imgGerir,
                                            command=consultarPresenças, font=("Helvitica",14 ))
buttonConsultar.place(x=20, y=170)

buttonSair = customtkinter.CTkButton(app, text="Sair App", text_color="white",
                                     fg_color="blue", width=230, height=120,
                                       image=imgSair, command=fecharAplicacao,
                                         font=("Helvitica",14 ))
buttonSair.place(x=20, y=310)
#-------------------#


app.mainloop()