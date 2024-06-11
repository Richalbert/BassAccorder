import pyaudio
import numpy as np

# Parametres d'enregistrement
FORMAT = pyaudio.paInt16    # Format des donnees audio
CHANNELS = 1    # Nombre de canaux (mono)
RATE = 44100    # Taux d'echantillonnage
CHUNK = 1024    # Taille du buffer

def get_audio_stream():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    return stream

def record_audio(stream):
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    return data
