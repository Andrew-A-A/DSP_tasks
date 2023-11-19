import math


def dct(signals):
    # y(k)=√2/N * ∑ x(n) * cos( pi / 4N ) * (2n - 1 ) * (2k - 1))
    signal_DCT = [0] * len(signals)
    for k, x_k in enumerate(signal_DCT):
        tmp = 0
        for n, x_n in signals:
            tmp += x_n * math.cos((math.pi / (4 * len(signals))) * (2 * n - 1) * (2 * k - 1))
        signal_DCT[k] = math.sqrt(2 / len(signals)) * tmp
    return signal_DCT


def remove_dc(signal):
    summation = 0
    signal_dc_removed = []
    for n, x_n in signal:
        summation += x_n
    mean = summation / len(signal)

    for n, x_n in signal:
        signal_dc_removed.append(round(x_n - mean, 3))
    return signal_dc_removed


