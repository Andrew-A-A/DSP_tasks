import numpy as np

from FourierMagic import *


def normalizedCrossCorrelation(signal1, signal2):
    # Compute the Discrete Fourier Transform (DFT) of signal1 and signal2
    f1 = dft(signal1)
    f2 = dft(signal2)

    # Initialize lists to store indices, squared values for signal1 and signal2
    x1_indices = []
    x1Squared = []
    x2Squared = []

    # Compute the squared values and indices for each element in signal1 and signal2
    for i in range(len(signal1)):
        x1_indices.append(i)
        x1Squared.append(signal1[i][1] ** 2)
        x2Squared.append(signal2[i][1] ** 2)

    # Calculate the sum of squared values for signal1 and signal2
    x1sqrSum = np.sum(x1Squared)
    x2sqrSum = np.sum(x2Squared)

    # Compute p12, the normalization factor
    p12 = (1 / len(x1_indices)) * (math.sqrt(x1sqrSum * x2sqrSum))

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
    normalizedSignal = [(1 / len(cross_correlation_time)) * s[1] / p12 for s in cross_correlation_time]

    # Return the indices and the normalized cross-correlation signal
    return [s[0] for s in cross_correlation_time], normalizedSignal




