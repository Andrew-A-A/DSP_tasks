import cmath
import math

import numpy as np

from FourierMagic import dft, idft
from SignalProcessor import SignalProcessor


# TODO Fix Convolution or implement new one
def fastConvolution(signal1, signal2):
    l1 = len(signal1)
    l2 = len(signal2)

    for i in range(l2 - 1):
        signal1.append([l1 + i, 0])
    for i in range(l1 - 1):
        signal2.append([l2 + i, 0])

    # Compute the Discrete Fourier Transform (DFT) of signal1 and signal2
    f1 = dft(signal1)
    f2 = dft(signal2)

    # Convert amplitude and phase to rectangular form for signal1
    for i in range(len(f1)):
        A = f1[i][0]
        phase = f1[i][1]
        signal1[i] = [i, cmath.rect(A, phase)]

    # Convert amplitude and phase to rectangular form for signal2
    for i in range(len(f2)):
        A = f2[i][0]
        phase = f2[i][1]
        signal2[i] = [i, cmath.rect(A, phase)]

    # Compute the cross-correlation in the frequency domain
    cross_correlation_freq = np.multiply([val[1] for val in signal1], [val[1] for val in signal2])
    # Convert the cross-correlation to amplitude and phase
    tmp = []
    for s in cross_correlation_freq:
        amps = abs(s)
        phases = cmath.phase(s)
        tmp.append([amps, phases])

    # Compute the Inverse Discrete Fourier Transform (IDFT) to get the cross-correlation in time domain
    cross_correlation_time = idft(tmp)

    # Return the indices and the normalized cross-correlation signal
    return [s[0] for s in cross_correlation_time], [val[1] for val in cross_correlation_time]


def fastCorrelation(signal1, signal2):
    # Compute the Discrete Fourier Transform (DFT) of signal1 and signal2
    f1 = dft(signal1)
    f2 = dft(signal2)

    # Convert amplitude and phase to rectangular form for signal1
    for i in range(len(f1)):
        A = f1[i][0]
        phase = f1[i][1]
        signal1[i] = [i, cmath.rect(A, phase)]

    # Convert amplitude and phase to rectangular form for signal2
    for i in range(len(f2)):
        A = f2[i][0]
        phase = f2[i][1]
        signal2[i] = [i, cmath.rect(A, phase)]

    # Compute the cross-correlation in the frequency domain
    cross_correlation_freq = np.conjugate([val[1] for val in signal1]) * [val[1] for val in signal2]

    # Convert the cross-correlation to amplitude and phase
    tmp = []
    for s in cross_correlation_freq:
        amps = abs(s)
        phases = cmath.phase(s)
        tmp.append([amps, phases])

    # Compute the Inverse Discrete Fourier Transform (IDFT) to get the cross-correlation in time domain
    cross_correlation_time = idft(tmp)

    # Normalize the cross-correlation
    normalizedSignal = [(1 / len(cross_correlation_time)) * s[1] for s in cross_correlation_time]

    # Return the indices and the normalized cross-correlation signal
    return [round(s[0], 3) for s in cross_correlation_time], normalizedSignal
