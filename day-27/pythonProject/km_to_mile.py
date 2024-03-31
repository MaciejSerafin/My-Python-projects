from tkinter import *


def km_to_miles():
    km = float(input.get())
    miles = km * 0.621371
    miles_result_label.config(text=f"{miles}")


window = Tk()
window.title("Km to Mile Converter")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#tekst 1 "is equal to"
my_label_1 = Label(text="is equal to", font=("Arial", 24))
my_label_1.grid(column = 0, row = 1)
my_label_1.config(padx=10, pady=10)


#entry km
input = Entry(width=10)
# input.insert(END, string="0")
input.grid(column =1, row =0)



#Label2 = "0"
miles_result_label = Label(text="0", font=("Arial", 24))
miles_result_label.grid(column = 1, row = 1)
miles_result_label.config(padx=10, pady=10)

#button = "Calculate"
button = Button(text = "Calculate", command = km_to_miles)
button.grid(column =1, row = 2)
button.config(padx=10, pady=10)


#Label3 = "Miles"
my_label_2 = Label(text="km", font=("Arial", 24))
my_label_2.grid(column = 3, row = 0)
my_label_2.config(padx=10, pady=10)

#Label4 = "Km"
my_label_3 = Label(text="miles", font=("Arial", 24))
my_label_3.grid(column = 3, row = 1)
my_label_3.config(padx=10, pady=10)


window.mainloop()