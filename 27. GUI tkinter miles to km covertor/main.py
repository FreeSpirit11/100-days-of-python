from tkinter import *
window = Tk()
window.title("Calculator")
window.config(padx=20,pady=20)


def convertor():
    result = round(int(entry.get())/1.60934)
    result_label.config(text=result)

label = Label(text="is equal to")
miles_label = Label(text="Miles")
km_label = Label(text="Km")
result_label = Label(text="0")
button = Button(text="Calculate",command=convertor)
entry = Entry(width=5)
entry.focus()

#pack,place,grid.
label.grid(row=1, column=0)
miles_label.grid(row=0, column=2)
km_label.grid(row=1, column=2)
result_label.grid(row=1, column=1)
button.grid(row=3, column=1)
entry.grid(row=0, column=1)


window.mainloop()
