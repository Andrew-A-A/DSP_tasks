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

        result.append([index , smooth_amplitude])

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


