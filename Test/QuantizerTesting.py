from Quantizer import quantize
from SignalProcessor import SignalProcessor
from data.Task3.Test1.QuanTest1 import QuantizationTest1
from data.Task3.Test2.QuanTest2 import QuantizationTest2


def test_quantize():
    signalProcessor = SignalProcessor()
    signalProcessor.read_signal_from_file("../data/Task3/Test1/Quan1_input.txt")
    q = quantize(signalProcessor.signal, bits_num=3)
    QuantizationTest1("../data/Task3/Test1/Quan1_Out.txt", [val[0] for val in q],
                      [val[1] for val in q])
    signalProcessor = SignalProcessor()
    signalProcessor.read_signal_from_file("../data/Task3/Test2/Quan2_input.txt")
    q = quantize(signalProcessor.signal, levels_num=4)
    QuantizationTest2("../data/Task3/Test2/Quan2_Out.txt", [val[0] for val in q],
                      [val[1] for val in q],
                      [val[2] for val in q], [val[3] for val in q])


test_quantize()
