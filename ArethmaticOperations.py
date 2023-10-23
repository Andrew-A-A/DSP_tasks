from SignalProcessor import SignalProcessor
from testing import SignalSamplesAreEqual


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
        total[i][1] = abs(total[i][1] - val)
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
    result = [[inner_list[0], (inner_list[1] - Min) * scaling_factor + range[0]] for inner_list in signal]

    return result


def accumulation(signal):
    y = signal
    for k in range(1, len(signal)):
        y[k][0] = y[k - 1][0] + signal[k][0]
        y[k][1] = y[k - 1][1] + signal[k][1]
    return y


def testAdd():
    print("Test Add:")
    signals = list()
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
    signals.append(signal_processor.signal)
    signal_processor.read_signal_from_file("data/task2/input signals/Signal2.txt")
    signals.append(signal_processor.signal)
    added = add(signals)
    SignalSamplesAreEqual("data/task2/output signals/Signal1+signal2.txt", [val[1] for val in added])

    signals = list()
    signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
    signals.append(signal_processor.signal)
    signal_processor.read_signal_from_file("data/task2/input signals/Signal3.txt")
    signals.append(signal_processor.signal)
    added = add(signals)
    SignalSamplesAreEqual("data/task2/output signals/Signal1+signal3.txt", [val[1] for val in added])


def testSubtract():
    signal_processor = SignalProcessor()
    print("Test Subtract:")
    signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
    signal1 = signal_processor.signal
    signal_processor.read_signal_from_file("data/task2/input signals/Signal2.txt")
    signal2 = signal_processor.signal
    subtracted = subtract(signal1, signal2)
    SignalSamplesAreEqual("data/task2/output signals/signal1-signal2.txt", [val[1] for val in subtracted])

    signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
    signal1 = signal_processor.signal
    signal_processor.read_signal_from_file("data/task2/input signals/Signal3.txt")
    signal2 = signal_processor.signal
    subtracted = subtract(signal1, signal2)
    SignalSamplesAreEqual("data/task2/output signals/signal1-signal3.txt", [val[1] for val in subtracted])


def testMultiply():
    print("Test Multiply:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
    signal1 = signal_processor.signal
    multi = multiply(signal1, 5)
    SignalSamplesAreEqual("data/task2/output signals/MultiplySignalByConstant-Signal1 - by 5.txt",
                          [val[1] for val in multi])

    signal_processor.read_signal_from_file("data/task2/input signals/Signal2.txt")
    signal2 = signal_processor.signal
    multi = multiply(signal2, 10)
    SignalSamplesAreEqual("data/task2/output signals/MultiplySignalByConstant-Signal2 - by 10.txt",
                          [val[1] for val in multi])


def testSquare():
    print("Test Square:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
    signal1 = signal_processor.signal
    sq = square(signal1)
    SignalSamplesAreEqual("data/task2/output signals/Output squaring signal 1.txt", [val[1] for val in sq])


def testShift():
    print("Test Shift:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("data/task2/input signals/Input Shifting.txt")
    Input1 = signal_processor.signal
    shifted1 = shift(Input1, 500)
    shifted2 = shift(Input1, -500)
    SignalSamplesAreEqual("data/task2/output signals/output shifting by add 500.txt", [val[1] for val in shifted1])
    SignalSamplesAreEqual("data/task2/output signals/output shifting by minus 500.txt", [val[1] for val in shifted2])


def testNormalize():
    print("Test Normalize:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
    Input1 = signal_processor.signal
    signal_processor.read_signal_from_file("data/task2/input signals/Signal2.txt")
    Input2 = signal_processor.signal
    normalized1 = normalize(Input1, (-1, 1))
    normalized2 = normalize(Input2, (0, 1))
    SignalSamplesAreEqual("data/task2/output signals/normalize of signal 1 -- output.txt",
                          [val[1] for val in normalized1])
    SignalSamplesAreEqual("data/task2/output signals/normlize signal 2 -- output.txt", [val[1] for val in normalized2])


def testAccumulate():
    print("Test Accumulate:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
    Input1 = signal_processor.signal
    accumulated = accumulation(Input1)
    SignalSamplesAreEqual("data/task2/output signals/output accumulation for signal1.txt",
                          [val[1] for val in accumulated])


testAdd()
testSubtract()
testMultiply()
testSquare()
testShift()
testNormalize()
testAccumulate()
