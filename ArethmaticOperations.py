def add(signals_to_add):
    # Initialize the total with the first signal
    total = signals_to_add[0]

    # Iterate over the remaining signals and add their values to the total
    for signal in signals_to_add[1:]:
        i = 0
        for index, val in signal:
            total[i][1] += val
            i += 1

    return total


def subtract(signal1, signal2):
    # Initialize the total with the first signal
    total = signal1

    # Iterate over the values of the second signal and subtract them from the total
    i = 0
    for index, val in signal2:
        total[i][1] = val - total[i][1]
        i += 1
    return total


def multiply(signal, value):
    # Multiply each value in the signal by the given value
    i = 0
    total = signal
    for _, _ in total:
        total[i][1] *= value
        i += 1
    return total


def square(signal):
    # Square each value in the signal
    i = 0
    total = signal
    for _, value in total:
        total[i][1] *= value
        i += 1
    return total


def shift(signal, unit):
    # Shift the time values of the signal by the given unit
    ret = signal
    for index in range(len(ret)):
        ret[index][0] += unit
    return ret


def normalize(signal, Range):
    # Normalize the amplitudes of the signal to the specified range
    Min = min([inner_list[1] for inner_list in signal])
    Max = max([inner_list[1] for inner_list in signal])
    scaling_factor = (Range[1] - Range[0]) / (Max - Min)
    result = [
        [inner_list[0], (inner_list[1] - Min) * scaling_factor + Range[0]]
        for inner_list in signal
    ]

    return result


def accumulation(signal):
    # Compute the cumulative sum of the signal values
    y = signal
    for k in range(1, len(signal)):
        y[k][0] = y[k - 1][0] + signal[k][0]
        y[k][1] = y[k - 1][1] + signal[k][1]
    return y
