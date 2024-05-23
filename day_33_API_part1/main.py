from tkinter import *
import requests

# Function to get Kanye quote
def get_quote():
    response = requests.get("https://api.kanye.rest/")
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)

# Setting up the main window
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

# Adding canvas with background image
canvas = Canvas(window, width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Click the button for a quote", width=250, font=("Arial", 25, "bold"), fill="white")
canvas.grid(row=0, column=0)

# Adding Kanye button
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(window, image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

# Running the main loop
window.mainloop()
