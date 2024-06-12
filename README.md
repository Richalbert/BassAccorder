# BassAccorder

BassAccorder est une application Python pour accorder une guitare basse en utilisant un microphone USB. 

Elle capture le son, analyse la fréquence principale et affiche les résultats.

1. La capture du son utilise la bibliothèque 'pyaudio' 

2. L'analyse du signal utilise la bibliotheque 'numpy' et la Transformee de Fourier permet d'extraire la frequence dominante

3. L'affichage du signal audio et de la frequence principale utilise la bibliotheque 'matplotlib'

la version 0.1 affiche une fenetre suivante lorsque la precedente est fermee

la version 0.2 introduit un affichage temps reel, avec une mise a jour de la fenetre graphique de maniere continue sans devoir la fermer, a l'aide d'un mecanisme de boucle d'evenements mettant a jour les donnees dans la figure existante


## Installation

```sh
pip install -r requirements.txt

## Lancement de BassAccorder

```sh
python -m bass_acccorder.main

## Utilisation de BassAccorder

1. Connecter le micro USB au PC

2. Lancer l'application qui va capturer le son, analyser la frequence principale et afficher les resultats

3. Les frequences de chacune des cordes sont:
* Mi: 41,2 Hz
* La: 55 Hz
* Re: 73,4 Hz
* Sol: 98 Hz