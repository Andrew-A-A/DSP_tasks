from Shift_Fold_Signal import Shift_Fold_Signal
from SignalProcessor import SignalProcessor
from SignalToolkit import *
from data.task5.comparesignal2 import SignalSamplesAreEqual
from data.task7.Convolution.ConvTest import *



def derivative_signal_test():
    # region input
    InputSignal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                   53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
                   78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    expectedOutput_first = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                            1, 1, 1, 1, 1, 1]
    expectedOutput_second = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                             0, 0, 0, 0, 0, 0, 0, 0, 0]
    # endregion
    """
    Write your Code here:
    Start
    """

    def sharping(signal):
        first_derivative = []
        second_derivative = []
        for i in range(0, len(signal)-1):
            x_n = signal[i]
            if i == 0:
                x_min_1 = 0
            else:
                x_min_1 = signal[i - 1]
            if i == len(signal) - 1:
                x_plus_1 = 0
            else:
                x_plus_1 = signal[i + 1]

            first_derivative.append(x_n - x_min_1)
            second_derivative.append(x_plus_1 - (2 * x_n) + x_min_1)
        return first_derivative, second_derivative

    FirstDrev, SecondDrev = sharping(InputSignal)

    """
    End
    """

    """
    Testing your Code
    """
    if (len(FirstDrev) != len(expectedOutput_first)) or (
            len(SecondDrev) != len(expectedOutput_second)
    ):
        print("mismatch in length")
        return
    first = second = True
    for i in range(len(expectedOutput_first)):
        if abs(FirstDrev[i] - expectedOutput_first[i]) < 0.01:
            continue
        else:
            first = False
            print("1st derivative wrong")
            return
    for i in range(len(expectedOutput_second)):
        if abs(SecondDrev[i] - expectedOutput_second[i]) < 0.01:
            continue
        else:
            second = False
            print("2nd derivative wrong")
            return
    if first and second:
        print("Derivative Test case passed successfully")
    else:
        print("Derivative Test case failed")
    return


print("Sharping Test:")
derivative_signal_test()
print("----------------------")

print("Smoothing Test:")
s = SignalProcessor()
s.read_signal_from_file("../data/task6/TestCases/Moving Average/MovAvgTest2.txt")
s_signal = smooth_amplitudes(s.signal, 3)
SignalSamplesAreEqual(
    "../data/task6/TestCases/Moving Average/OutMovAvgTest2.txt",
    [val[1] for val in s_signal],
)
print("----------------------")

print("Folding Test:")
s.read_signal_from_file("../data/task6/TestCases/Shifting and Folding/input_fold.txt")
s_signal = folding(s.signal)
SignalSamplesAreEqual(
    "../data/task6/TestCases/Shifting and Folding/Output_fold.txt",
    [val[1] for val in s_signal],
)
print("----------------------")

print("Remove DC Test:")
s.read_signal_from_file("../data/task5/Remove DC component/DC_component_input.txt")
s_signal = remove_dc_frequency_domain(s.signal)
SignalSamplesAreEqual(
    "../data/task5/Remove DC component/DC_component_output.txt",
    [val[1] for val in s_signal],
)
print("----------------------")

print("Shif Folded by 500 Test:")
s = SignalProcessor()
s.read_signal_from_file("../data/task6/TestCases/Shifting and Folding/input_fold.txt")
first_column, second_column = shift_folding(s.signal, 500)
Shift_Fold_Signal(
    "../data/task6/TestCases/Shifting and Folding/Output_ShifFoldedby500.txt",
    first_column,
    second_column,
)
print("----------------------")

print("Shif Folded by -500 Test:")
s = SignalProcessor()
s.read_signal_from_file("../data/task6/TestCases/Shifting and Folding/input_fold.txt")
first_column, second_column = shift_folding(s.signal, -500)
Shift_Fold_Signal(
    "../data/task6/TestCases/Shifting and Folding/Output_ShiftFoldedby-500.txt",
    first_column,
    second_column,
)
print("----------------------")

print("Convolution Test:")
s = SignalProcessor()
signal1 = s.read_signal_from_file("../data/task7/Convolution/Input_conv_Sig1.txt")
signal2 = s.read_signal_from_file("../data/task7/Convolution/Input_conv_Sig2.txt")
indices, samples = convolve(signal1, signal2)
ConvTest(indices, samples)
print("----------------------")
