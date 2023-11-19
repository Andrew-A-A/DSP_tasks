import cmath
import math


def dft(signal_in_time_domain):
    # arguments: one signal
    # return: [[amp, phase shift]]
    signals_in_freq_domain = convert_to_frequency_domain(signal_in_time_domain)
    amp_shift = []
    for signal in signals_in_freq_domain:
        # Amplitude = sqrt (real number^2 + coefficient of imaginary number ^ 2)
        amplitude = abs(signal)
        # Phase shift = inverse tan (coefficient of imaginary number / real number)
        phase_shift = cmath.phase(signal)
        amp_shift.append([amplitude, phase_shift])
    return amp_shift


def idft(signals_in_frequency_domain):
    # arguments: [[amp, phase shift]]
    # return: signal
    signals_in_time_domain = convert_to_time_domain(signals_in_frequency_domain)
    reconstructed_signal = []
    for i in range(len(signals_in_time_domain)):
        reconstructed_signal.append([i, signals_in_time_domain[i]])
    return reconstructed_signal


def convert_to_frequency_domain(signals):
    # x(k)= 0, n-1 ∑ x(n) * e^(( -J * 2 * pi * k * n )/N)
    signals_in_freq_domain = [0] * len(signals)
    for k, x_k in enumerate(signals_in_freq_domain):
        tmp = 0
        for n, x_n in signals:
            tmp += x_n * cmath.exp(-2j * math.pi * k * n / len(signals))
        signals_in_freq_domain[k] = tmp
    return signals_in_freq_domain


def convert_to_time_domain(signals):
    # Convert amplitude and phase shift to signal in frequency domain X(k)
    # X(k) = A Cos θ + J sin θ
    for i in range(len(signals)):
        A = signals[i][0]
        phase = signals[i][1]
        signals[i] = [i, cmath.rect(A, phase)]
    # Initialize signal in a time domain list
    signals_in_time_domain = [0] * len(signals)
    # Convert frequency domain to time domain
    for n, x_n in enumerate(signals_in_time_domain):
        tmp = 0
        # Calculate X(n)= 1/N ∑ x(k) * e^(( J * 2 * pi * k * n )/N)
        for k, x_k in signals:
            tmp += x_k * cmath.exp(2j * math.pi * k * n / len(signals))
        signals_in_time_domain[n] = tmp.real.__round__(3) / len(signals)
    return signals_in_time_domain


# Function creates two lists for plotting (Frequency V.S Amplitude) (Frequency V.S Phase shift)
def sketch(amp_shift: list, sampling_frequency):
    # arguments: [[amp, phase shift]], int
    # return [[frequency, amp]], [[frequency, phase shift]]
    sampling_time = 1 / sampling_frequency
    omega = (2 * math.pi) / sampling_time * len(amp_shift)
    frequency_verse_amplitude = []
    frequency_verse_phase = []
    for i in range(len(amp_shift)):
        amplitude = amp_shift[i][0]
        phase_shift = amp_shift[i][1]
        frequency_verse_amplitude.append([omega * (i + 1), amplitude])
        frequency_verse_phase.append([omega * (i + 1), phase_shift])
    return frequency_verse_amplitude, frequency_verse_phase
