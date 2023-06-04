import os
import pickle
import time
from tkinter import *
from random import randrange
from test import get_prediction
 
with open(os.getcwd() + "\\Integración IA\\MLPClassifier.clf", "rb") as file:
    clf = pickle.load(file)

# creating the tkinter window
main_window = Tk(className='Lector de Biomas')
main_window.configure(bg='white')
main_window.geometry("280x110")
main_window.resizable(width=False, height=False)
 
bioma = StringVar()

def start_reader():
    bioma.set("...")
    main_window.state(newstate='iconic')
    time.sleep(0.2)
    set_bioma(get_prediction(clf))
    main_window.state(newstate='normal')

def set_bioma(prediction):
    bioma.set(prediction)


    #bioma.set("Cultivo")
# create a button widget and attached  
# with counter function  
read_btn = Button(main_window,
                   text = "Read",
                   command = start_reader,
                   padx = 30,
                   pady = 5,
                   bg='green',
                   fg='white',
                   font=('Helvetica bold',10)) 
 
# create a Label widget
my_label = Label(main_window,
                 text = "Bioma Detectado:",
                 font=('Helvetica', 10),
                 bg='white')

label_bioma = Label(main_window,
                    textvariable = bioma,
                    font=('Helvetica bold', 25),
                    bg='white')

bioma.set("...")
my_label.pack()
label_bioma.pack()
read_btn.pack()

main_window.mainloop()