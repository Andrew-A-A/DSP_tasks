def add(signals_to_add):
    i = 0
    total = signals_to_add[0]
    for signal in signals_to_add[1:]:
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

# signals = list()
# signal_processor = SignalProcessor()
#
# print("Test Add:")
# signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
# signals.append(signal_processor.signal)
# signal_processor.read_signal_from_file("data/task2/input signals/Signal2.txt")
# signals.append(signal_processor.signal)
# added = add(signals)
# SignalSamplesAreEqual("data/task2/output signals/Signal1+signal2.txt", [val[1] for val in added])
#
# signals = list()
# signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
# signals.append(signal_processor.signal)
# signal_processor.read_signal_from_file("data/task2/input signals/Signal3.txt")
# signals.append(signal_processor.signal)
# added = add(signals)
# SignalSamplesAreEqual("data/task2/output signals/Signal1+signal3.txt", [val[1] for val in added])
#
#
# print("Test Subtract:")
# signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
# signal1 = signal_processor.signal
# signal_processor.read_signal_from_file("data/task2/input signals/Signal2.txt")
# signal2 = signal_processor.signal
# subtracted = subtract(signal1, signal2)
# SignalSamplesAreEqual("data/task2/output signals/signal1-signal2.txt", [val[1] for val in subtracted])
#
#
# signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
# signal1 = signal_processor.signal
# signal_processor.read_signal_from_file("data/task2/input signals/Signal3.txt")
# signal2 = signal_processor.signal
# subtracted = subtract(signal1, signal2)
# SignalSamplesAreEqual("data/task2/output signals/signal1-signal3.txt", [val[1] for val in subtracted])
#
# print("Test Multiply:")
# signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
# signal1 = signal_processor.signal
# multi = multiply(signal1, 5)
# SignalSamplesAreEqual("data/task2/output signals/MultiplySignalByConstant-Signal1 - by 5.txt", [val[1] for val in multi])
#
# signal_processor.read_signal_from_file("data/task2/input signals/Signal2.txt")
# signal2 = signal_processor.signal
# multi = multiply(signal2, 10)
# SignalSamplesAreEqual("data/task2/output signals/MultiplySignalByConstant-Signal2 - by 10.txt", [val[1] for val in multi])
#
# print("Test Square:")
# signal_processor.read_signal_from_file("data/task2/input signals/Signal1.txt")
# signal1 = signal_processor.signal
# sq = square(signal1)
# SignalSamplesAreEqual("data/task2/output signals/Output squaring signal 1.txt", [val[1] for val in sq])
