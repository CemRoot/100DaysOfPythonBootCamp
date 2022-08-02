BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *

window = Tk()
window.title("Flash Card App")
window.config(padx=20, pady=20)
window.configure(background=BACKGROUND_COLOR)
my_image = PhotoImage(file="card_front.png")
my_label = Label(image=my_image)


mainloop()