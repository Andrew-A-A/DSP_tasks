import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from SignalProcessor import SignalProcessor


class Task_6:
    def __init__(self, main_window, title):
        self.main_window = main_window
        self.app = None  # Initialize app as None
        self.signal_processor = SignalProcessor()
        self.file_path = ""
        self.title = title

    def open_window(self):
        if self.app is not None:
            return

        self.app = tk.Toplevel(self.main_window)
        self.app.title(self.title)
        self.app.geometry("500x500+200+200")

        frame = tk.Frame(self.app, width=50)
        # Create a Load File button
        loadfile = tk.Button(frame, text="Load File", width=10, command=self.load_file)
        loadfile.pack(side="left", padx=1)

        frame.pack()

    def load_file(self):
        root = tk.Tk()
        root.withdraw()  # to hide the main window
        self.file_path = filedialog.askopenfilename(parent=root, title="Choose file")
