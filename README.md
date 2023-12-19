# DSP tasks 2023 ASU
Welcome to the Signal Processing Toolbox repository! <br>
This toolbox provides a comprehensive set of functionalities for signal processing, covering both time domain and frequency domain tools.
The toolbox is designed to be user-friendly and customizable for various signal processing tasks.<br>
This is implementation of digital signal processing tasks for 4th year CS students in the Faculty of Computer Science at Ain Shams University.
The course aims to provide students with a comprehensive understanding of digital signal processing and its applications in various fields.
## Getting Started

To get started with the Signal Processing Toolbox, follow these steps:

### Prerequisites

Make sure you have the following prerequisites installed on your system:

- Python (version 3.x)
- Dependencies: numpy, matplotlib (install using `pip install numpy matplotlib`)

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/Andrew-A-A/DSP_tasks
```

### Usage

Navigate to the project directory and run the main script:

```bash
python main.py
```

This will launch the Signal Processing Toolbox application, and you will be presented with a menu to choose from different signal processing tasks.

## Features

### 1. Signal Generation

#### 1.1 Continuous and Discrete Signal Display

- Read samples of a signal from a txt file and display it in both continuous and discrete representations.

#### 1.2 Sinusoidal or Cosinusoidal Signal Generation

- Generate sinusoidal or cosinusoidal signals with user-specified parameters:
  - Type (sine or cosine)
  - Amplitude (A)
  - Phase shift (theta)
  - Analog frequency
  - Sampling frequency

### 2. Arithmetic Operations

#### 2.1 Signal Addition, Subtraction, and Multiplication

- Add, subtract, and multiply input signals and display the resulting signal.

#### 2.2 Signal Squaring, Shifting, and Normalization

- Square a signal and display the resulting signal.
- Shift a signal by a positive or negative constant.
- Normalize the signal within a user-specified range (-1 to 1 or 0 to 1).

#### 2.3 Accumulation

- Accumulate input signals.

### 3. Quantization

- Quantize an input signal based on user-specified levels or number of bits.
- Display the quantized signal, quantization error, and encoded signal.

### 4. Frequency Domain Tools

#### 4.1 Fourier Transform and Frequency Analysis

- Apply Fourier transform to any input signal.
- Display frequency versus amplitude and frequency versus phase relations.
- Prompt the user to enter the sampling frequency in HZ.

#### 4.2 Amplitude and Phase Modification

- Allow modification of the amplitude and phase of the signal components.

#### 4.3 Signal Reconstruction using IDFT

- Allow signal reconstruction using Inverse Discrete Fourier Transform (IDFT).

#### 4.4 Save and Read Frequency Components

- Save frequency components in a txt file in polar form (amplitude and phase).
- Read a txt file containing frequency components in polar form and reconstruct the signal using IDFT.

#### 4.5 Discrete Cosine Transform (DCT)

- Compute DCT for a given input signal and display the result.
- Allow the user to choose the first m coefficients to be saved in a txt file.

#### 4.6 Remove DC Component

- Remove the DC component in the time domain.

### 5. Time Domain Tools

#### 5.1 Smoothing

- Compute moving average \(y(n)\) for signal \(x(n)\), letting the user enter the number of points included in averaging.

#### 5.2 Sharpening

- Compute and display \(y(n)\) representing:
  - First Derivative of the input signal: \(Y(n) = x(n) - x(n-1)\)
  - Second Derivative of the input signal: \(Y(n) = x(n+1) - 2x(n) + x(n-1)\)

#### 5.3 Delaying or Advancing

- Delay or advance a signal by \(k\) steps.

#### 5.4 Folding

- Fold a signal.

#### 5.5 Delaying or Advancing a Folded Signal

- Delay or advance a folded signal.

#### 5.6 Remove the DC Component in Frequency Domain

- Remove the DC component in the frequency domain.

### 6. Convolution and Correlation

#### 6.1 Fast Convolution

- Perform fast convolution on two signals.

#### 6.2 Fast Correlation

- Perform fast correlation on two signals.

#### 6.3 Cross-Correlation

- Compute and display cross-correlation between two signals.

#### 6.4 Direct Convolution

- Convolve two signals using the direct method.

### Happy Signal Processing!
