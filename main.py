import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from ArethmaticOperations import *
from SignalProcessor import SignalProcessor
from testing import SignalSamplesAreEqual
from tkinter import ttk

# Lists for storing signals
added_signals = []

# Function to read and display a signal from a file
def read_file_and_display():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    signal_processor.read_signal_from_file(file_path)
    signal_processor.display_signal()


# Function to generate and display a signal based on user input
def generate_and_display_signal():
    try:
        # Extract user input parameters
        signal_type_val = signal_type.get()
        amplitude_val = float(amplitude_entry.get())
        analog_freq_val = float(analog_freq_entry.get())
        sampling_freq_val = float(sampling_freq_entry.get())
        phase_shift_val = float(phase_shift_entry.get())

        # Generate the signal
        signal_processor.generate_signal(signal_type_val, amplitude_val, analog_freq_val, sampling_freq_val,
                                         phase_shift_val)

    except ValueError:
        messagebox.showerror("Missing input", "Please fill all required data.")
        return

    signal_processor.display_signal()

    # Print amplitude of the generated signal in the console
    generated_signal = signal_processor.signal
    i = 0
    for _, amplitude in generated_signal:
        print(f"{i} {amplitude}")
        i += 1

    # Test generated signals
    if signal_type.get() == "sin":
        SignalSamplesAreEqual("data/task1/SinOutput.txt", [sample[1] for sample in generated_signal])
    else:
        SignalSamplesAreEqual("data/task1/CosOutput.txt", [sample[1] for sample in generated_signal])


# Function to handle event when an operation is selected from the combo box
def on_select(event):
    operation = combo.get()

    # Clear the added_signals list
    added_signals.clear()

    # Reset the number entry field
    number_entry.delete(0, "end")
    number_entry.insert(0, 'Enter a number')

    update_label_text()  # Update the label displaying loaded files

    if operation == "Add":
        # Show button with text "Load files" and a list to show the loaded files names
        load_button.grid(row=1, column=3)
        loaded_files_label.grid(row=2, column=3)
        file_one_label.grid_forget()
        file_one_button.grid_forget()
        file_two_label.grid_forget()
        file_two_button.grid_forget()
        select_file_button.grid_forget()
        number_entry.grid_forget()
        normalization_frame.grid_forget()
    elif operation == "Subtract":
        # Show two labels (file one and file two) with button behind each one
        file_one_label.grid(row=1, column=3)
        file_one_button.grid(row=1, column=4)
        file_two_label.grid(row=2, column=3)
        file_two_button.grid(row=2, column=4)
        load_button.grid_forget()
        loaded_files_label.grid_forget()
        select_file_button.grid_forget()
        number_entry.grid_forget()
        normalization_frame.grid_forget()

    elif operation == "Accumulate":
        # Show only button to select one file
        select_file_button.grid(row=1, column=3)
        load_button.grid_forget()
        loaded_files_label.grid_forget()
        file_one_label.grid_forget()
        file_one_button.grid_forget()
        file_two_label.grid_forget()
        file_two_button.grid_forget()
        normalization_frame.grid_forget()
        number_entry.grid_forget()
    elif operation == "Square":
        # Show only button to select one file
        select_file_button.grid(row=1, column=3)
        number_entry.grid_forget()
        load_button.grid_forget()
        loaded_files_label.grid_forget()
        file_one_label.grid_forget()
        file_one_button.grid_forget()
        file_two_label.grid_forget()
        file_two_button.grid_forget()
        normalization_frame.grid_forget()
    elif operation == "Multiply" or operation == "Shift":
        # Show button to select file and text box to write a number
        select_file_button.grid(row=1, column=3)
        number_entry.grid(row=2, column=3)
        load_button.grid_forget()
        loaded_files_label.grid_forget()
        file_one_label.grid_forget()
        file_one_button.grid_forget()
        file_two_label.grid_forget()
        file_two_button.grid_forget()
        normalization_frame.grid_forget()
    elif operation == "Normalize":
        # Show button to select file and radio button to select
        # whether user want to normalize from -1 to 1 or from 0 to 1
        select_file_button.grid(row=1, column=3)
        normalization_frame.grid(row=2, column=3)
        load_button.grid_forget()
        loaded_files_label.grid_forget()
        file_one_label.grid_forget()
        file_one_button.grid_forget()
        file_two_label.grid_forget()
        file_two_button.grid_forget()
        number_entry.grid_forget()
    else:
        # Hide all operation-specific widgets
        select_file_button.grid_forget()
        number_entry.grid_forget()
        load_button.grid_forget()
        loaded_files_label.grid_forget()
        file_one_label.grid_forget()
        file_one_button.grid_forget()
        file_two_label.grid_forget()
        file_two_button.grid_forget()
        normalization_frame.grid_forget()


# Function to handle entry field click event
def on_entry_click(*arks):
    if number_entry.get() == 'Enter a number':
        number_entry.delete(0, "end")
        number_entry.config(fg="black")  # Change text color to black when typing


# Function to handle entry field focus out event
def on_focus_out(*arks):
    if number_entry.get() == "":
        number_entry.insert(0, 'Enter a number')
        number_entry.config(fg='gray')  # Use the specified lighter color


# Function to load files for signal processing
def load_files(changeFile=-1):
    root = tk.Tk()
    root.withdraw()  # to hide the main window
    file_paths = filedialog.askopenfilenames(parent=root, title='Choose files')
    if changeFile == -1 or changeFile >= len(added_signals):
        added_signals.append(list(file_paths))
    else:
        added_signals[changeFile] = list(file_paths)
    update_label_text()


# Function to update the label text with loaded file paths
def update_label_text():
    loaded_files_label.config(text="\n".join([item for sublist in added_signals for item in sublist]))


# Function to perform the selected signal processing operation
def PerformFunction():
    operation = combo.get()

    if operation == "":
        signal_processor.display_signal()
        return

    arith_operation = AritmaticOperation()
    output_signal = []

    number_of_files = sum(map(lambda sublist: len(sublist), added_signals))

    if operation == "Add":
        if number_of_files < 2:
            messagebox.showerror("Missing input", "Number of added files must be >= 2")
            return

        signals = []
        for signal in added_signals:
            for inner_signal in signal:
                signal_processor.read_signal_from_file(inner_signal)
                signals.append(signal_processor.signal)

        output_signal = arith_operation.add(signals)

    elif operation == "Subtract":
        if number_of_files < 2:
            messagebox.showerror("Missing input", "Number of selected files must be exactly 2")
            return

        signal_processor.read_signal_from_file(added_signals[0][0])
        first_signal = signal_processor.signal
        signal_processor.read_signal_from_file(added_signals[1][0])
        second_signal = signal_processor.signal
        output_signal = arith_operation.subtract(first_signal, second_signal)

    elif operation == "Multiply":
        if number_of_files < 1 or number_entry.get() == '' or number_entry.get() == 'Enter a number':
            messagebox.showerror("Missing input", "You must choose one file and enter the multiplication factor")
            return

        signal_processor.read_signal_from_file(added_signals[0][0])
        first_signal = signal_processor.signal
        output_signal = arith_operation.multiply(first_signal, int(number_entry.get()))

    elif operation == "Shift":
        if number_of_files < 1 or number_entry.get() == '' or number_entry.get() == 'Enter a number':
            messagebox.showerror("Missing input", "You must choose one file and enter the shifting factor")
            return

        signal_processor.read_signal_from_file(added_signals[0][0])
        first_signal = signal_processor.signal
        output_signal = arith_operation.shift(first_signal, int(number_entry.get()))

    elif operation == "Normalize":
        if number_of_files < 1 or False:  # Add condition for selecting normalization range
            messagebox.showerror("Missing input", "You must choose one file and the normalization range")
            return

        signal_processor.read_signal_from_file(added_signals[0][0])
        first_signal = signal_processor.signal
        factor = (-1, 1) if selected_option.get() == "-1to1" else (0, 1)
        output_signal = arith_operation.normalize(first_signal, factor)

    elif operation == "Square":
        if number_of_files < 1:
            messagebox.showerror("Missing input", "You must choose one file")
            return

        signal_processor.read_signal_from_file(added_signals[0][0])
        first_signal = signal_processor.signal
        output_signal = arith_operation.square(first_signal)

    elif operation == "Accumulate":
        if number_of_files < 1:
            messagebox.showerror("Missing input", "You must choose one file")
            return

        signal_processor.read_signal_from_file(added_signals[0][0])
        first_signal = signal_processor.signal
        output_signal = arith_operation.accumulation(first_signal)

    signal_processor.set_signal(output_signal)
    signal_processor.display_signal()


app = tk.Tk()
app.title("Signal Processing")

signal_processor = SignalProcessor()

# region GUI
# Create GUI elements
read_button = tk.Button(app, text="Read Signal from File", command=read_file_and_display)
generate_button = tk.Button(app, text="Generate and Display Signal", command=generate_and_display_signal)

amplitude_label = tk.Label(app, text="Amplitude:")
amplitude_entry = tk.Entry(app)

analog_freq_label = tk.Label(app, text="Analog Frequency:")
analog_freq_entry = tk.Entry(app)

sampling_freq_label = tk.Label(app, text="Sampling Frequency:")
sampling_freq_entry = tk.Entry(app)

phase_shift_label = tk.Label(app, text="Phase Shift:")
phase_shift_entry = tk.Entry(app)

signal_type = tk.StringVar()
signal_type.set(" ")
sine_radio = tk.Radiobutton(app, text="Sine Wave", variable=signal_type, value="sin")
cosine_radio = tk.Radiobutton(app, text="Cosine Wave", variable=signal_type, value="cos")

options = ["", "Add", "Subtract", "Multiply", "Shift", "Normalize", "Square", "Accumulate", ]
combo = ttk.Combobox(app, values=options)
combo.current(0)
combo.bind("<<ComboboxSelected>>", on_select)

# Add widgets for each option
load_button = tk.Button(app, text="Load files", command=load_files)
loaded_files_label = tk.Label(app, text="\n".join([item for sublist in added_signals for item in sublist]))

file_one_label = tk.Label(app, text="File one:")
file_one_button = tk.Button(app, text="Select file", command=lambda: load_files(changeFile=0))
file_two_label = tk.Label(app, text="File two:")
file_two_button = tk.Button(app, text="Select file", command=lambda: load_files(changeFile=1))
select_file_button = tk.Button(app, text="Select file", command=lambda: load_files(changeFile=0))
# Create a label as a placeholder
placeholder_label = tk.Label(app, text='Enter a number', fg='gray')
number_entry = tk.Entry(app, fg='gray')  # Set initial text color to lighter color
number_entry.insert(0, 'Enter a number')
number_entry.bind("<FocusIn>", on_entry_click)
number_entry.bind("<FocusOut>", on_focus_out)

normalization_frame = tk.Frame(app)
selected_option = tk.StringVar()
normalize_label = tk.Label(normalization_frame, text="Normalize from:")

normalize_minus_one_radio = tk.Radiobutton(normalization_frame, text="-1 to 1", value="-1to1", variable=selected_option)
normalize_zero_radio = tk.Radiobutton(normalization_frame, text="0 to 1", value="0to1", variable=selected_option)
perform_operation_button = tk.Button(app, text="Perform operation", command=PerformFunction)


# Place GUI elements on the grid
normalize_label.grid(row=1, column=3)
normalize_minus_one_radio.grid(row=2, column=3)
normalize_zero_radio.grid(row=3, column=3)
normalization_frame.selection_clear()
read_button.grid(row=0, column=0, columnspan=2)
generate_button.grid(row=1, column=0, columnspan=2)
sine_radio.grid(row=2, column=0)
cosine_radio.grid(row=2, column=1)
amplitude_label.grid(row=3, column=0)
amplitude_entry.grid(row=3, column=1)
analog_freq_label.grid(row=4, column=0)
analog_freq_entry.grid(row=4, column=1)
sampling_freq_label.grid(row=5, column=0)
sampling_freq_entry.grid(row=5, column=1)
phase_shift_label.grid(row=6, column=0)
phase_shift_entry.grid(row=6, column=1)
combo.grid(row=0, column=3)
perform_operation_button.grid(row=3, column=3)
app.mainloop()
# endregion
