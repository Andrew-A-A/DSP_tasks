import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from ArethmaticOperations import *
from SignalProcessor import SignalProcessor
from testing import SignalSamplesAreEqual
from tkinter import ttk

added_signals = []
sub_signals = []


def read_file_and_display():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    signal_processor.read_signal_from_file(file_path)
    signal_processor.display_signal()


def generate_and_display_signal():
    try:
        signal_processor.generate_signal(
            signal_type.get(),
            float(amplitude_entry.get()),
            float(analog_freq_entry.get()),
            float(sampling_freq_entry.get()),
            float(phase_shift_entry.get()),
        )
    except ValueError:
        messagebox.showerror(
            "Missing input",
            "Please fill all data required \n(Signal type,Amplitude,Analog Frequency,Sampling "
            "frequency and phase shift)"
        )
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


def on_select(event):
    selection = event.widget.get()
    if selection == "add":
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
    elif selection == "Subtract":
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

    elif selection == "Accumulate":
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
    elif selection == "Square":
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
    elif selection == "Multiply":
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
    elif selection == "Shift":
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
    elif selection == "Normalized":
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
        select_file_button.grid_forget()
        number_entry.grid_forget()
        load_button.grid_forget()
        loaded_files_label.grid_forget()
        file_one_label.grid_forget()
        file_one_button.grid_forget()
        file_two_label.grid_forget()
        file_two_button.grid_forget()
        normalization_frame.grid_forget()


def load_files():
    root = tk.Tk()
    root.withdraw()  # to hide the main window
    file_paths = filedialog.askopenfilenames(parent=root, title='Choose files')
    if len(file_paths) < 2:
        messagebox.showerror(
            "Missing input",
            "Please select at least two files to be added"
        )
        return
    signals = []
    for signal in file_paths:
        signal_processor.read_signal_from_file(signal)
        signals.append(signal_processor.signal)
    added_signals.append(list(file_paths))
    update_label_text()
    signal_processor.signal = add(signals)
    return signals


def load_file(num):
    root = tk.Tk()
    root.withdraw()  # to hide the main window
    file_path = filedialog.askopenfilename(parent=root, title='Choose files')
    if len(file_path) < 1:
        messagebox.showerror(
            "Missing input",
            "Please select file"
        )
        return
    signal_processor.read_signal_from_file(file_path)
    if num == 0:
        sub_signals.append(signal_processor.signal)
        return
    else:
        sub_signals.append(signal_processor.signal)
        signal_processor.signal = subtract(sub_signals[0], sub_signals[1])
        return signal_processor.signal


def update_label_text():
    loaded_files_label.config(text="\n".join([item for sublist in added_signals for item in sublist]))


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

options = ["", "add", "Subtract", "Multiply", "Shift", "Normalized", "Square", "Accumulate", ]
combo = ttk.Combobox(app, values=options)
combo.current(0)
combo.bind("<<ComboboxSelected>>", on_select)

# Add widgets for each option
load_button = tk.Button(app, text="Load files", command=load_files)
loaded_files_label = tk.Label(app, text="\n".join([item for sublist in added_signals for item in sublist]))

file_one_label = tk.Label(app, text="File one:")
file_one_button = tk.Button(app, text="Select file", command=lambda: load_file(0))
file_two_label = tk.Label(app, text="File two:")
file_two_button = tk.Button(app, text="Select file", command=lambda: load_file(1))
select_file_button = tk.Button(app, text="Select file")
number_entry = tk.Entry(app)
normalization_frame = tk.Frame(app)
normalize_label = tk.Label(normalization_frame, text="Normalize from:")
normalize_minus_one_radio = tk.Radiobutton(normalization_frame, text="-1 to 1", value="-1to1")
normalize_zero_radio = tk.Radiobutton(normalization_frame, text="0 to 1", value="0to1")
normalize_label.grid(row=1, column=3)
normalize_minus_one_radio.grid(row=2, column=3)
normalize_zero_radio.grid(row=3, column=3)
normalization_frame.selection_clear()

perform_operation_button = tk.Button(app, text="Perform operation", command=signal_processor.display_signal)

# Place GUI elements on the grid
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
