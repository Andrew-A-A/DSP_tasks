from FreqTools import dct, remove_dc
from SignalProcessor import SignalProcessor
from data.task5.comparesignal2 import SignalSamplesAreEqual

s = SignalProcessor()
s.read_signal_from_file("../data/task5/DCT/DCT_input.txt")
dct_signal = dct(s.signal)
SignalSamplesAreEqual("../data/task5/DCT/DCT_output.txt", dct_signal)

s.read_signal_from_file("../data/task5/Remove DC component/DC_component_input.txt")
dc_signal = remove_dc(s.signal)
SignalSamplesAreEqual(
    "../data/task5/Remove DC component/DC_component_output.txt", dc_signal
)
