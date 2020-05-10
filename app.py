from tkinter import *
import random

root = Tk()
root.geometry(("250x200"))
#root.resizable(0,0)
root.title("Password Generator")

holder = ''
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()?.-'
under = '_'

undervar = IntVar()
lettervar = IntVar()
numvar = IntVar()
symvar = IntVar()

password = ''

def generate(length, letter, numerator, symbls, unders):
    global password, holder, letters, numbers, symbols, under, pwrd
    plholder = lengbtn.get()
    length = int(plholder)
    counter = 0
    
    if unders == 1:
        holder += under
    if letter == 1:
        holder += letters
    if numerator == 1:
        holder += numbers
    if symbls == 1:
        holder += symbols
    
    for x in range(length):
        counter + 1
        password = password + random.choice(holder)
        print(password)
        pwrd['text']=password

    print("done")
    password = ''
    holder = ''

        

lengq = Label(root, text="Length:")
lengq.pack()
lengbtn = Entry(root)
lengbtn.pack()

letterbtn = Checkbutton(root, text="Letters?", variable=lettervar)
letterbtn.pack()

symbolbtn = Checkbutton(root, text="Symbols?", variable=symvar)
symbolbtn.pack()

numberbtn = Checkbutton(root, text="Numbers?", variable=numvar)
numberbtn.pack()

underbtn = Checkbutton(root, text="Underscores?", variable=undervar)
underbtn.pack()

gen = Button(root, text="Generate", command=lambda:generate(10, lettervar.get(), numvar.get(), symvar.get(), undervar.get()))
gen.pack()

pwrd = Label(root, text="")
pwrd.pack()

root.mainloop()
