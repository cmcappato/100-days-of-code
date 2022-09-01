from tkinter import *


def button_clicked():
    # my_label.config(text="Button got clicked")
    new_text = input_.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New text")  # Or my_label["text"] = "New text"
# my_label.pack()  # Places the label in the center of the screen
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Button
new_button = Button(text="New Button", command=button_clicked)
# button.pack()
new_button.grid(column=2, row=0)

# Entry
input_ = Entry(width=10)
# input_.pack()
input_.grid(column=3, row=2)
input_.get()





window.mainloop()  # Will keep the window open so that the user can interact with it
