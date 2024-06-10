import matplotlib.pyplot as plt
from .audio_capture.py import get_audio_stream, record_audio
from .frequency_analysis import analyze_frequency

def plot_data(data, freq):
    plt.figure(figsize=(10, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(data)
    plt.title("Signal Audio")
    
    plt.subplot(2, 1, 2)
    plt.plot(np.abs(fft(data))[:len(data)//2])
    plt.title(f"FFT - Fréquence principale: {freq:.2f} Hz")
    
    plt.tight_layout()
    plt.show()

def main():
    stream = get_audio_stream()
    try:
        while True:
            data = record_audio(stream)
            freq = analyze_frequency(data, RATE)
            plot_data(data, freq)
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()

if __name__ == "__main__":
    main()
