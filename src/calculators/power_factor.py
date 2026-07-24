import tkinter as tk


def show_power_factor_calculator(content_frame):
    """Display The Power Factor Calculator Page."""

    # removing any existing widgets
    for widget in content_frame.winfo_children():
        widget.destroy()

    # create a new title
    title = tk.Label(
        content_frame,
        text='Power Factor Calculator',
        font=('Arial', 20, 'bold'),
        bg='white',
    )
    title.pack(pady=20)

    # create a label and entry for real power
    real_power_label = tk.Label(
        content_frame,
        text='Real power (KW):',
        font=('Arial', 12)
    )

    real_power_label.pack(pady=5)

    real_power_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    real_power_entry.pack(pady=5)

    # create a label and entry for apparent power

    apparent_power_label = tk.Label(
        content_frame,
        text='Apparent Power (kVA):',
        font=('Arial', 12)
    )

    apparent_power_label.pack(pady=5)

    apparent_power_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )

    apparent_power_entry.pack(pady=5)

    # calculation for power factor

    def calculate_power_factor():
        try:
            real_power = float(real_power_entry.get())
            apparent_power = float(apparent_power_entry.get())
            power_factor = real_power / apparent_power
            result_label.config(text=f'Power factor: {power_factor:.2f} ')
        except ValueError:
            result_label.config(
                text='Invalid input. Please enter valid numbers.')

    # create a label and entry to show results

    result_label = tk.Label(
        content_frame,
        text='Power Factor (0.0)',
        font=('Arial, 12'),
        fg='blue',
    )

    result_label.pack(pady=5)

    results_button = tk.Button(
        content_frame,
        width=20,
        text='Calculate',
        font=('Arial', 12),
        command=calculate_power_factor
    )

    results_button.pack(pady=5)
