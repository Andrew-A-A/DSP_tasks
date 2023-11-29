def add(signals_to_add):
    total = signals_to_add[0]
    for signal in signals_to_add[1:]:
        i = 0
        for index, val in signal:
            total[i][1] += val
            i += 1

    return total


def subtract(signal1, signal2):
    i = 0
    total = signal1
    for index, val in signal2:
        total[i][1] = val - total[i][1]
        i += 1
    return total


def multiply(signal, value):
    i = 0
    total = signal
    for _, _ in total:
        total[i][1] *= value
        i += 1
    return total


def square(signal):
    i = 0
    total = signal
    for _, value in total:
        total[i][1] *= value
        i += 1
    return total


def shift(signal, unit):
    ret = signal
    for indx in range(len(ret)):
        ret[indx][0] += unit
    return ret


def normalize(signal, range):
    Min = min([inner_list[1] for inner_list in signal])
    Max = max([inner_list[1] for inner_list in signal])
    scaling_factor = (range[1] - range[0]) / (Max - Min)
    result = [
        [inner_list[0], (inner_list[1] - Min) * scaling_factor + range[0]]
        for inner_list in signal
    ]

    return result


def accumulation(signal):
    y = signal
    for k in range(1, len(signal)):
        y[k][0] = y[k - 1][0] + signal[k][0]
        y[k][1] = y[k - 1][1] + signal[k][1]
    return y
