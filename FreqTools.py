import math


def dct(signal):
    # y(k) = √(2/N) * ∑ x(n) * cos( (pi / 4N ) * (2n - 1 ) * (2k - 1))
    signal_DCT = [0] * len(signal)
    for k, x_k in enumerate(signal_DCT):
        tmp = 0
        for n, x_n in signal:
            tmp += x_n * math.cos(
                (math.pi / (4 * len(signal))) * (2 * n - 1) * (2 * k - 1)
            )
        signal_DCT[k] = math.sqrt(2 / len(signal)) * tmp
    return signal_DCT


def remove_dc(signal):
    # x(k) = x(n) - mean
    summation = 0
    signal_dc_removed = []
    for n, x_n in signal:
        summation += x_n
    mean = summation / len(signal)
    for n, x_n in signal:
        signal_dc_removed.append(round(x_n - mean, 3))
    return signal_dc_removed
