from textblob import TextBlob
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext

def sentimentFAKE():
    """Hard coded sentiment anaylsis without user input (this is temporary, to ensure code works) 
    """
    sampletext = "Banana's are yellow fruits with black seeds in the middle. While some like it, the taste is often too mushy to enjoy. "
    analysis = TextBlob(sampletext).sentiment
    print(analysis)

userinput = input()
analysis = TextBlob(userinput).sentiment
print(analysis)

'''
#create page
outpage = Tk()
outpage.title("Sentiment analysis")
outpage.geometry("500x400")

title_sentiment = Label(outpage, text="Sentiment Analysis", font=("Helvetica", 40, "bold"))
title_sentiment.grid(sticky=NSEW, row=0)

polarity = Label(outpage, text="Polarity: ")
polarity.grid(sticky=W, row=1)

subjectivity = Label(outpage, text="Subjectivity: ")
subjectivity.grid(sticky=W, row=2)

#run mainloop
outpage.mainloop()'''