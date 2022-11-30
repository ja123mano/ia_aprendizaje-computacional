from tkinter import *
 
# creating the tkinter window
main_window = Tk(className='Lector de Biomas')
main_window.configure(bg='white')
main_window.geometry("280x110")
main_window.resizable(width=False, height=False)
 
bioma = StringVar()

def start_reader():
    start_btn.pack_forget()
    stop_btn.pack()
    bioma.set("Agua")

def stop_reader():
    start_btn.pack()
    stop_btn.pack_forget()
    bioma.set("Cultivo")
# create a button widget and attached  
# with counter function  
start_btn = Button(main_window,
                   text = "Start",
                   command = start_reader,
                   padx = 30,
                   pady = 5,
                   bg='green',
                   fg='white',
                   font=('Helvetica bold',10))

stop_btn = Button(main_window,
                   text = "Stop",
                   command = stop_reader,
                   padx = 30,
                   pady = 5,
                   bg='red',
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

bioma.set("Ciudad")

my_label.pack()
label_bioma.pack()
start_btn.pack()

main_window.mainloop()