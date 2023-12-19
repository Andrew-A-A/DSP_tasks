import tkinter as tk
from tkinter import filedialog

from PracticalTask import fastCorrelation, fastConvolution
from SignalProcessor import SignalProcessor


class Task_9:
    def __init__(self, main_window, title):
        self.main_window = main_window
        self.app = None  # Initialize app as None
        self.signal_processor = SignalProcessor()
        self.file_path = ["", ""]
        self.title = title

    def open_window(self):
        if self.app is not None:
            return

        self.app = tk.Toplevel(self.main_window)
        self.app.title(self.title)
        self.app.geometry("300x300+200+200")

        frame = tk.Frame(self.app, width=50)

        # Create a Load File button for the first signal
        loadfile1 = tk.Button(frame, text="Load First Signal", width=30, command=lambda: self.load_file(0))
        loadfile1.pack(padx=1, pady=5)

        # Create a Load File button for the first signal
        loadfile2 = tk.Button(frame, text="Load Second Signal", width=30, command=lambda: self.load_file(1))
        loadfile2.pack(padx=1, pady=5)

        # Create a button to execute the correlate function
        convolveButton = tk.Button(frame, text="Fast-Correlate", width=30, command=self.fast_correlate_function)
        convolveButton.pack(padx=1, pady=5)

        # Create a button to execute the convolve function
        convolveButton = tk.Button(frame, text="Fast-Convolve", width=30, command=self.fast_convolve_function)
        convolveButton.pack(padx=1, pady=5)

        frame.pack()

    def load_file(self, file_index):
        root = tk.Tk()
        root.withdraw()  # to hide the main window
        self.file_path[file_index] = filedialog.askopenfilename(parent=root, title="Choose file")

    def fast_correlate_function(self):
        signal1 = self.signal_processor.read_signal_from_file(self.file_path[0])
        signal2 = self.signal_processor.read_signal_from_file(self.file_path[1])
        indices, samples = fastCorrelation(signal1, signal2)
        result = [[a, b] for a, b in zip(indices, samples)]
        self.signal_processor.set_signal(result)
        self.signal_processor.display_signal()

    def fast_convolve_function(self):
        signal1 = self.signal_processor.read_signal_from_file(self.file_path[0])
        signal2 = self.signal_processor.read_signal_from_file(self.file_path[1])
        indices, samples = fastConvolution(signal1, signal2)
        result = [[a, b] for a, b in zip(indices, samples)]
        self.signal_processor.set_signal(result)
        self.signal_processor.display_signal()
