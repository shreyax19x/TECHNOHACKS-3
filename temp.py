import tkinter as tk

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return celsius * 9.0/5.0 + 32

def convert_temperature():
    try:
        temperature = float(entry_temperature.get())
        unit = temperature_unit.get()

        if unit == 'Fahrenheit':
            result = fahrenheit_to_celsius(temperature)
            result_label.config(text=f"{temperature:.2f} Fahrenheit is equal to {result:.2f} Celsius.")
        elif unit == 'Celsius':
            result = celsius_to_fahrenheit(temperature)
            result_label.config(text=f"{temperature:.2f} Celsius is equal to {result:.2f} Fahrenheit.")
        else:
            result_label.config(text="Invalid unit. Please enter 'Fahrenheit' or 'Celsius'.")
    except ValueError:
        result_label.config(text="Invalid temperature. Please enter a valid number.")


window = tk.Tk()
window.title("Temperature Converter")


font_style = ("Arial", 14)
padding = 10


entry_temperature = tk.Entry(window, width=10, font=font_style, justify="center")
entry_temperature.grid(row=0, column=0, padx=padding, pady=padding, sticky="ew")


temperature_unit = tk.StringVar(value='Fahrenheit')
unit_menu = tk.OptionMenu(window, temperature_unit, 'Fahrenheit', 'Celcisus')
unit_menu.config(font=font_style,fg="#008CBA")
unit_menu.grid(row=0, column=1, padx=padding, pady=padding, sticky="ew")

convert_button = tk.Button(window, text="Convert", command=convert_temperature, font=font_style,fg="#008CBA")
convert_button.grid(row=1, column=0, columnspan=2, pady=padding, sticky="ew")

result_label = tk.Label(window, text="", font=font_style,fg="#008CBA")
result_label.grid(row=2, column=0, columnspan=2, pady=padding)

footer_label = tk.Label(window, text="Task-Temperature Converter", font=("Arial", 15), pady=padding, foreground="#555")
footer_label.grid(row=3, column=0, columnspan=2, pady=padding)

for i in range(4):
    window.grid_rowconfigure(i, weight=1)
    window.grid_columnconfigure(i, weight=1)

for child in window.winfo_children():
    child.grid_configure(padx=padding, pady=padding)

window.mainloop()