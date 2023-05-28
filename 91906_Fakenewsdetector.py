from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter import scrolledtext

#When user agrees to terms, destroy TOS page and make main program available
def destroy_TOS():
    TOS.destroy()
    user_text.configure(state="normal", bg="#E3E3E3")
    output_text.configure(bg="#E3E3E3")

#make main window
menu = Tk()
menu.title("Fake News Detector")
menu.state('zoomed')
menu.grid_columnconfigure(0, weight=1)
menu.configure(bg="#EAE0D5")

#Create title of page
title_label = Label(menu, text="Fake News Detector", foreground="#22333B",bg="#EAE0D5", font=("Helvetica", 40, "bold"))
title_label.grid(padx=10, pady=10, column=0, row=0)

#icon 
icon = PhotoImage(file="assets\icon.png")
icon = icon.subsample(2)
icon_label = Label(menu, image=icon, bg='#EAE0D5')
icon_label.grid(row=0, column=0, sticky=NW)

#subheading
file = open(r"text files\intro_text.txt", "r")
userinp_label = Label(menu, text=file.read(), font=("Helvetica", 10))
userinp_label.grid(row=1, column=0, pady=5)

#Create label frame 
user_labelframe = LabelFrame(menu,pady=5, padx=5, bg="#5E503F")
user_labelframe.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
user_labelframe.rowconfigure(0, weight=1)
user_labelframe.columnconfigure(0, weight=1)
user_labelframe.columnconfigure((0,1),weight=1)

#Create label for instructions
input_label = Label(user_labelframe, text="Input:",bg="#5E503F",fg="#FFFFFF", font=("bold"))
input_label.grid(row=0, column=0, padx=5, pady=5)

output_label = Label(user_labelframe, text="Output:",bg="#5E503F",fg="#FFFFFF", font=("bold"))
output_label.grid(row=0, column=1, padx=5, pady=5)

#user input and output
user_text = scrolledtext.ScrolledText(user_labelframe)
user_text.grid(row=1,column=0,sticky=W)

output_text = scrolledtext.ScrolledText(user_labelframe)
output_text.grid(row=1,column=1,sticky=E)

user_text.configure(state="disabled", bg="#898989")
output_text.configure(state="disabled", bg="#898989")

#Create TOS
TOS = Toplevel(menu)
TOS.geometry("500x200")
TOS.title("Terms of Service")
title_tos = Label(TOS, text="Terms of Service", font=("Courier",20, "bold"))
title_tos.grid(row=0,column=0)

#make Labelframe
tos_labelframe = LabelFrame(TOS, pady=5, padx=5)
tos_labelframe.grid(row=1, column=0)

#open textfile and put in TOS
f = open(r"text files\tos_text.txt", "r")
content_tos = Label(tos_labelframe, text=f.read())
content_tos.grid(row=0, column=0, pady=5, padx=5)

#Make scrollbar for TOS

#Buttons at end of service
agree_button = ttk.Button(tos_labelframe, text="Agree", command=destroy_TOS)
agree_button.grid(row=1, column=0, sticky=W)

disagree_button = Button(tos_labelframe, text="Disagree")
disagree_button.place(x=380, y=300)


from tkinter import *
from tkinter import ttk
from tkinter import Tk
from tkinter import scrolledtext

#When user agrees to terms, destroy TOS page and make main program available
def destroy_TOS():
    TOS.destroy()
    user_text.configure(state="normal", bg="#E3E3E3")
    output_text.configure(bg="#E3E3E3")

#make main window
menu = Tk()
menu.title("Fake News Detector")
menu.state('zoomed')
menu.grid_columnconfigure(0, weight=1)
menu.configure(bg="#EAE0D5")

#Create title of page
title_label = Label(menu, text="Fake News Detector", foreground="#22333B",bg="#EAE0D5", font=("Helvetica", 40, "bold"))
title_label.grid(padx=10, pady=10, column=0, row=0)

#icon 
icon = PhotoImage(file="assets\icon.png")
icon = icon.subsample(2)
icon_label = Label(menu, image=icon, bg='#EAE0D5')
icon_label.grid(row=0, column=0, sticky=NW)

#subheading
file = open(r"text files\intro_text.txt", "r")
userinp_label = Label(menu, text=file.read(), font=("Helvetica", 10))
userinp_label.grid(row=1, column=0, pady=5)

#Create label frame 
user_labelframe = LabelFrame(menu,pady=5, padx=5, bg="#5E503F")
user_labelframe.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
user_labelframe.rowconfigure(0, weight=1)
user_labelframe.columnconfigure(0, weight=1)
user_labelframe.columnconfigure((0,1),weight=1)

#Create label for instructions
input_label = Label(user_labelframe, text="Input:",bg="#5E503F",fg="#FFFFFF", font=("bold"))
input_label.grid(row=0, column=0, padx=5, pady=5)

output_label = Label(user_labelframe, text="Output:",bg="#5E503F",fg="#FFFFFF", font=("bold"))
output_label.grid(row=0, column=1, padx=5, pady=5)

#user input and output
user_text = scrolledtext.ScrolledText(user_labelframe)
user_text.grid(row=1,column=0,sticky=W)

output_text = scrolledtext.ScrolledText(user_labelframe)
output_text.grid(row=1,column=1,sticky=E)

user_text.configure(state="disabled", bg="#898989")
output_text.configure(state="disabled", bg="#898989")

#Create TOS
TOS = Toplevel(menu)
TOS.geometry("500x200")
TOS.title("Terms of Service")
title_tos = Label(TOS, text="Terms of Service", font=("Courier",20, "bold"))
title_tos.grid(row=0,column=0)

#make Labelframe
tos_labelframe = LabelFrame(TOS, pady=5, padx=5)
tos_labelframe.grid(row=1, column=0)

#open textfile and put in TOS
f = open(r"text files\tos_text.txt", "r")
content_tos = Label(tos_labelframe, text=f.read())
content_tos.grid(row=0, column=0, pady=5, padx=5)

#Make scrollbar for TOS

#Buttons at end of service
agree_button = Button(tos_labelframe, text="Agree", command=destroy_TOS)
agree_button.grid(row=1, column=0, sticky=W)

disagree_button = Button(tos_labelframe, text="Disagree")
disagree_button.grid(row=1, column=1, sticky=E)

#run mainloop
menu.mainloop()

#run mainloop
menu.mainloop()