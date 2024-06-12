import pyaudio      # https://people.csail.mit.edu/hubert/pyaudio/docs/
import numpy as np

# Parametres d'enregistrement
FORMAT = pyaudio.paInt16    # Format des donnees audio (16 bits)
CHANNELS = 1    # Nombre de canaux (1 pour mono, 2 pour stereo)
RATE = 44100    # Taux d'echantillonnage (nb d'echantillons par seconde)
CHUNK = 1024    # Taille du buffer audio

# Initialisation du flux audio
# appele une seule fois pour initialiser le flux audio a partir du micro
def get_audio_stream():
    """Initialise et retourne un flux audio a partir du microphone"""
    # To use PyAudio, first instantiate PyAudio and 
    # initialize PortAudio system resources
    audio = pyaudio.PyAudio()   # Creation d'une instance PyAudio

    # Open stream
    stream = audio.open(format=FORMAT, 
                        channels=CHANNELS,
                        rate=RATE, 
                        input=True,     # le flux est configure pour l'entree audio
                        frames_per_buffer=CHUNK)
    return stream

def record_audio(stream):
    """Enregistre un morceau de donnees audio a partir du flux"""
    data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
    return data
