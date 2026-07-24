import tkinter as tk


def show_cable__sizing_calculator(content_frame):
    """Display The Cable Sizing Calculator Page."""

    # removing any existing widgets
    for widget in content_frame.winfo_children():
        widget.destroy()

    # create a new title
        title = tk.Label(
            content_frame,
            text='Cable Sizing Calculator',
            font=('Arial', 20),
            bg='white',
        )

        title.pack(pady=20)
