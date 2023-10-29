import math


def quantize(signal, levels_num=-1, bits_num=-1):
    intervals = []
    intervals_mid = []
    quantized_signal = []
    q_bits = bits_num

    # Check if the number of levels is given or number of bits
    if levels_num == -1:
        levels_num = pow(2, bits_num)
    else:
        q_bits = int(math.log2(levels_num))

    # Find max & min amplitudes
    max_amp = max([val[1] for val in signal])
    min_amp = min([val[1] for val in signal])

    # Find delta ( max-min / #levels )
    delta = (max_amp - min_amp) / levels_num

    # Make ranges which equal to levels (add delta)
    i = min_amp
    while i < max_amp:
        # Make ranges
        intervals.append([round(i, 4), round(i + delta, 4)])
        i += delta

    # Calculate midpoint to each range
    for interval_min, interval_max in intervals:
        intervals_mid.append(round((interval_min + interval_max) / 2, 4))

    # Quantize & Calculate Quantization error (Quantized_Amp - Amp)
    for _, value in signal:
        for index, (interval_min, interval_max) in enumerate(intervals):
            # Assign each signal to it's interval
            if interval_min <= value <= interval_max:
                # Encode
                encoded_val = format(index, f'0{q_bits}b')

                # Add quantized sample
                if bits_num == -1:
                    # Calculate error
                    quantization_error = round(intervals_mid[index] - value, 4)
                    quantized_signal.append([index + 1, encoded_val, intervals_mid[index], quantization_error])
                else:
                    quantized_signal.append([encoded_val, intervals_mid[index]])
                break
    return quantized_signal
