import tkinter as tk


def show_cable__sizing_calculator(content_frame):
    """Display The Cable Sizing Calculator Page."""

    # Remove any existing widgets
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Create a new title
    title = tk.Label(
        content_frame,
        text='Cable Sizing Calculator',
        font=('Arial', 20),
        bg='white',
    )
    title.pack(pady=20)

    # Create a label and entry for current
    current_label = tk.Label(
        content_frame,
        text='Current (A)',
        font=('Arial', 12)
    )
    current_label.pack(pady=5)

    current_entry = tk.Entry(
        content_frame,
        width=20,
        font=('Arial', 12)
    )
    current_entry.pack(pady=5)

    result_label = tk.Label(
        content_frame,
        text='Size Recommended:',
        font=('Arial', 12),
        fg='red'
    )
    result_label.pack(pady=10)

    def calculate():
        try:
            current = float(current_entry.get())
            if current <= 20:
                result_label.config(text='Cable size is 2.5 mm²')
            elif current <= 32:
                result_label.config(text='Cable size is 4 mm²')
            elif current <= 40:
                result_label.config(text='Cable size is 6 mm²')
            elif current <= 63:
                result_label.config(text='Cable size is 10 mm²')
            elif current <= 80:
                result_label.config(text='Cable size is 16 mm²')
            elif current <= 100:
                result_label.config(text='Cable size is 25 mm²')
            else:
                result_label.config(text='Consult cable tables')
        except ValueError:
            result_label.config(text='Please enter valid numeric values.')

    calculate_button = tk.Button(
        content_frame,
        text='Calculate',
        font=('Arial', 12),
        command=calculate
    )
    calculate_button.pack(pady=5)
