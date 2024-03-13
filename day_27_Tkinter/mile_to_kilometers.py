import tkinter

def convert_miles_to_km():
    # Get the value from miles_input, convert it to kilometers and update kilometer_result
    miles = float(miles_input.get())  # Get the value from the entry as float
    kilometers = miles * 1.60934  # Convert miles to kilometers
    kilometer_result.config(text=f"{kilometers}")  # Update the label with the result

window = tkinter.Tk()
window.title("Miles to Kilometer Converter")

# Creating an Entry widget for miles input
miles_input = tkinter.Entry(window)
miles_input.grid(column=1, row=0)

# Creating a Label widget for "Miles"
miles_label = tkinter.Label(window, text="Miles")
miles_label.grid(column=2, row=0)

# "is equal to" label
is_label_equal = tkinter.Label(window, text="is equal to")
is_label_equal.grid(column=0, row=1)

# Result label, initially set to "0"
kilometer_result = tkinter.Label(window, text="0")
kilometer_result.grid(column=1, row=1)

# "Km" label
kilometer_label = tkinter.Label(window, text="Km")
kilometer_label.grid(column=2, row=1)

# Calculate button, which calls the convert_miles_to_km function when clicked
calculate_mile = tkinter.Button(window, text="Calculate", command=convert_miles_to_km)
calculate_mile.grid(column=1, row=2)

window.mainloop()
