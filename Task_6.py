import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from SignalProcessor import SignalProcessor
from SignalToolkit import *
import matplotlib.pyplot as plt


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
        self.app.geometry("300x300+200+200")

        frame = tk.Frame(self.app, width=50)
        # Create a Load File button
        loadfile = tk.Button(frame, text="Load File", width=10, command=self.load_file)
        loadfile.pack(padx=1)

        # Create a smoothing button
        Smooth = tk.Button(frame, text="Smooth", width=10, command=self.smooth_function)
        Smooth.pack(padx=1, pady=5)

        # Create a sharpening button
        Sharpen = tk.Button(
            frame, text="Sharpen", width=10, command=self.sharpen_function
        )
        Sharpen.pack(padx=1, pady=5)

        # Create a folding button
        folding = tk.Button(frame, text="Fold", width=10, command=self.fold_function)
        folding.pack(padx=1, pady=5)

        # Create a remove_dc button
        remove_dc = tk.Button(
            frame, text="Remove DC", width=10, command=self.remove_dc_function
        )
        remove_dc.pack(padx=1, pady=5)

        # Create a shift_fold button
        shift_fold = tk.Button(
            frame, text="Shift Folding", width=10, command=self.shift_fold_function
        )
        shift_fold.pack(padx=1, pady=5)

        # create a number_entry entry enter the window size
        self.number_entry_windwo_size = tk.Entry(frame, fg="gray", width=23)
        self.number_entry_windwo_size.pack(padx=1, pady=5)

        # create a number_entry entry enter the shifting value
        self.number_entry_shift = tk.Entry(frame, fg="gray", width=23)
        self.number_entry_shift.pack(padx=1, pady=5)

        # initialize the number entries
        self.number_entries = [
            (self.number_entry_windwo_size, "Enter the Window size"),
            (self.number_entry_shift, "Enter the Shifting Value"),
        ]
        for number_entry in self.number_entries:
            # Initialize the number_entry`s value with a placeholder
            number_entry[0].insert(0, number_entry[1])

            number_entry[0].bind(
                "<FocusIn>",
                lambda event, number_entry=number_entry: self.on_entry_click(
                    event, number_entry
                ),
            )
            number_entry[0].bind(
                "<FocusOut>",
                lambda event, number_entry=number_entry: self.on_focus_out(
                    event, number_entry
                ),
            )

        frame.pack()

    def load_file(self):
        root = tk.Tk()
        root.withdraw()  # to hide the main window
        self.file_path = filedialog.askopenfilename(parent=root, title="Choose file")

    def smooth_function(self):
        signal = self.signal_processor.read_signal_from_file(self.file_path)
        window_size = int(self.number_entry_windwo_size.get())
        signal = smooth_amplitudes(signal, window_size)
        self.plot("Index", "Amplitude", np.array(signal))

    def sharpen_function(self):
        signal = self.signal_processor.read_signal_from_file(self.file_path)
        first, second = sharping(signal)
        signal = np.column_stack((first, second)).tolist()
        self.plot("Index", "Amplitude", np.array(signal))

    def fold_function(self):
        signal = self.signal_processor.read_signal_from_file(self.file_path)
        signal = folding(signal)
        self.plot("Index", "Amplitude", np.array(signal))

    def remove_dc_function(self):
        signal = self.signal_processor.read_signal_from_file(self.file_path)
        signal = remove_dc_frequency_domain(signal)
        self.plot("Index", "Amplitude", np.array(signal))

    def shift_fold_function(self):
        signal = self.signal_processor.read_signal_from_file(self.file_path)
        shifting_value = int(self.number_entry_shift.get())
        signal = shift_folding(signal, shifting_value)
        self.plot("Index", "Amplitude", np.array(signal))

    def plot(self, X_axis_label, Y_axis_label, data):
        x = data[:, 0]  # get the first column
        y = data[:, 1]  # get the second column
        # plot
        plt.plot(x, y)
        # give labels for x-axis and y-axis
        plt.xlabel(X_axis_label)
        plt.ylabel(Y_axis_label)
        # Add a title to the plot
        plt.title(f"{X_axis_label} verses {Y_axis_label}")
        # Add a legend to the plot
        plt.legend()
        # Display the plot
        plt.show()

    # Function to handle entry field click event
    def on_entry_click(self, event, number_entry):
        if number_entry[0].get() == number_entry[1]:
            number_entry[0].delete(0, "end")
            number_entry[0].config(fg="black")  # Change text color to black when typing

    # Function to handle entry field focus out event
    def on_focus_out(self, event, number_entry):
        if number_entry[0].get() == "":
            number_entry[0].insert(0, number_entry[1])
            number_entry[0].config(fg="gray")  # Use the specified lighter color
