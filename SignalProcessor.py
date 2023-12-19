from tkinter import messagebox
import numpy as np
from matplotlib import pyplot as plt


# Define a class for signal processing
class SignalProcessor:
    # Define variable that will store read/generated signal
    def __init__(self):
        self.signal = []

    # Set the signal with provided values
    def set_signal(self, signal):
        self.signal = signal

    # Read signal data from a file and populate the signal variable
    def read_signal_from_file(self, filename):
        with open(filename, "r") as file:
            # Read metadata from the file
            t = int(file.readline().strip())
            is_periodic = bool(int(file.readline().strip()))
            n_samples = int(file.readline().strip())
            self.signal = []

            # Read samples from the file based on whether the signal is periodic or not
            if is_periodic:
                for _ in range(n_samples):
                    values = file.readline().replace(",", " ").split()
                    values[0] = values[0].replace("f", "")
                    values[1] = values[1].replace("f", "")
                    amplitude, phase_shift = map(float, values)
                    self.signal.append([amplitude, phase_shift])
            else:
                for _ in range(n_samples):
                    values = file.readline().split()
                    index, sample_amp = map(float, values)
                    self.signal.append([index, sample_amp])

        return self.signal

    # Display the signal using matplotlib
    def display_signal(self, discrete=True, continuous=True):
        if not self.signal:
            print("No signal data to display.")
            return
        if not continuous:
            # Display discrete signal using stem plot
            plt.plot()
            x = [sample[0] for sample in self.signal]
            y = [sample[1] for sample in self.signal]
            markerline, stemlines, baseline = plt.stem(x, y)
            plt.setp(markerline, color="r")
            plt.setp(stemlines, color="b")
            plt.setp(baseline, color="y")
            plt.xlabel("Sample Index" if self.signal[0][0] == 0 else "Frequency")
            plt.ylabel("Amplitude")
            plt.show()
        elif not discrete:
            # Display continuous signal
            plt.subplot()
            x, y = zip(*self.signal)
            plt.plot(x, y)
            plt.xlabel("Time" if self.signal[0][0] == 0 else "Frequency")
            plt.ylabel("Amplitude")
            plt.show()
        else:
            # Display both continuous and discrete signals
            plt.subplot(211)
            x, y = zip(*self.signal)
            plt.plot(x, y)
            plt.xlabel("Time" if self.signal[0][0] == 0 else "Frequency")
            plt.ylabel("Amplitude")

            plt.subplot(212)
            x = [sample[0] for sample in self.signal]
            y = [sample[1] for sample in self.signal]
            markerline, stemlines, baseline = plt.stem(x, y)
            plt.setp(markerline, color="b")
            plt.setp(stemlines, color="b")
            plt.setp(baseline, color="b")
            plt.xlabel("Sample Index" if self.signal[0][0] == 0 else "Frequency")
            plt.ylabel("Amplitude")
            plt.show()

    # Generate a signal based on given parameters
    def generate_signal(
            self, signalType, amplitude, analog_frequency, sampling_frequency, phase_shift):
        # Check if the sampling theorem is satisfied
        if 2 * analog_frequency > sampling_frequency:
            messagebox.showerror(
                "Sampling Frequency Error",
                "The sampling frequency must be at least twice the maximum analog frequency.",
            )
            return

        # Calculate angular frequency
        omega = 2 * np.pi * analog_frequency
        # Generate time values
        t = np.linspace(0, 1, int(sampling_frequency), endpoint=False)

        # Generate the signal based on the selected signal type
        if signalType == "sin":
            signal = amplitude * np.sin(omega * t + phase_shift)
        else:
            signal = amplitude * np.cos(omega * t + phase_shift)

        self.signal = list(zip(t, signal))
