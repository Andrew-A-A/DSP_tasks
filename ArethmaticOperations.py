from SignalProcessor import SignalProcessor


# from testing import SignalSamplesAreEqual


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


signals = list()
signal_processor = SignalProcessor()

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
