import tkinter

FONT = ("Comic Sans MS", 20, "bold")

def miles_to_km():
    num_km_label.config(text=round(int(miles_box.get()) * 1.60934, 1))


window = tkinter.Tk()
window.title("Miles to Kilometres Conversion Calculator")
window.minsize(400, 200)
window.config(padx=50, pady=50)

miles_label = tkinter.Label(text="miles", font=FONT)
miles_label.grid(column=2, row = 0)
km_label = tkinter.Label(text="kilometres", font=FONT)
km_label.grid(column=2, row=1)
equal_label = tkinter.Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

miles_box = tkinter.Entry(bg="gray95", font=FONT)
miles_box.grid(column=1, row=0)

calculate_button = tkinter.Button(text="Calculate", command=miles_to_km, font=FONT)
calculate_button.grid(column=1, row=2)

num_km_label = tkinter.Label(font=FONT)
num_km_label.grid(column=1, row=1)

window.mainloop()