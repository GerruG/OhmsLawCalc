import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk  

def calculate_ohms_law():
    try:
        v = voltage_entry.get()
        i = current_entry.get()
        r = resistance_entry.get()
        p = power_entry.get()

        v = float(v) if v else None
        i = float(i) if i else None
        r = float(r) if r else None
        p = float(p) if p else None

        if v is not None and i is not None:
            calculated_r = v / i
            calculated_p = v * i
            resistance_var.set(f"{calculated_r:.2f}")
            power_var.set(f"{calculated_p:.2f}")
        elif v is not None and r is not None:
            calculated_i = v / r
            calculated_p = v * calculated_i
            current_var.set(f"{calculated_i:.2f}")
            power_var.set(f"{calculated_p:.2f}")
        elif i is not None and r is not None:
            calculated_v = i * r
            calculated_p = i * calculated_v
            voltage_var.set(f"{calculated_v:.2f}")
            power_var.set(f"{calculated_p:.2f}")
        elif v is not None and p is not None:
            calculated_i = p / v
            calculated_r = v / calculated_i
            current_var.set(f"{calculated_i:.2f}")
            resistance_var.set(f"{calculated_r:.2f}")
        elif i is not None and p is not None:
            calculated_v = p / i
            calculated_r = calculated_v / i
            voltage_var.set(f"{calculated_v:.2f}")
            resistance_var.set(f"{calculated_r:.2f}")
        elif r is not None and p is not None:
            calculated_i = (p / r) ** 0.5
            calculated_v = calculated_i * r
            voltage_var.set(f"{calculated_v:.2f}")
            current_var.set(f"{calculated_i:.2f}")
        else:
            messagebox.showerror("Error", "Please enter at least two values.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def add_ohms_law_explanation(parent):
    explanation = """Ohm's Law is a fundamental principle in electrical engineering that relates voltage (V), current (I), resistance (R), and power (P) in a resistive circuit. The law is usually stated as V = I x R, which means that the voltage across a resistor is directly proportional to the current flowing through it, with the proportionality constant being the resistance.

You can calculate the power (P) using the formula P = V x I, which represents the rate of energy conversion in the circuit.

To use this calculator, enter two known values to calculate the remaining ones."""
    
    # Create a text widget for the explanation
    explanation_text = tk.Text(parent, height=12, width=50, wrap='word')
    explanation_text.grid(column=2, row=1, rowspan=4, padx=10, pady=5, sticky='NS')
    explanation_text.insert(tk.END, explanation)
    explanation_text.config(state=tk.DISABLED)  # Make the text widget read-only


def add_ohms_law_image(parent):
    # Define the path to your image
    image_path = "images/ohms-lag.jpg"

    # Load the image using PIL
    image = Image.open(image_path)
    image.thumbnail((300, 300))  # Resize the image if it's too large
    photo = ImageTk.PhotoImage(image)

    # Create a canvas to display the image
    canvas = tk.Canvas(parent, width=300, height=300)
    canvas.grid(column=2, row=5, padx=10, pady=5, sticky='EW')
    canvas.create_image(150, 150, image=photo)
    canvas.image = photo  # Keep a reference so it's not garbage collected



# Create the main window
root = tk.Tk()
root.title("Ohm's Law Calculator")
root.columnconfigure(2, weight=1)
root.resizable(False, False)

voltage_var = tk.StringVar()
current_var = tk.StringVar()
resistance_var = tk.StringVar()
power_var = tk.StringVar()

ttk.Label(root, text="Voltage (V)").grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
voltage_entry = ttk.Entry(root, textvariable=voltage_var)
voltage_entry.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5)

ttk.Label(root, text="Current (I)").grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
current_entry = ttk.Entry(root, textvariable=current_var)
current_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

ttk.Label(root, text="Resistance (R)").grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
resistance_entry = ttk.Entry(root, textvariable=resistance_var)
resistance_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

ttk.Label(root, text="Power (P)").grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
power_entry = ttk.Entry(root, textvariable=power_var)
power_entry.grid(column=1, row=3, sticky=tk.EW, padx=5, pady=5)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_ohms_law)
calculate_button.grid(column=2, row=0, padx=5, pady=5, sticky='EW')



add_ohms_law_explanation(root)
add_ohms_law_image(root)

# Run the main loop
root.mainloop()