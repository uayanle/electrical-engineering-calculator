import tkinter as tk


def show_short_circuit_calculator(content_frame):
    """Display the Short Circuit Calculator page."""

    # removing any existing widgets
    for widget in content_frame.winfo_children():
        widget.destroy()

    # new title label and entry

    title = tk.Label(
        content_frame,
        text='Short Circuit Calculator',
        font=('Arial', 20),
        bg='white',
    )

    title.pack(pady=20)

    # creating a label and entry for voltage

    voltage_label = tk.Label(
        content_frame,
        text=('Voltage (V)'),
        font=('Arial', 12)
    )

    voltage_label.pack(pady=5)

    voltage_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    voltage_entry.pack(pady=5)

# creating a new label and entry for impedance

    impedance_label = tk.Label(
        content_frame,
        text='Impedance (Ω)',
        font=('Arial', 12)
    )

    impedance_label.pack(pady=5)

    impedance_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12),
    )

    impedance_entry.pack(pady=5)

    def calculate_short_circuit_current():
        try:
            voltage = float(voltage_entry.get())
            impedance = float(impedance_entry.get())
            short_circuit_current = voltage / impedance
            results_label.config(
                text=f"Short circuit current: {short_circuit_current:.2f} A")
        except ValueError:
            results_label.config(text="Please enter valid numbers.")

    # calculate button

    calculate_button = tk.Button(
        content_frame,
        text='Calculate',
        font=('Arial', 12),
        command=calculate_short_circuit_current,
        bg='white',
    )

    calculate_button.pack(pady=10)

    # results

    results_label = tk.Label(
        content_frame,
        text='Current is:',
        font=('Arial', 12),
        bg='white',
    )

    results_label.pack(pady=5)
