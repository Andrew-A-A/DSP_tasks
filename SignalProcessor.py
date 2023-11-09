from tkinter import messagebox
import numpy as np
from matplotlib import pyplot as plt


class SignalProcessor:
    # Define variable that will store read/generated signal
    def __init__(self):
        self.signal = []

    def set_signal(self, signal):
        self.signal = signal

    def read_signal_from_file(self, filename):
        with open(filename, "r") as file:
            t = int(file.readline().strip())
            is_periodic = bool(int(file.readline().strip()))
            n_samples = int(file.readline().strip())
            self.signal = []
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

    def display_signal(self, discrete=True, continuous=True):
        if not self.signal:
            print("No signal data to display.")
            return
        if not continuous:
            plt.plot()
            x = [sample[0] for sample in self.signal]
            y = [sample[1] for sample in self.signal]
            markerline, stemlines, baseline = plt.stem(x, y)
            plt.setp(markerline, color="b")
            plt.setp(stemlines, color="b")
            plt.setp(baseline, color="b")

            plt.xlabel("Sample Index" if self.signal[0][0] == 0 else "Frequency")
            plt.ylabel("Amplitude")
            plt.show()
        elif not discrete:
            plt.subplot()
            x, y = zip(*self.signal)
            plt.plot(x, y)
            plt.xlabel("Time" if self.signal[0][0] == 0 else "Frequency")
            plt.ylabel("Amplitude")
            plt.show()
        else:
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

    def generate_signal(
        self, signalType, amplitude, analog_frequency, sampling_frequency, phase_shift
    ):
        # Check if the sampling theorem satisfied
        if 2 * analog_frequency > sampling_frequency:
            messagebox.showerror(
                "Sampling Frequency Error",
                "The sampling frequency must be at least twice the maximum analog frequency.",
            )
            return

        omega = 2 * np.pi * analog_frequency
        t = np.linspace(0, 1, int(sampling_frequency), endpoint=False)
        if signalType == "sin":
            signal = amplitude * np.sin(omega * t + phase_shift)
        else:
            signal = amplitude * np.cos(omega * t + phase_shift)

        self.signal = list(zip(t, signal))
