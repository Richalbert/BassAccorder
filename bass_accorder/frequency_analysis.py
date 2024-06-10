import numpy as np
from scipy.fftpack import fft

def analyze_frequency(data, rate):
    fft_data = fft(data)
    freqs = np.fft.fftfreq(len(fft_data))
    
    idx = np.argmax(np.abs(fft_data))
    freq = abs(freqs[idx] * rate)
    
    return freq
