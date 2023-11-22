import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt

from Quantizer import *
from FreqTools import *
from SignalProcessor import SignalProcessor
from FourierMagic import dft, sketch, idft


class Task_45:
    def __init__(self, main_window, title):
        self.main_window = main_window
        self.app = None  # Initialize app as None
        self.signal_processor = SignalProcessor()
        self.file_path = ""
        self.title = title
        self.EPSILON = 10 ** (-8)  # to compare floating numbers

    def open_window(self):
        if self.app is not None:
            return

        self.app = tk.Toplevel(self.main_window)
        self.app.title(self.title)
        self.app.geometry("835x500+200+200")

        # Create a frame to hold the widgets
        frame = tk.Frame(self.app, width=50)

        # create a frame for select/save file
        files = tk.Frame(frame, width=22)

        # Create a Load File button
        loadfile = tk.Button(files, text="Load File", width=10, command=self.load_file)
        loadfile.pack(side="left", padx=1)

        # Create a save File button
        savefile = tk.Button(files, text="Save Table", width=10, command=self.save_file)
        savefile.pack(side="right", padx=1)

        # place files frame
        files.grid(row=0, column=0, pady=10)
        # Create an entry point to save M records
        self.number_entry_records = tk.Entry(frame, fg="gray", width=33)
        self.number_entry_records.grid(row=2, column=0, padx=5, pady=5)

        # Create a button to execute the DFT
        DFT_button = tk.Button(frame, text="DFT", width=20, command=self.implementDFT)
        DFT_button.grid(row=5, column=0, pady=2)

        # Create a button to execute the DFT
        IDFT_button = tk.Button(
            frame, text="IDFT", width=20, command=self.implementIDFT
        )
        IDFT_button.grid(row=7, column=0, pady=2)

        # Create a button to execute DCT
        DFT_button = tk.Button(frame, text="DCT", width=20, command=self.implementDCT)
        DFT_button.grid(row=10, column=0, pady=2)

        # Create a button to execute remove_DC
        DFT_button = tk.Button(
            frame, text="Remove DC", width=20, command=self.implementRemove_DC
        )
        DFT_button.grid(row=12, column=0, pady=2)

        # create entry number for sampling_frequency
        self.number_entry_sampling_frequency = tk.Entry(frame, fg="gray", width=30)
        self.number_entry_sampling_frequency.grid(row=15, column=0, padx=5, pady=40)

        # Create a Plot file button
        plot_button = tk.Button(
            frame, text="Plot", width=10, command=self.plot_function
        )
        plot_button.grid(row=17, column=0, padx=5, pady=5)

        # place the frame
        frame.pack(side="left")
        # create the table that contains [Amplitude, Phase Shift]
        self.create_table()

    def implementDFT(self):
        if len(self.file_path) == 0:
            messagebox.showerror("Missing Input", "Please select a file first")
            return

        # clear the elements in the tree
        for child in self.tree.get_children():
            self.tree.delete(child)

        signal = self.signal_processor.read_signal_from_file(self.file_path)
        lst = dft(signal)

        # add the lst to the tree
        for sample in lst:
            self.add_sample((sample[0], sample[1]))

    def implementIDFT(self):
        data = self.signal_processor.read_signal_from_file(self.file_path)
        if len(data) == 0:
            messagebox.showerror("Missing Input", "Please select a file first")
            return

        self.signal_processor.signal = idft(data)
        self.signal_processor.display_signal(self.signal_processor.signal)

    def plot_function(self):
        root = tk.Tk()
        root.withdraw()  # to hide the main window
        file_path = filedialog.askopenfilename(parent=root, title="Choose file")

        if len(file_path) == 0:
            messagebox.showerror("Missing Input", "Please select a file first")
            return

        sampling_frequency = self.number_entry_sampling_frequency.get()
        if sampling_frequency == self.number_entries[3][1]:
            messagebox.showerror("Missing Input", "Please enter the Sampling Frequency")
            return

        sampling_frequency = int(sampling_frequency)
        sample_file = self.signal_processor.read_signal_from_file(file_path)

        frequency_amplitude, frequency_phase = sketch(sample_file, sampling_frequency)
        # plot frequency verse Amplitude
        self.plot("Frequency", "Amplitude", np.array(frequency_amplitude))
        # plot frequency verse Phase Shift
        self.plot("Frequency", "Phase Shift", np.array(frequency_phase))

    def implementDCT(self):
        if len(self.file_path) == 0:
            messagebox.showerror("Missing Input", "Please select a file first")
            return

        # clear the elements in the tree
        for child in self.tree.get_children():
            self.tree.delete(child)

        signal = self.signal_processor.read_signal_from_file(self.file_path)
        result = dct(signal)
        data = [[i, result[i]] for i in range(len(result))]
        # add the lst to the tree
        for sample in data:
            self.add_sample((sample[0], sample[1]))

        self.plot("K", "X(K)", np.array(data))

    def implementRemove_DC(self):
        if len(self.file_path) == 0:
            messagebox.showerror("Missing Input", "Please select a file first")
            return
        # clear the elements in the tree
        for child in self.tree.get_children():
            self.tree.delete(child)

        signal = self.signal_processor.read_signal_from_file(self.file_path)
        result = remove_dc(signal)
        data = [[i, result[i]] for i in range(len(result))]
        # add the lst to the tree
        for sample in data:
            self.add_sample((sample[0], sample[1]))

        self.plot("K", "X(K)", np.array(data))

    def plot(self, X_axis_label, Y_axis_label, data):
        x = data[:, 0]  # get the first column
        y = data[:, 1]  # get the second column
        # plot
        plt.plot(x, y)
        # Add a legend to the plot
        plt.legend()
        # give labels for x-axis and y-axis
        plt.xlabel(X_axis_label)
        plt.ylabel(Y_axis_label)
        # Add a title to the plot
        plt.title(f"{X_axis_label} Verses {Y_axis_label}")
        # Display the plot
        plt.show()

    def load_file(self):
        root = tk.Tk()
        root.withdraw()  # to hide the main window
        self.file_path = filedialog.askopenfilename(parent=root, title="Choose file")

    def save_file(self):
        data = []
        # save only the required number of records (if not specified save the whole table)
        cnt = 0
        limit = 0
        if (
            self.number_entry_records.get() == "Enter the number of samples to save"
            or len(self.number_entry_records.get()) == 0
        ):
            limit = len(self.tree.get_children())
        else:
            limit = int(self.number_entry_records.get())
        # itterate over the table to change the amplitude and/or the phase shift
        for child in self.tree.get_children():
            if cnt >= limit:
                break
            cur_Amp = float(self.tree.item(child)["values"][0])
            cur_phaseShift = float(self.tree.item(child)["values"][1])
            cnt += 1

            data.append([cur_Amp, cur_phaseShift])

        if len(data) == 0:
            messagebox.showerror("Table is empty", "Please run an algorithm first")
            return

        # Open a file dialog to select a file to save
        root = tk.Tk()
        root.withdraw()  # to hide the main window
        filename = filedialog.asksaveasfilename(parent=root, defaultextension=".txt")

        if len(filename) == 0:
            return

        # Open the file in write mode
        with open(filename, "w") as f:
            f.write("0\n")
            f.write(str(int(self.is_periodic(data))) + "\n")
            f.write(str(len(data)) + "\n")

            # Write each inner list to a separate line in the file
            for idx in range(len(data)):
                line = ""
                for value in data[idx]:
                    # each line tht contains the values should be seperated by a space
                    if len(line) > 0:
                        line += " "
                    line += str(value)

                if idx > 0:
                    line = "\n" + line

                f.write(line)

    def add_sample(self, sample):  # sample must be tuple
        self.tree.insert("", "end", text=len(self.tree.get_children()), values=sample)

    def edit_sample(self):  # sample must be tuple
        Index = int(self.number_entry_Index.get())
        if Index >= len(self.tree.get_children()):
            return

        new_Amp = self.number_entry_Amp.get()
        new_phaseShift = self.number_entry_phaseShift.get()

        item_id = self.tree.get_children()[Index]

        old_Amp = float(self.tree.item(item_id)["values"][0])
        old_phaseShift = float(self.tree.item(item_id)["values"][1])

        # if the user haven`t change the amplitude keep it unchanged
        if new_Amp == self.number_entries[1][1]:
            new_Amp = old_Amp
        else:
            new_Amp = float(new_Amp)

        # if the user haven`t change the phase shift keep it unchanged
        if new_phaseShift == self.number_entries[2][1]:
            new_phaseShift = old_phaseShift
        else:
            new_phaseShift = float(new_phaseShift)

        old_Amp = abs(old_Amp)
        old_phaseShift = abs(old_phaseShift)

        # itterate over the table to change the amplitude and/or the phase shift
        for child in self.tree.get_children():
            cur_Amp = abs(float(self.tree.item(child)["values"][0]))
            cur_phaseShift = abs(float(self.tree.item(child)["values"][1]))

            # change the amplitue if it is the same as the changed amplitude
            if abs(cur_Amp - old_Amp) < self.EPSILON:
                cur_Amp = new_Amp
            # change the phase shift if it is the same as the changed phase shift
            if abs(cur_phaseShift - old_phaseShift) < self.EPSILON:
                cur_phaseShift = new_phaseShift

            # modify the row in the tree table
            self.tree.item(child, values=(cur_Amp, cur_phaseShift))

    def create_table(self):
        # Create a treeview with 3 columns
        columns = ("Column #1", "Column #2")
        self.tree = ttk.Treeview(
            self.app, columns=columns, selectmode="extended", height=100
        )
        for column in columns:
            self.tree.heading(column, text=column, anchor=tk.CENTER)
            self.tree.column(column, anchor=tk.CENTER)

        # Add a scrollbar to the treeview
        self.scrollbar = ttk.Scrollbar(
            self.app, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        # create a frame to handle the samples editing
        frame = tk.Frame(self.app)

        # create a number_entry to enter the index of the sample to be edited
        self.number_entry_Index = tk.Entry(frame, fg="gray", width=23)
        self.number_entry_Index.grid(row=1, column=100, padx=5)

        # create a number_entry to enter the new Amplitude
        self.number_entry_Amp = tk.Entry(frame, fg="gray", width=23)
        self.number_entry_Amp.grid(row=1, column=120, padx=5)

        # create a number_entry entry enter the new phase shift
        self.number_entry_phaseShift = tk.Entry(frame, fg="gray", width=23)
        self.number_entry_phaseShift.grid(row=1, column=140, padx=5)

        # initialize the number entries
        self.number_entries = [
            (self.number_entry_Index, "Enter the Index"),
            (self.number_entry_Amp, "Enter the new Amplitude"),
            (self.number_entry_phaseShift, "Enter the new PhaseShift"),
            (self.number_entry_sampling_frequency, "Enter the Sampling Frequency"),
            (
                self.number_entry_records,
                "Enter the number of samples to save",
            ),
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

        # create a button to edit the cells of the table
        Edit_button = tk.Button(
            frame, text="Modify", width=15, command=self.edit_sample
        )
        Edit_button.grid(row=1, column=150, padx=10)

        # Pack the frame
        frame.pack(side="bottom", expand=True, padx=10, pady=10)
        # Pack the treeview to the window
        self.tree.pack(side="right", expand=True)

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

    def is_periodic(self, signal):
        # Find the dominant frequency component
        L = 0
        R = len(signal) - 1

        while L < R:
            if (
                abs(signal[L][0] - signal[R][1]) > self.EPSILON
                or abs(signal[L][1] - signal[R][1]) > self.EPSILON
            ):
                return True

        return False  # No significant harmonic, signal is periodic
