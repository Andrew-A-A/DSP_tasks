from FourierMagic import dft, idft
from SignalProcessor import SignalProcessor
from data.task4.signalcompare import SignalComapreAmplitude, SignalComaprePhaseShift


# 1- read the output file
# 2- put the data of output file in the two lists (amplitude and phase)
# 3- run each function in file
# 4- and make condition if the two functions return the true
def DFT_test():
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file(
        "../data/task4/DFT/Output_Signal_DFT_A,Phase.txt"
    )
    dft_test_amplitude = [val[0] for val in signal_processor.signal]
    dft_test_phase = [val[1] for val in signal_processor.signal]
    signal_processor.read_signal_from_file("../data/task4/DFT/input_Signal_DFT.txt")
    dft_actual = dft(signal_processor.signal)
    dft_actual_amplitude = [val[0] for val in dft_actual]
    dft_actual_phase = [val[1] for val in dft_actual]
    amp_test = SignalComapreAmplitude(dft_actual_amplitude, dft_test_amplitude)
    phase_test = SignalComaprePhaseShift(dft_actual_phase, dft_test_phase)
    if amp_test and phase_test:
        print("DFT Test passed")


def IDFT_test():
    signal_processor = SignalProcessor()
    signal_processor.read_signal_from_file("../data/task4/IDFT/Output_Signal_IDFT.txt")
    idft_test_amplitude = [val[0] for val in signal_processor.signal]
    idft_test_phase = [val[1] for val in signal_processor.signal]
    signal_processor.read_signal_from_file(
        "../data/task4/IDFT/Input_Signal_IDFT_A,Phase.txt"
    )
    idft_actual = idft(signal_processor.signal)
    idft_actual_amplitude = [val[0] for val in idft_actual]
    idft_actual_phase = [val[1] for val in idft_actual]
    amp_test = SignalComapreAmplitude(idft_actual_amplitude, idft_test_amplitude)
    phase_test = SignalComaprePhaseShift(idft_actual_phase, idft_test_phase)
    if amp_test and phase_test:
        print("IDFT Test passed")


DFT_test()

IDFT_test()
