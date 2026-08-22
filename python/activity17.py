from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


main = Tk()
main.title("Denomination Calculator")
main.configure(bg="light blue")
main.geomtery('750x500')

upload = Image.open("tkinterimage.jpg")
upload = upload.resize((400,400))
Image = ImageTk.PhotoImage(upload)
label = Label(main, image="image", bg="light blue")
label.place(x=200, y=40)

label1 = Label(main, text = "Welcome to Denomination Counter Application User!", bg="light blue")
label1.place(relx=1, y=400, anchor= CENTER) #This is how you define anchor, center
def toplevel():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry("650x400")

    label = Label("top", text="Enter total amount", bg="light grey")
    enter = Entry("top")
    lb1 = Label("top", text ="Here are the numbers of notes for each denomination", bg="light grey")

    l1 = Label("top", text="2000" , bg="light grey")
    l2 = Label("top", text="500" , bg="light grey")
    l3 = Label("top", text="100" , bg="light grey")
    l4 = Label("top", text="50" , bg="light grey")
    l5 = Label("top", text="10" , bg="light grey")

    t1 = Entry("top")
    t2 = Entry("top")
    t3 = Entry("top")
    t4 = Entry("top")
    t5 = Entry("top")

    def calculator():
        try: 
            global amount
            amount = int(Entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            amount %= 100
            note50 = amount // 50
            amount %= 50
            note10 = amount // 10
            amount %= 10      

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)
            t5.delete(0, END)

            t1.insert(0, END, str(note2000))
            t2.insert(0, END, str(note500))
            t3.insert(0, END, str(note100))
            t4.insert(0, END, str(note50))
            t5.insert(0, END, str(note10))    
        except ValueError: # the error box will pop up if nothing is typed
            messagebox.showerror("Error", "Please enter a valid value")

    btn = Button("top", text = "calculate", command="calculator", bg="brown", fg="white")

    label.place(x=230, y=50)
    Entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lb1.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)


    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

calc_button = Button(main, text="Open Calculator", command=toplevel, bg='green', fg='white', font=('Arial', 16))
calc_button.place(relx=0.5, y=370, anchor=CENTER)

main.mainloop()