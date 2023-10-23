import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from SignalProcessor import SignalProcessor
from testing import SignalSamplesAreEqual

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
    except:
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


app = tk.Tk()
app.title("Signal Processing")

signal_processor = SignalProcessor()

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
app.mainloop()
