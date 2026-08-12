from tkinter import *

tab = Tk()
tab.title("Tkinter Window")
tab.geometry("800x800")

heading = Label(text="Welcome to this Website", fg="white", bg ="black")
button = Button(text="Click me", bg ="white", fg ="grey")
interact = Entry(fg="green", bg = "yellow", width = 20)
heading.pack()
button.pack()
interact.pack()

Frame = Frame(master=tab, relief = SUNKEN, borderwidth=10)
Frame.pack()
label = Label(master=Frame, text="Hope you are doing well")
label.pack()

textbox = Text(fg="black", bg="green")
textbox.pack()

tab.mainloop()