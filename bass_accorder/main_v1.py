import matplotlib.pyplot as plt
from .audio_capture import get_audio_stream, record_audio
from .frequency_analysis import analyze_frequency
from scipy.fftpack import fft 
import numpy as np

# Paramètres d'enregistrement
RATE = 44100  # Taux d'échantillonnage

"""La fonction plot_data affiche les donnees audio capturees et 
leur transformee de Fourier (FFT) afin d'analyser le frequence principale 
"""
def plot_data(data, freq):
    # Initialisation de la figure
    plt.figure(figsize=(10, 6))     # 10 pouces de largeur, 6 pouces de hauteur

    # 1er sous graphe: le signal audio
    plt.subplot(2, 1, 1)        # 2 lignes, 1 colonne sur le 1er sous graphe
    plt.plot(data)              # trace les donnees brutes
    plt.title("Signal Audio")   # titre du sous graphe 
    
    # 2nd sous graphe: la FFT du signal
    plt.subplot(2, 1, 2)        # 2 lignes, 1 colonne sur le 2nd sous graphe
    # Calcule la FFT: 
    #   fft(data)       applique la FFT au signal
    #   np.abs(..)      prend la valeur absolue des coeff de la FFT
    #   [:len(data)//2] prend uniquement la 1ere partie du spectre
    #                   la FFT est symetrique pour un signal reel
    plt.plot(np.abs(fft(data))[:len(data)//2])
    plt.title(f"FFT - Fréquence principale: {freq:.2f} Hz")
    
    # Ajustement de la mise en page
    plt.tight_layout()

    # Affichage de la figure
    plt.show()

def main():
    stream = get_audio_stream()     # Initialisation du flux audio
    try:
        while True:
            data = record_audio(stream)     # capture un morceau de donnees audio
            freq = analyze_frequency(data, RATE)    # analyse la freq principale
            plot_data(data, freq)       # affiche le signal audio et son spectre
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop_stream()
        stream.close()

if __name__ == "__main__":
    print(__name__)
    main()


""" Le code se lance dans un terminal en tapant la commande

    python -m bass_accorder.main

"""