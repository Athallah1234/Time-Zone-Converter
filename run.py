import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz

class TimeZoneConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Time Zone Converter")

        # Time Zone Options
        self.timezones = list(pytz.all_timezones)
        self.selected_timezone1 = tk.StringVar(value=self.timezones[0])
        self.selected_timezone2 = tk.StringVar(value=self.timezones[0])

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Labels
        label1 = ttk.Label(self.root, text="Enter Time:")
        label1.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        label2 = ttk.Label(self.root, text="From Time Zone:")
        label2.grid(row=1, column=0, padx=10, pady=10, sticky="W")

        label3 = ttk.Label(self.root, text="To Time Zone:")
        label3.grid(row=2, column=0, padx=10, pady=10, sticky="W")

        label4 = ttk.Label(self.root, text="Converted Time:")
        label4.grid(row=3, column=0, padx=10, pady=10, sticky="W")

        # Entry Widgets
        self.time_entry = ttk.Entry(self.root)
        self.time_entry.grid(row=0, column=1, padx=10, pady=10)

        # Comboboxes for Time Zones
        self.timezone1_combobox = ttk.Combobox(self.root, values=self.timezones, textvariable=self.selected_timezone1)
        self.timezone1_combobox.grid(row=1, column=1, padx=10, pady=10)

        self.timezone2_combobox = ttk.Combobox(self.root, values=self.timezones, textvariable=self.selected_timezone2)
        self.timezone2_combobox.grid(row=2, column=1, padx=10, pady=10)

        # Display Converted Time
        self.converted_time_label = ttk.Label(self.root, text="")
        self.converted_time_label.grid(row=3, column=1, padx=10, pady=10, sticky="W")

        # Convert Button
        convert_button = ttk.Button(self.root, text="Convert", command=self.convert_time)
        convert_button.grid(row=4, column=1, padx=10, pady=10, sticky="W")

    def convert_time(self):
        input_time_str = self.time_entry.get().strip()  # Remove leading and trailing whitespaces

        if not input_time_str:
            self.converted_time_label.config(text="Error: Please enter a valid time.")
            return

        try:
            input_time = datetime.strptime(input_time_str, "%Y-%m-%d %H:%M:%S")
            from_timezone = pytz.timezone(self.selected_timezone1.get())
            to_timezone = pytz.timezone(self.selected_timezone2.get())

            converted_time = input_time.replace(tzinfo=from_timezone).astimezone(to_timezone)

            self.converted_time_label.config(text=converted_time.strftime("%Y-%m-%d %H:%M:%S %Z"))
        except ValueError as e:
            self.converted_time_label.config(text="Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeZoneConverterApp(root)
    root.mainloop()

