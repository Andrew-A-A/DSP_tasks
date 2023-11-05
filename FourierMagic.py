# Convert time domain to frequency domain
# x(k)= 0, n-1 ∑ x(n) * e^(( -J * 2 * pi * k * n )/N)
# e^(-J * θ)= cos(θ) - J sin(θ)

# Sketch
# Amplitude =sqrt (real number^2 + coefficient of imaginary number ^ 2)
# Phase shift = inverse tan (coefficient of imaginary number ^ 2/ real number ^ 2)

import cmath
import math

from SignalProcessor import SignalProcessor


def idf(signals_in_time_domain, sampling_frequency):
    signals_in_freq_domain = convert_to_frequency_domain(signals_in_time_domain)
    amp_shift = []
    for signal in signals_in_freq_domain:
        amplitude = abs(signal)
        phase_shift = cmath.phase(signal)
        amp_shift.append([amplitude, phase_shift])
    return amp_shift


def convert_to_frequency_domain(signals):
    signals_in_freq_domain = [0] * len(signals)
    for k, x_k in enumerate(signals_in_freq_domain):
        tmp = 0
        for n, x_n in signals:
            tmp += x_n * cmath.exp(-2j * math.pi * k * n / len(signals))
        signals_in_freq_domain[k] = tmp
    return signals_in_freq_domain


signal_processor = SignalProcessor()
signal_processor.read_signal_from_file("data/task4/DFT/input_Signal_DFT.txt")

idf(signal_processor.signal, 4)
