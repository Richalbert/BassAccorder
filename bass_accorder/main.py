import matplotlib.pyplot as plt         # https://matplotlib.org/
from .audio_capture import get_audio_stream, record_audio
from .frequency_analysis import analyze_frequency
from scipy.fftpack import fft 
import numpy as np

# Paramètres d'enregistrement
RATE = 44100  # Taux d'échantillonnage

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html#matplotlib.pyplot.subplots

def plot_data_init():
    '''Initialise la figure et des axes pour l'affichage temps reel'''
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    line1, = ax1.plot([], [])
    line2, = ax2.plot([], [])
    ax1.set_title("Signal Audio")
    ax2.set_title("FFT - Fréquence principale: ")
    return fig, ax1, ax2, line1, line2



def plot_data_update(line1, line2, ax1, ax2, data, freq):
    """Met à jour les tracés avec les nouvelles données capturées."""

    line1.set_data(np.arange(len(data)), data)      # maj des donnees du sugnal audio

    # Calcule la FFT: 
    #   fft(data)       applique la FFT au signal
    #   np.abs(..)      prend la valeur absolue des coeff de la FFT
    #   [:len(data)//2] prend uniquement la 1ere partie du spectre
    #                   la FFT est symetrique pour un signal reel
    fft_data = np.abs(fft(data))[:len(data)//2]
    
    line2.set_data(np.arange(len(fft_data)), fft_data)  # maj des donnees de la FFT

    ax2.set_title(f"FFT - Fréquence principale: {freq:.2f} Hz")

    # les limites des axes s'adaptent a chaque jeu de donnees
    ax1.set_xlim(0, len(data))
    ax1.set_ylim(np.min(data), np.max(data))

    ax2.set_xlim(0, len(fft_data))
    ax2.set_ylim(0, np.max(fft_data))

    plt.draw()      # redessine la figure
    plt.pause(1)    # apres une pause


def main():

    # Initialisation du flux audio
    stream = get_audio_stream()     

    # Initialisation de la figure
    fig, ax1, ax2, line1, line2 = plot_data_init()


    try:
        while True:
            data = record_audio(stream)                         # capture les donnees
            freq = analyze_frequency(data, RATE)                # analyse la frequence
            plot_data_update(line1, line2, ax1, ax2, data, freq)     # maj les figures
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()
        plt.close(fig)



if __name__ == "__main__":
    print(__name__)
    main()


""" Le code se lance dans un terminal en tapant la commande

    python -m bass_accorder.main

"""