import customtkinter

app = customtkinter.CTk()

app.geometry("300x600")
app.title("My Notepad")

frame = ctk.CTkFrame(app, width=300, height=300)
frame.place(x=0, y=0)

widget1 = ctk.CTkButton(frame, text="Guardar Notas")
widget1.pack(pady=10)

widget2 = ctk.CTkLabel(frame, text="Limpar Notas")
widget2.pack(pady=10)

widget3 = ctk.CTkEntry(frame, placeholder_text="Ler Bloco de Notas")
widget3.pack(pady=10)

app.mainloop()