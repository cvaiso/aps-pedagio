import tkinter as tk

class VehicleView:
    def __init__(self, root):
        self.root = root
    def add_vehicle(self):
        popup = tk.Toplevel(self.root)
        popup.title("Add Vehicle")
        popup.geometry('299x400')
        popup.configure(bg='light blue')

        plate_frame = tk.Frame(popup)
        plate_frame.pack(anchor='w', expand=True)
        tk.Label(plate_frame, text="Plate", width=11, bg='light blue').pack(side='left')
        tk.Entry(plate_frame, width=24).pack(side='left')

        model_frame = tk.Frame(popup)
        model_frame.pack(anchor='w', expand=True)
        tk.Label(model_frame, text="Model", width=11, bg='light blue').pack(side='left')
        tk.Entry(model_frame, width=24).pack(side='left')

        color_frame = tk.Frame(popup)
        color_frame.pack(anchor='w', expand=True)
        tk.Label(color_frame, text="Color", width=11, bg='light blue').pack(side='left')
        tk.Entry(color_frame, width=24).pack(side='left')

        status_frame = tk.Frame(popup)
        status_frame.pack(anchor='w', expand=True)
        tk.Label(status_frame, text="Status", width=11, bg='light blue').pack(side='left')
        status_entry = tk.Entry(status_frame, width=24)
        status_entry.insert(-1, "licensed")
        status_entry.pack(side='left')

        button_frame = tk.Frame(popup)
        button_frame.pack(anchor='center', expand=True)
        tk.Button(button_frame, text="Submit").pack(side='left')
        tk.Button(button_frame, text="Cancel", command=popup.destroy).pack(side='left')