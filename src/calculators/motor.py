import tkinter as tk
import math


def show_motor_current_calculator(content_frame):
    """Display The Motor Current Calculator Page."""

    # remove any existing widgets
    for widget in content_frame.winfo_children():
        widget.destroy()

    # create a new title
    title = tk.Label(
        content_frame,
        text='Motor Current Calculator',
        font=('Arial', 20),
        bg='white',
    )

    title.pack(pady=20)

    # create a label and entry for motor power

    motor_power_label = tk.Label(
        content_frame,
        text='Motor Label (kW)',
        font=('Arial', 12)
    )

    motor_power_label.pack(pady=5)

    motor_power_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    motor_power_entry.pack(pady=5)

    # create a label and entry for line voltage

    line_voltage_label = tk.Label(
        content_frame,
        text='Line Voltage (V)',
        font=('Arial', 12)
    )

    line_voltage_label.pack(pady=5)

    line_voltage_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12),
    )

    line_voltage_entry.pack(pady=5)

    # create a label and entry for power factor

    power_factor_label = tk.Label(
        content_frame,
        text='Power Factor',
        font=('Arial', 12)
    )

    power_factor_label.pack(pady=5)

    power_factor_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    power_factor_entry.pack(pady=5)

    # create a label and entry for efficiency

    efficiency_label = tk.Label(
        content_frame,
        text='Efficiency',
        font=('Arial', 12)
    )

    efficiency_label.pack(pady=5)

    efficiency_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    efficiency_entry.pack(pady=5)

    # calculation for motor current

    def calculate_motor_current():
        try:
            motor_power = float(motor_power_entry.get())
            line_voltage = float(line_voltage_entry.get())
            power_factor = float(power_factor_entry.get())
            efficiency = float(efficiency_entry.get())
            motor_current = motor_power / (
                line_voltage * power_factor * efficiency * math.sqrt(3)
            )
            result_label.config(text=f'Motor Current: {motor_current:.2f} A')
        except ValueError:
            result_label.config(
                text='Invalid input. Please enter valid numbers.'
            )

    result_label = tk.Label(
        content_frame,
        text='Motor Current (0.0)',
        font=('Arial', 12),
        fg='blue',
    )

    result_label.pack(pady=5)

    results_button = tk.Button(
        content_frame,
        width=20,
        text='Calculate',
        font=('Arial', 12),
        command=calculate_motor_current
    )

    results_button.pack(pady=5)
