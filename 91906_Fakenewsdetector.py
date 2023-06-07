from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext

# When user agrees to terms, destroy TOS page and make main program available
def destroy_TOS():
    TOS.destroy()
    user_text.configure(state="normal", bg="#E3E3E3")
    output_text.configure(bg="#E3E3E3")

# Make main window
menu = Tk()
menu.title("Fake News Detector")
menu.state('zoomed')
menu.grid_columnconfigure(0, weight=1)
menu.configure(bg="#EAE0D5")

# Create title of page
title_label = Label(menu, text="Fake News Detector", foreground="#22333B", bg="#EAE0D5", font=("Helvetica", 40, "bold"))
title_label.grid(padx=10, pady=10, column=0, row=0)

# Icon
icon = PhotoImage(file="assets/icon.png")
icon = icon.subsample(2)
icon_label = Label(menu, image=icon, bg='#EAE0D5')
icon_label.grid(row=0, column=0, sticky=NW)

# Subheading
file = open(r"text files/intro_text.txt", "r")
userinp_label = Label(menu, text=file.read(), font=("Helvetica", 10))
userinp_label.grid(row=1, column=0, pady=5)

# Create label frame
user_labelframe = LabelFrame(menu, pady=5, padx=5, bg="#5E503F")
user_labelframe.grid(row=2, column=0, columnspan=4, padx=10, pady=10)
user_labelframe.rowconfigure(0, weight=1)
user_labelframe.columnconfigure(0, weight=1)
user_labelframe.columnconfigure((0, 1), weight=1)

# Create label for instructions
input_label = Label(user_labelframe, text="Input:", bg="#5E503F", fg="#FFFFFF", font=("bold"))
input_label.grid(row=0, column=0, padx=5, pady=5)

output_label = Label(user_labelframe, text="Output:", bg="#5E503F", fg="#FFFFFF", font=("bold"))
output_label.grid(row=0, column=1, padx=5, pady=5)

# User input and output
user_text = scrolledtext.ScrolledText(user_labelframe)
user_text.grid(row=1, column=0, sticky=NSEW)

output_text = scrolledtext.ScrolledText(user_labelframe)
output_text.grid(row=1, column=1, sticky=NSEW)

user_text.configure(state="disabled", bg="#898989")
output_text.configure(state="disabled", bg="#898989")

# Enter button for input
enter_button = Button(menu, text="Enter", justify=CENTER)
enter_button.grid(row=4, column=0, sticky=W, padx=20, pady=5)

# Create TOS
TOS = Toplevel(menu)
TOS.title("Terms of Service")
TOS.geometry("500x400")
TOS.transient(menu)  # Set the main window as the master for TOS
TOS.lift()  # Raise TOS window above the main window
TOS.grid_columnconfigure(0, weight=1)

title_tos = Label(TOS, text="Terms of Service", font=("Courier", 20, "bold"))
title_tos.grid(row=0, column=0, sticky=NSEW, padx=10, pady=10)

# Create canvas for TOS
tos_canvas = Canvas(TOS)#, width=tos_width)
tos_canvas.grid(row=1, column=0, sticky=NSEW)

# Create scrollbar for TOS
tos_scrollbar = Scrollbar(TOS, orient=VERTICAL, command=tos_canvas.yview)
tos_scrollbar.grid(row=1, column=1, sticky="ns")
tos_canvas.configure(yscrollcommand=tos_scrollbar.set)

# Make Labelframe inside canvas
tos_labelframe = LabelFrame(tos_canvas)
tos_labelframe.pack(fill="both", expand=True, pady=5,padx=5)

# Open textfile and put in TOS
f = open(r"text files/tos_text.txt", "r")
content_tos = Label(tos_labelframe, text=f.read())
content_tos.pack(pady=5, padx=5)

# Configure canvas to scrollable region
tos_canvas.create_window((0, 0), window=tos_labelframe, anchor="nw")
tos_canvas.configure(scrollregion=tos_canvas.bbox("all"))

# Configure canvas scrolling
tos_labelframe.bind("<Configure>", lambda e: tos_canvas.configure(scrollregion=tos_canvas.bbox("all")))
tos_canvas.bind_all("<MouseWheel>", lambda e: tos_canvas.yview_scroll(int(-1 * (e.delta / 120)), "units"))

# Buttons at end of service
agree_button = ttk.Button(tos_labelframe, text="Agree", command=destroy_TOS)
#agree_button.grid(padx=5, sticky=W, row=2, column=0)
agree_button.pack(side=LEFT, padx=5)

disagree_button = ttk.Button(tos_labelframe, text="Disagree")
#disagree_button.grid(padx=5, row=2, column=1, sticky=E)
disagree_button.pack(side=RIGHT, padx=5)

# Run mainloop
menu.mainloop()