from tkinter import *


def calculate_kms():
    kms = float(miles_input.get()) * 1.609
    result_label.config(text=str(kms).format("{:.2f}"))


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)
miles_input.get()

miles_label = Label(text="Miles", font=("Arial", 18))
miles_label.grid(column=2, row=0)

equals_label = Label(text="is equal to", font=("Arial", 18))
equals_label.grid(column=0, row=1)

result_label = Label(text="0", font=("Arial", 18))
result_label.grid(column=1, row=1)

kms_label = Label(text="Km", font=("Arial", 18))
kms_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate_kms)
calculate_button.grid(column=1, row=2)

window.mainloop()
