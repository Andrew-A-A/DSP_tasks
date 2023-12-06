import numpy as np
from FourierMagic import dft, idft
from ArethmaticOperations import *

def moving_average(data, window_size):
    half_window = window_size // 2
    smoothed_data = []

    for i in range(len(data)):
        start_index = max(0, i - half_window)
        end_index = min(len(data), i + half_window + 1)

        # Check if the window is within bounds
        if end_index - start_index == window_size:
            window = data[start_index:end_index]
            # Calculate the average of the window
            avg = sum(window) / len(window)
            smoothed_data.append(avg)
        else:
            # If the window extends beyond the edges, use the original value
            smoothed_data.append(data[i])

    return smoothed_data


def smooth_amplitudes(data, window_size):
    result = []

    for item in data:
        index, amplitude = item[0], item[1]

        # Extract the amplitudes for the moving average calculation
        amplitudes = [item[1] for item in data]

        # Calculate the smoothed amplitude using the moving average
        smooth_amplitude = moving_average(amplitudes, window_size)[int(index)]

        result.append([index, smooth_amplitude])

    return result


def sharping(signal):
    first_derivative = []
    second_derivative = []
    for i in range(0, len(signal)):
        x_n = signal[i][1]
        if i == 0:
            x_min_1 = 0
        else:
            x_min_1 = signal[i - 1][1]
        if i == len(signal) - 1:
            x_plus_1 = 0
        else:
            x_plus_1 = signal[i + 1][1]

        first_derivative.append([i, x_n - x_min_1])
        second_derivative.append([i, x_plus_1 - (2 * x_n) + x_min_1])
    return first_derivative, second_derivative


def folding(signal):
    folded_signal = []
    n = len(signal) - 1
    for i in range(0, n + 1):
        folded_signal.append([i, signal[n - i][1]])
    return folded_signal


def remove_dc_frequency_domain(signal):
    df_signal = dft(signal)
    df_signal[0] = [0, 0]
    return idft(df_signal)


def delay_signal(signal, k):
    modified_signal = np.zeros_like(signal)
    for indx in range(len(signal) - k):
        modified_signal[indx + k][1] = signal[indx]

    return modified_signal


def advance_signal(signal, k):
    modified_signal = np.zeros_like(signal)
    for indx in range(k, len(signal)):
        modified_signal[indx - k][1] = signal[indx]

    return modified_signal


def shift_folding(signal, shifting_value):
    shifted = shift(signal, shifting_value)
    first_column, second_column = map(list, zip(*shifted))
    second_column = list(reversed(second_column))
    return first_column, second_column


def convolve(signal1, signal2):
    len_1 = len(signal1)
    len_2 = len(signal2)

    result_indices = []
    result_samples = [0] * (len_1 + len_2 - 1)

    for i in range(len_1):
        for j in range(len_2):
            index_sum = int(signal1[i][0] + signal2[j][0])
            result_samples[index_sum] += signal1[i][1] * signal2[j][1]

            if index_sum not in result_indices:
                result_indices.append(index_sum)

    result_indices.sort()
    result_samples = [result_samples[index] for index in result_indices]

    return result_indices, result_samples