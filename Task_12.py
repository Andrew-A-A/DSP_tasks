import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ArethmaticOperations import *
from SignalProcessor import SignalProcessor
from testing import SignalSamplesAreEqual


class Task_12:
    def __init__(self, main_window):
        self.signal_processor = SignalProcessor()
        self.added_signals = []
        self.sub_signals = []
        self.main_window = main_window
        self.app = None  # Initialize app as None

    def open_window(self):
        if self.app is not None:
            return
        self.app = tk.Toplevel(self.main_window)
        self.app.title("Task 1&2")

        # Create GUI elements
        self.read_button = tk.Button(self.app, text="Read Signal from File", command=self.read_file_and_display)
        self.generate_button = tk.Button(self.app, text="Generate and Display Signal",
                                         command=self.generate_and_display_signal)

        self.amplitude_label = tk.Label(self.app, text="Amplitude:")
        self.amplitude_entry = tk.Entry(self.app)

        self.analog_freq_label = tk.Label(self.app, text="Analog Frequency:")
        self.analog_freq_entry = tk.Entry(self.app)

        self.sampling_freq_label = tk.Label(self.app, text="Sampling Frequency:")
        self.sampling_freq_entry = tk.Entry(self.app)

        self.phase_shift_label = tk.Label(self.app, text="Phase Shift:")
        self.phase_shift_entry = tk.Entry(self.app)

        self.signal_type = tk.StringVar()
        self.signal_type.set(" ")
        self.sine_radio = tk.Radiobutton(self.app, text="Sine Wave", variable=self.signal_type, value="sin")
        self.cosine_radio = tk.Radiobutton(self.app, text="Cosine Wave", variable=self.signal_type, value="cos")

        self.options = ["", "Add", "Subtract", "Multiply", "Shift", "Normalize", "Square", "Accumulate", ]
        self.combo = ttk.Combobox(self.app, values=self.options)
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.on_select)

        # Add widgets for each option
        self.load_button = tk.Button(self.app, text="Load files", command=self.load_files)
        self.loaded_files_label = tk.Label(self.app,
                                           text="\n".join([item for sublist in self.added_signals for item in sublist]))

        self.file_one_label = tk.Label(self.app, text="File one:")
        self.file_one_button = tk.Button(self.app, text="Select file", command=self.load_file)
        self.file_two_label = tk.Label(self.app, text="File two:")
        self.file_two_button = tk.Button(self.app, text="Select file", command=self.load_file)
        self.select_file_button = tk.Button(self.app, text="Select file", command=lambda: self.load_files(changeFile=0))
        # Create a label as a placeholder
        self.placeholder_label = tk.Label(self.app, text='Enter a number', fg='gray')
        self.number_entry = tk.Entry(self.app, fg='gray')  # Set initial text color to lighter color
        self.number_entry.insert(0, 'Enter a number')
        self.number_entry.bind("<FocusIn>", self.on_entry_click)
        self.number_entry.bind("<FocusOut>", self.on_focus_out)

        self.normalization_frame = tk.Frame(self.app)
        self.selected_option = tk.StringVar()
        self.normalize_label = tk.Label(self.normalization_frame, text="Normalize from:")

        self.normalize_minus_one_radio = tk.Radiobutton(self.normalization_frame, text="-1 to 1", value="-1to1",
                                                        variable=self.selected_option)
        self.normalize_zero_radio = tk.Radiobutton(self.normalization_frame, text="0 to 1", value="0to1",
                                                   variable=self.selected_option)
        self.perform_operation_button = tk.Button(self.app, text="Perform operation", command=self.PerformFunction)

        # Place GUI elements on the grid
        self.normalize_label.grid(row=1, column=3)
        self.normalize_minus_one_radio.grid(row=2, column=3)
        self.normalize_zero_radio.grid(row=3, column=3)
        self.normalization_frame.selection_clear()
        self.read_button.grid(row=0, column=0, columnspan=2)
        self.generate_button.grid(row=1, column=0, columnspan=2)
        self.sine_radio.grid(row=2, column=0)
        self.cosine_radio.grid(row=2, column=1)
        self.amplitude_label.grid(row=3, column=0)
        self.amplitude_entry.grid(row=3, column=1)
        self.analog_freq_label.grid(row=4, column=0)
        self.analog_freq_entry.grid(row=4, column=1)
        self.sampling_freq_label.grid(row=5, column=0)
        self.sampling_freq_entry.grid(row=5, column=1)
        self.phase_shift_label.grid(row=6, column=0)
        self.phase_shift_entry.grid(row=6, column=1)
        self.combo.grid(row=0, column=3)
        self.perform_operation_button.grid(row=3, column=3)

    def close_window(self):
        if self.app:
            self.app.destroy()
            self.app = None

    # Function to read and display a signal from a file
    def read_file_and_display(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.signal_processor.read_signal_from_file(file_path)
        self.signal_processor.display_signal()

    # Function to generate and display a signal based on user input
    def generate_and_display_signal(self):
        try:
            # Extract user input parameters
            signal_type_val = self.signal_type.get()
            amplitude_val = float(self.amplitude_entry.get())
            analog_freq_val = float(self.analog_freq_entry.get())
            sampling_freq_val = float(self.sampling_freq_entry.get())
            phase_shift_val = float(self.phase_shift_entry.get())
            # Generate the signal
            self.signal_processor.generate_signal(
                signal_type_val,
                amplitude_val,
                analog_freq_val,
                sampling_freq_val,
                phase_shift_val,
            )
        except ValueError:
            messagebox.showerror("Missing input", "Please fill all required data.")
            return
        self.signal_processor.display_signal()

        # Print amplitude of the generated signal in the console
        generated_signal = self.signal_processor.signal
        i = 0
        for _, amplitude in generated_signal:
            print(f"{i} {amplitude}")
            i += 1

        # Test generated signals
        if self.signal_type.get() == "sin":
            SignalSamplesAreEqual(
                "data/task1/SinOutput.txt", [sample[1] for sample in generated_signal]
            )
        else:
            SignalSamplesAreEqual(
                "data/task1/CosOutput.txt", [sample[1] for sample in generated_signal]
            )

    # Function to handle event when an operation is selected from the combo box
    def on_select(self, event):
        operation = self.combo.get()

        # Clear the added_signals list
        self.added_signals.clear()

        # Reset the number entry field
        self.number_entry.delete(0, "end")
        self.number_entry.insert(0, "Enter a number")

        self.update_label_text()  # Update the label displaying loaded files

        if operation == "Add":
            # Show button with text "Load files" and a list to show the loaded files names
            self.load_button.grid(row=1, column=3)
            self.loaded_files_label.grid(row=2, column=3)
            self.file_one_label.grid_forget()
            self.file_one_button.grid_forget()
            self.file_two_label.grid_forget()
            self.file_two_button.grid_forget()
            self.select_file_button.grid_forget()
            self.number_entry.grid_forget()
            self.normalization_frame.grid_forget()
        elif operation == "Subtract":
            # Show two labels (file one and file two) with button behind each one
            self.file_one_label.grid(row=1, column=3)
            self.file_one_button.grid(row=1, column=4)
            self.file_two_label.grid(row=2, column=3)
            self.file_two_button.grid(row=2, column=4)
            self.load_button.grid_forget()
            self.loaded_files_label.grid_forget()
            self.select_file_button.grid_forget()
            self.number_entry.grid_forget()
            self.normalization_frame.grid_forget()

        elif operation == "Accumulate":
            # Show only button to select one file
            self.select_file_button.grid(row=1, column=3)
            self.load_button.grid_forget()
            self.loaded_files_label.grid_forget()
            self.file_one_label.grid_forget()
            self.file_one_button.grid_forget()
            self.file_two_label.grid_forget()
            self.file_two_button.grid_forget()
            self.normalization_frame.grid_forget()
            self.number_entry.grid_forget()
        elif operation == "Square":
            # Show only button to select one file
            self.select_file_button.grid(row=1, column=3)
            self.number_entry.grid_forget()
            self.load_button.grid_forget()
            self.loaded_files_label.grid_forget()
            self.file_one_label.grid_forget()
            self.file_one_button.grid_forget()
            self.file_two_label.grid_forget()
            self.file_two_button.grid_forget()
            self.normalization_frame.grid_forget()
        elif operation == "Multiply" or operation == "Shift":
            # Show button to select file and text box to write a number
            self.select_file_button.grid(row=1, column=3)
            self.number_entry.grid(row=2, column=3)
            self.load_button.grid_forget()
            self.loaded_files_label.grid_forget()
            self.file_one_label.grid_forget()
            self.file_one_button.grid_forget()
            self.file_two_label.grid_forget()
            self.file_two_button.grid_forget()
            self.normalization_frame.grid_forget()
        elif operation == "Normalize":
            # Show button to select file and radio button to select
            # whether user want to normalize from -1 to 1 or from 0 to 1
            self.select_file_button.grid(row=1, column=3)
            self.normalization_frame.grid(row=2, column=3)
            self.load_button.grid_forget()
            self.loaded_files_label.grid_forget()
            self.file_one_label.grid_forget()
            self.file_one_button.grid_forget()
            self.file_two_label.grid_forget()
            self.file_two_button.grid_forget()
            self.number_entry.grid_forget()
        else:
            # Hide all operation-specific widgets
            self.select_file_button.grid_forget()
            self.number_entry.grid_forget()
            self.load_button.grid_forget()
            self.loaded_files_label.grid_forget()
            self.file_one_label.grid_forget()
            self.file_one_button.grid_forget()
            self.file_two_label.grid_forget()
            self.file_two_button.grid_forget()
            self.normalization_frame.grid_forget()

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

    # Function to load files for signal processing
    def load_files(self, changeFile=-1):
        root = tk.Tk()
        root.withdraw()  # to hide the main window
        file_paths = filedialog.askopenfilenames(parent=root, title="Choose files")
        if changeFile == -1 or changeFile >= len(self.added_signals):
            self.added_signals.append(list(file_paths))
        else:
            self.added_signals[changeFile] = list(file_paths)
        self.update_label_text()

    def load_file(self):
        root = tk.Tk()
        root.withdraw()  # to hide the main window
        file_path = filedialog.askopenfilename(parent=root, title="Choose file")
        self.sub_signals.append(file_path)

    # Function to update the label text with loaded file paths
    def update_label_text(self):
        self.loaded_files_label.config(
            text="\n".join([item for sublist in self.added_signals for item in sublist])
        )

    # Function to perform the selected signal processing operation
    def PerformFunction(self):
        operation = self.combo.get()
        if operation == "":
            self.signal_processor.display_signal()
            return

        arith_operation = AritmaticOperation()
        output_signal = []
        number_of_files = sum(map(lambda sublist: len(sublist), self.added_signals))

        if operation == "Add":
            if number_of_files < 2:
                messagebox.showerror("Missing input", "Number of added files must be >= 2")
                return

            signals = []
            for signal in self.added_signals:
                for inner_signal in signal:
                    self.signal_processor.read_signal_from_file(inner_signal)
                    signals.append(self.signal_processor.signal)

            output_signal = arith_operation.add(signals)

        elif operation == "Subtract":
            if len(self.sub_signals) < 2:
                messagebox.showerror("Missing input", "Number of selected files must be exactly 2")
                return

            self.signal_processor.read_signal_from_file(self.sub_signals[0])
            first_signal = self.signal_processor.signal
            self.signal_processor.read_signal_from_file(self.sub_signals[1])
            second_signal = self.signal_processor.signal
            output_signal = arith_operation.subtract(first_signal, second_signal)

        elif operation == "Multiply":
            if number_of_files < 1 or self.number_entry.get() == "" or self.number_entry.get() == "Enter a number":
                messagebox.showerror("Missing input", "You must choose one file and enter the multiplication factor", )
                return

            self.signal_processor.read_signal_from_file(self.added_signals[0][0])
            first_signal = self.signal_processor.signal
            output_signal = arith_operation.multiply(first_signal, int(self.number_entry.get()))

        elif operation == "Shift":
            if number_of_files < 1 or self.number_entry.get() == "" or self.number_entry.get() == "Enter a number":
                messagebox.showerror("Missing input", "You must choose one file and enter the shifting factor", )
                return

            self.signal_processor.read_signal_from_file(self.added_signals[0][0])
            first_signal = self.signal_processor.signal
            output_signal = arith_operation.shift(first_signal, -int(self.number_entry.get()))

        elif operation == "Normalize":
            if number_of_files < 1:
                messagebox.showerror("Missing input", "You must choose one file and the normalization range")
                return

            self.signal_processor.read_signal_from_file(self.added_signals[0][0])
            first_signal = self.signal_processor.signal
            factor = (-1, 1) if self.selected_option.get() == "-1to1" else (0, 1)
            output_signal = arith_operation.normalize(first_signal, factor)

        elif operation == "Square":
            if number_of_files < 1:
                messagebox.showerror("Missing input", "You must choose one file")
                return

            self.signal_processor.read_signal_from_file(self.added_signals[0][0])
            first_signal = self.signal_processor.signal
            output_signal = arith_operation.square(first_signal)

        elif operation == "Accumulate":
            if number_of_files < 1:
                messagebox.showerror("Missing input", "You must choose one file")
                return

            self.signal_processor.read_signal_from_file(self.added_signals[0][0])
            first_signal = self.signal_processor.signal
            output_signal = arith_operation.accumulation(first_signal)

        self.signal_processor.set_signal(output_signal)
        self.sub_signals.clear()
        self.added_signals.clear()
        self.signal_processor.display_signal()
