from tkinter import *

def button_clicked():
    print("I got clicked")
    data = input.get()
    my_label.config(text = data)


window = Tk()
window.title("My first GUI prograam")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text = "New Text")
my_label.grid(column = 0, row = 0)
my_label.config(padx=50, pady=50)


#Button
button = Button(text = "Click Me", command = button_clicked)
button.grid(column =1, row = 1)

#Button2
button2 = Button(text = "Click Me", command = button_clicked)
button2.grid(column =2, row = 0)


#Entry

input = Entry(width=10)
print(input.get())
input.grid(column = 3, row =3 )



window.mainloop()