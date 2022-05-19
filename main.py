from tkinter import *
MILES = 1.609344

window = Tk()
window.minsize(width=200, height=50)
window.title("Mile to Km Converter")
window.config(pady=10, padx=10)

# Labels
miles = Label(text="Miles")
is_iqual_to = Label(text="is equal to")
result = Label(text="0")
km = Label(text="Km")

# Fields
entry = Entry(width=20)
entry.insert(END, string="0")


# Buttons
def convert():
    measure_to_convert = float(entry.get())
    if radio_state.get() == "Miles":
        converted_measure = measure_to_convert * MILES
        result.config(text=f"{converted_measure:.4f}")
    elif radio_state.get() == "Km":
        converted_measure = measure_to_convert / MILES
        result.config(text=f"{converted_measure:.4f}")


calculate = Button(text="Calculate", command=convert)


# Radiobutton
def radio_used():
    if radio_state.get() == "Miles":
        miles.config(text="Miles")
        km.config(text="Km")
    elif radio_state.get() == "Km":
        miles.config(text="Km")
        km.config(text="Miles")


radio_state = StringVar()
radio_miles_to_km = Radiobutton(text="Miles to Km", value="Miles", variable=radio_state, command=radio_used, padx=10)
radio_miles_to_km.select()
radio_km_to_miles = Radiobutton(text="Km to Miles", value="Km", variable=radio_state, command=radio_used, padx=10)


# placement
entry.grid(column=2, row=1)
miles.grid(column=3, row=1)
is_iqual_to.grid(column=1, row=2)
result.grid(column=2, row=2)
km.grid(column=3, row=2)
calculate.grid(column=2, row=3)
radio_km_to_miles.grid(column=1, row=0)
radio_miles_to_km.grid(column=1, row=1)
entry.focus_set()


window.mainloop()
