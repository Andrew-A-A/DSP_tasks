import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


# region Testing function
def SignalSamplesAreEqual(file_name, samples):
    expected_indices = []
    expected_samples = []
    with open(file_name, 'r') as f:
        line = f.readline()
        line = f.readline()
        line = f.readline()
        line = f.readline()
        while line:
            # process line
            L = line.strip()
            if len(L.split(' ')) == 2:
                L = line.split(' ')
                V1 = int(L[0])
                V2 = float(L[1])
                expected_indices.append(V1)
                expected_samples.append(V2)
                line = f.readline()
            else:
                break

    if len(expected_samples) != len(samples):
        print("Test case failed, your signal have different length from the expected one")
        return
    for i in range(len(expected_samples)):
        if abs(samples[i] - expected_samples[i]) < 0.01:
            continue
        else:
            print("Test case failed, your signal have different values from the expected one")
            return
    print("Test case passed successfully")


# endregion


# Class that handles signals data
class SignalProcessor:
    # Define variable that will store read/generated signal
    def __init__(self):
        self.signal = []

    def read_signal_from_file(self, filename):
        with open(filename, 'r') as file:
            t = int(file.readline().strip())
            is_periodic = bool(int(file.readline().strip()))
            n_samples = int(file.readline().strip())
            self.signal = []
            for _ in range(n_samples):
                values = file.readline().split()
                index, sample_amp = map(float, values)
                self.signal.append((index, sample_amp))

    def display_signal(self):
        if not self.signal:
            print("No signal data to display.")
            return
        plt.subplot(211)
        x, y = zip(*self.signal)
        plt.plot(x, y)
        plt.xlabel("Time" if self.signal[0][0] == 0 else "Frequency")
        plt.ylabel("Amplitude")

        plt.subplot(212)
        x = [sample[0] for sample in self.signal]
        y = [sample[1] for sample in self.signal]

        markerline, stemlines, baseline = plt.stem(x, y)
        plt.setp(markerline, color='b')
        plt.setp(stemlines, color='b')
        plt.setp(baseline, color='b')

        plt.xlabel("Sample Index" if self.signal[0][0] == 0 else "Frequency")
        plt.ylabel("Amplitude")
        plt.show()

    def generate_signal(self, signalType, amplitude, analog_frequency, sampling_frequency, phase_shift):
        # Check if the sampling theorem satisfied
        if 2 * analog_frequency > sampling_frequency:
            messagebox.showerror(
                "Sampling Frequency Error",
                "The sampling frequency must be at least twice the maximum analog frequency."
            )
            return

        omega = 2 * np.pi * analog_frequency
        t = np.linspace(0, 1, int(sampling_frequency), endpoint=False)
        if signalType == "sin":
            signal = amplitude * np.sin(omega * t + phase_shift)
        else:
            signal = amplitude * np.cos(omega * t + phase_shift)

        self.signal = list(zip(t, signal))


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
        SignalSamplesAreEqual("SinOutput.txt", [sample[1] for sample in generated_signal])
    else:
        SignalSamplesAreEqual("CosOutput.txt", [sample[1] for sample in generated_signal])


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

