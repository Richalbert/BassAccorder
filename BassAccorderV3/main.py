import pyaudio
import numpy as np
import time
import wave
import matplotlib.pyplot as plt

# open stream
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 2048  # RATE / number of updates per second

RECORD_SECONDS = 20

# use a Blackman window
window = np.blackman(CHUNK)

def soundPlot(stream, ax1, ax2):
    t1 = time.time()
    data = stream.read(CHUNK, exception_on_overflow=False)
    waveData = wave.struct.unpack("%dh" % (CHUNK), data)
    npArrayData = np.array(waveData)
    indata = npArrayData * window
    
    # Plot time domain
    ax1.cla()
    ax1.plot(indata)
    ax1.grid()
    ax1.axis([0, CHUNK, -5000, 5000])
    
    fftData = np.abs(np.fft.rfft(indata))
    fftTime = np.fft.rfftfreq(CHUNK, 1./RATE)
    which = fftData[1:].argmax() + 1
    
    # Plot frequency domain graph
    ax2.cla()
    ax2.plot(fftTime, fftData)
    ax2.grid()
    ax2.axis([0, 5000, 0, 10**6])
    
    plt.pause(0.0001)
    print("took %.02f ms" % ((time.time() - t1) * 1000))
    
    # Use quadratic interpolation around the max
    if which != len(fftData) - 1:
        y0, y1, y2 = np.log(fftData[which - 1:which + 2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        thefreq = (which + x1) * RATE / CHUNK
    else:
        thefreq = which * RATE / CHUNK
    print("The freq is %f Hz." % (thefreq))

if __name__ == "__main__":
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    
    plt.ion()
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    
    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #     soundPlot(stream, ax1, ax2)

    try:
        while True:
            soundPlot(stream, ax1, ax2)
    except KeyboardInterrupt:
        print("Exiting ...")
    
    stream.stop_stream()
    stream.close()
    p.terminate()
