import tkinter as tk
from tkinter import filedialog, messagebox

from Quantizer import *
from SignalProcessor import SignalProcessor


class Task_3:
    def __init__(self, main_window):
        self.main_window = main_window
        self.app = None  # Initialize app as None
        self.signal_processor = SignalProcessor()
        self.file_path = ""

    def open_window(self):
        if self.app is not None:
            return

        self.app = tk.Toplevel(self.main_window)
        self.app.title("Task 3")
        self.app.geometry("200x200+200+200")

        # Create a frame to hold the widgets
        frame = tk.Frame(self.app)

        # Create a Select File button
        selectfile = tk.Button(frame, text="Select file", command=self.load_file)
        selectfile.grid(row=0, column=2, pady=10)

        # Create a label as a placeholder
        self.placeholder_label = tk.Label(frame, text='Enter a number', fg='gray')
        self.number_entry = tk.Entry(frame, fg='gray')  # Set initial text color to lighter color
        self.number_entry.insert(0, 'Enter a number')
        self.number_entry.bind("<FocusIn>", self.on_entry_click)
        self.number_entry.bind("<FocusOut>", self.on_focus_out)
        self.number_entry.grid(row=5, column=2, pady=5)

        # Create Radio Buttons
        self.selected_option = tk.StringVar()
        radio1 = tk.Radiobutton(frame, text="Levels", value="Levels", variable=self.selected_option)
        radio2 = tk.Radiobutton(frame, text="Bits", value="Bits", variable=self.selected_option)
        radio1.grid(row=10, column=2)
        radio2.grid(row=15, column=2)

        # # Create perform operation button
        perform_operation_button = tk.Button(frame, text="Perform operation", command=self.perform_operation)
        perform_operation_button.grid(row=30, column=2, pady=20)
        frame.pack()

    def load_file(self):
        root = tk.Tk()
        root.withdraw()  # to hide the main window
        self.file_path = filedialog.askopenfilename(parent=root, title="Choose file")

    def perform_operation(self):
        if self.file_path == "" or self.number_entry.get() == "Enter a number":
            messagebox.showerror("Missing input", "Please select a file first and a number")
            return

        self.signal_processor.read_signal_from_file(self.file_path)
        signal = self.signal_processor.signal

        value = int(self.number_entry.get())
        output_signal = []
        if self.selected_option.get() == "Levels":
            output_signal = quantize(signal=signal, levels_num=value)
        else:
            output_signal = quantize(signal=signal, bits_num=value)

        self.signal_processor.set_signal(signal)
        self.signal_processor.display_signal()

    # Function to handle entry field click event
    def on_entry_click(self, *args):
        if self.number_entry.get() == "Enter a number":
            self.number_entry.delete(0, "end")
            self.number_entry.config(fg="black")  # Change text color to black when typing

    # Function to handle entry field focus out event
    def on_focus_out(self, *args):
        if self.number_entry.get() == "":
            self.number_entry.insert(0, "Enter a number")
            self.number_entry.config(fg="gray")  # Use the specified lighter color
