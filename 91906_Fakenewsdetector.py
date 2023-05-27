from tkinter import *
from tkinter import ttk
from tkinter import Tk

def destroy_TOS():
    TOS.destroy()

menu = Tk()
#menu.geometry("500x250")
menu.title("Fake News Detector")
menu.state('zoomed')
#menu.grid_rowconfigure(0, weight=1)
menu.grid_columnconfigure(0, weight=1)

#Create title of page
title_label = Label(menu, bg="blue", text="Fake News Detector", foreground="red", font=("Courier", 40, "bold"))
title_label.grid()#(row=0,column=2)

userinp_label = Label(menu, text="Hi, put your text here")
userinp_label.grid(row=1, column=0)

#Create TOS
TOS = Toplevel(menu)
TOS.geometry("500x200")
TOS.title("Terms of Service")
title_tos = Label(TOS, text="Terms of Service", font=("Courier",20, "bold"))
title_tos.grid(row=0,column=0)

#open textfile and put in TOS
f = open(r"tos_text.txt", "r")
content_tos = Label(TOS, text=f.read())
content_tos.grid(row=1, column=0)

#Create vertical scrollbar
scrollbar_tos = ttk.Scrollbar(TOS, orient='vertical')#, command=f.read().yview)
scrollbar_tos.grid(row=1, column=1, sticky=NS)

#scroll_bar = Scrollbar(TOS)    
#scroll_bar.grid(row=1,column=1,sticky=NS)
#mylist = Listbox(TOS, yscrollcommand=scroll_bar.set)
#mylist.index(END, f.read())
#for line in range(1, 26):
 #   mylist.insert(END, "Geeks " + str(line))
#mylist.grid(row=1,column=0)
#scroll_bar.config(command=mylist.yview)

#v = Scrollbar(TOS, orient="vertical")
#v.grid(row=1, column=1, sticky=NS)
#for i in range(10):
#    content_tos.insert(END)
#v.config(command=content_tos.yview)

agree_button = Button(TOS, text="Agree", command=destroy_TOS)
agree_button.grid(row=2, column=0, sticky=W)
#run mainloop
menu.mainloop()