# BassAccorder

BassAccorder est une application Python pour accorder une guitare basse en utilisant un microphone USB. 

Elle capture le son, analyse la fréquence principale et affiche les résultats.

1. La capture du son utilise la bibliothèque 'pyaudio' 

2. L'analyse du signal utilise la bibliotheque 'numpy' et la Transformee de Fourier permet d'extraire la frequence dominante

3. L'affichage du signal audio et de la frequence principale utilise la bibliotheque 'matplotlib'

## Installation

```sh
pip install -r requirements.txt
