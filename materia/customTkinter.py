# definir componente tabview
tabview = customtkinter.CTkTabview(app, width = 250, height = 500, fg_color = "black")
tabview.pack(padx = 10, pady = 10)

# definir tab1
tab1 = tabview.add("Tab 1")
tab2 = tabview.add("Tab 2")
tab3 = tabview.add("Tab 3")

tabview.set("Tab 1")

#--------------------------------------------



#Frame
frame1 = customtkinter.CTkFrame(app, width=750, height=500, bg_color="black")
frame1.place(x=250, y=0)
#-------------------#