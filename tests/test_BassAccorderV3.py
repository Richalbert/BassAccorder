import unittest             # pour creer des tests unitaires
import numpy as np          # pour les operations numeriques
import pyaudio              # ppour capturer le son
import matplotlib.pyplot as plt

#from BassAccorderV3.main import analyze_frequency, plot_data
from BassAccorderV3.main import soundPlot   # fonction a tester

'''La clasee herite de unittest.Testcase pour creer des tests unitaires'''
class TestBassAccorderV3(unittest.TestCase):

    '''La methode setUp()
        * initaialise PyAudio 
        * ouvre un flux audio pour la capture
        * definie les parametres RATE, CHUNK et window
    '''
    def setUp(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=1,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=2048)
        self.RATE = 44100
        self.CHUNK = 2048
        self.window = np.blackman(self.CHUNK)
        self.fig = plt.figure(figsize=(10, 8))
        self.ax1 = self.fig.add_subplot(211)
        self.ax2 = self.fig.add_subplot(212)


    '''La methode tearDown() ferme et nettoie le flux audio apres chaque test'''
    def tearDown(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


    '''La methode test la fonction soundPlot() avec le flux audio pour verifier
        qu'elle s'execute sans lever d'exception '''
    def test_soundPlot(self):
        try:
            soundPlot(self.stream, self.ax1, self.ax2)
        except Exception as e:
                self.fail((f"soundPlot raised an exception: {e}"))



if __name__ == '__main__':
    unittest.main()


'''Execution des tests
    cd BassAccorder
    python -m unittest discover tests
'''

