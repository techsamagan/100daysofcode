import tkinter

window = tkinter.Tk()
window.title("My windows program")
window.minsize(width = 500, height=300)


#Label
my_label = tkinter.Label(text="I am Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


#Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button got clicked")
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()
window.mainloop()


#Entry
input = tkinter.Entry(width=10, height=7)
input.pack(text="Enter")