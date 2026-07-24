import tkinter as tk
from calculators.three_phase import show_three_phase_calculator
from calculators.voltage_drop import show_voltage_drop_calculator
from calculators.transformer import show_transformer_calculator
from calculators.power_factor import show_power_factor_calculator
from calculators.motor import show_motor_current_calculator
import math


root = tk.Tk()  # creates the main application window

# window title
root.title("Electrical Engineering Calculator")

# window size
root.geometry("1000x600")

# prevention of window becoming too small
root.minsize(800, 500)

# creating the left menu
menu_frame = tk.Frame(root, width=250, bg="#2C3E50")
menu_frame.pack(side='left', fill='y')

# creating the menu title because we want label inside the menu frame
menu_title = tk.Label(
    menu_frame,
    text='Calculators',
    font=('Arial', 16, 'bold'),
    fg='white',
    bg='#2C3E50',
)
# adding padding to the menu title to make it look better
menu_title.pack(pady=20)


# creating my main content workspace
content_frame = tk.Frame(root, bg='white')
content_frame.pack(side='right', expand=True, fill='both')

# welcome message
welcome_label = tk.Label(
    content_frame,
    text='Welcome to the Electrical Engineering Calculator!',
    font=('Arial', 18),
    bg='white',

)

# adding padding to the welcome message to make it look better
welcome_label.pack(pady=40)


def show_three_phase_calculator():
    """Display the Three Phase Calculator page."""

    # Remove any existing widgets in the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # create a new title
    title = tk.Label(
        content_frame,
        text='Three Phase Calculator',
        font=('Arial', 20, 'bold'),
        bg='white',
    )

    title.pack(pady=20)

# create a label and entry for voltage
    voltage_label = tk.Label(
        content_frame,
        text='Voltage (V):',
        font=('Arial', 12),
    )
    voltage_label.pack(pady=5)

    voltage_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )
    voltage_entry.pack(pady=5)

    # create a label and entry for current
    current_label = tk.Label(
        content_frame,
        text='Current (A):',
        font=('Arial', 12),

    )
    current_label.pack(pady=5)

    current_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12),
    )
    current_entry.pack(pady=5)

    # create a label and entry for power factor
    power_factor_label = tk.Label(
        content_frame,
        text='Power Factor:',
        font=('Arial', 12),
    )
    power_factor_label.pack(pady=5)

    power_factor_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12),
    )
    power_factor_entry.pack(pady=5)

    # Calculation function
    def calculate_three_phase_power():
        try:
            voltage = float(voltage_entry.get())
            current = float(current_entry.get())
            power_factor = float(power_factor_entry.get())
            power = math.sqrt(3) * voltage * current * power_factor
            power_kw = power / 1000  # convert to kilowatts
            result_label.config(text=f"Power: {power_kw:.2f} kW")
        except ValueError:
            result_label.config(text="Please enter valid numbers.")

    # calculate button
    calculate_button = tk.Button(
        content_frame,
        text='Calculate',
        font=('Arial', 12),
        command=calculate_three_phase_power
    )
    calculate_button.pack(pady=10)
    result_label = tk.Label(
        content_frame,
        text="Power:",
        font=("Arial", 14),
        bg="white",
    )
    result_label.pack(pady=20)


# adding the first button
three_phase_button = tk.Button(
    menu_frame,
    text='Three Phase Calculator',
    width=20,
    command=show_three_phase_calculator
)
three_phase_button.pack(pady=5)

# adding the second button
voltage_drop_button = tk.Button(
    menu_frame,
    text='Voltage Drop Calculator',
    width=20,
    command=lambda: show_voltage_drop_calculator(content_frame)


)
voltage_drop_button.pack(pady=5)

# adding the third button
power_factor_button = tk.Button(
    menu_frame,
    text='Power Factor Calculator',
    width=20,
    command=lambda: show_power_factor_calculator(content_frame)

)
power_factor_button.pack(pady=5)

# adding the fourth button
transformer_button = tk.Button(
    menu_frame,
    text='Transformer Calculator',
    width=20,
    command=lambda: show_transformer_calculator(content_frame)

)
transformer_button.pack(pady=5)

# adding the fifth button
motor_current_button = tk.Button(
    menu_frame,
    text='Motor Current Calculator',
    width=20,
    command=lambda: show_motor_current_calculator(content_frame)
)

motor_current_button.pack(pady=5)

# adding the sixth button
cable_sizing_button = tk.Button(
    menu_frame,
    text='Cable sizing Calculator',
    width=20
)
cable_sizing_button.pack(pady=5)

# adding the seventh button
short_circuit_button = tk.Button(
    menu_frame,
    text='Short Circuit Calculator',
    width=20
)

short_circuit_button.pack(pady=5)

# keep the application running
root.mainloop()
