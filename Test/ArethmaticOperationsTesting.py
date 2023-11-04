from ArethmaticOperations import AritmaticOperation
from SignalProcessor import SignalProcessor
from testing import SignalSamplesAreEqual

operation = AritmaticOperation()


def testAdd():
    print("Test Add:")
    signals = list()
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal1.txt")
    signals.append(signal_processor.signal)
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal2.txt")
    signals.append(signal_processor.signal)
    added = operation.add(signals)
    SignalSamplesAreEqual("../data/task2/output signals/Signal1+signal2.txt", [val[1] for val in added])

    signals = list()
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal1.txt")
    signals.append(signal_processor.signal)
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal3.txt")
    signals.append(signal_processor.signal)
    added = operation.add(signals)
    SignalSamplesAreEqual("../data/task2/output signals/signal1+signal3.txt", [val[1] for val in added])


def testSubtract():
    signal_processor = SignalProcessor()
    print("Test Subtract:")
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal1.txt")
    signal1 = signal_processor.signal
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal2.txt")
    signal2 = signal_processor.signal
    subtracted = operation.subtract(signal1, signal2)
    SignalSamplesAreEqual("../data/task2/output signals/signal1-signal2.txt", [val[1] for val in subtracted])

    signal_processor.read_signal_from_file("../data/task2/input signals/Signal1.txt")
    signal1 = signal_processor.signal
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal3.txt")
    signal2 = signal_processor.signal
    subtracted = operation.subtract(signal1, signal2)
    SignalSamplesAreEqual("../data/task2/output signals/signal1-signal3.txt", [val[1] for val in subtracted])


def testMultiply():
    print("Test Multiply:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal1.txt")
    signal1 = signal_processor.signal
    multi = operation.multiply(signal1, 5)
    SignalSamplesAreEqual("../data/task2/output signals/MultiplySignalByConstant-Signal1 - by 5.txt",
                          [val[1] for val in multi])

    signal_processor.read_signal_from_file("../data/task2/input signals/Signal2.txt")
    signal2 = signal_processor.signal
    multi = operation.multiply(signal2, 10)
    SignalSamplesAreEqual("../data/task2/output signals/MultiplySignalByConstant-signal2 - by 10.txt",
                          [val[1] for val in multi])


def testSquare():
    print("Test Square:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal1.txt")
    signal1 = signal_processor.signal
    sq = operation.square(signal1)
    SignalSamplesAreEqual("../data/task2/output signals/Output squaring signal 1.txt", [val[1] for val in sq])


def testShift():
    print("Test Shift:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("../data/task2/input signals/Input Shifting.txt")
    Input1 = signal_processor.signal
    shifted1 = operation.shift(Input1, 500)
    shifted2 = operation.shift(Input1, -500)
    SignalSamplesAreEqual("../data/task2/output signals/output shifting by add 500.txt", [val[1] for val in shifted1])
    SignalSamplesAreEqual("../data/task2/output signals/output shifting by minus 500.txt", [val[1] for val in shifted2])


def testNormalize():
    print("Test Normalize:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal1.txt")
    Input1 = signal_processor.signal
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal2.txt")
    Input2 = signal_processor.signal
    normalized1 = operation.normalize(Input1, (-1, 1))
    normalized2 = operation.normalize(Input2, (0, 1))
    SignalSamplesAreEqual("../data/task2/output signals/normalize of signal 1 -- output.txt",
                          [val[1] for val in normalized1])
    SignalSamplesAreEqual("../data/task2/output signals/normlize signal 2 -- output.txt", [val[1] for val in normalized2])


def testAccumulate():
    print("Test Accumulate:")
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("../data/task2/input signals/Signal1.txt")
    Input1 = signal_processor.signal
    accumulated = operation.accumulation(Input1)
    SignalSamplesAreEqual("../data/task2/output signals/output accumulation for signal1.txt",
                          [val[1] for val in accumulated])


testAdd()
testSubtract()
testMultiply()
testSquare()
testShift()
testNormalize()
testAccumulate()
