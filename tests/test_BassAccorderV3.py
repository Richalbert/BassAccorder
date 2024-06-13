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






    # '''genere une onde de 440 Hz qui correspond a la note La (A4)'''
    # def test_analyze_frequency(self):
    #     # Generate a 440 Hz sine wave
    #     fs = 44100  # Sample rate
    #     duration = 1.0  # Duration in seconds
    #     t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    #     frequency = 440  # Frequency of the sine wave
    #     sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
        
    #     # Analyze frequency pour detecter la frequence de l'onde
    #     detected_freq = analyze_frequency(sine_wave, fs)
        
    #     # Assert the detected frequency is close to 440 Hz 
    #     # avec une marge d'erreur de 1 Hz
    #     self.assertAlmostEqual(detected_freq, 440, delta=1.0)

    # '''ce test ne verifie pas visuellement le graphique mais s'assure que 
    # la fonction ne plante pas    '''
    # def test_plot_data(self):
    #     # Generate a 440 Hz sine wave
    #     fs = 44100  # Sample rate
    #     duration = 1.0  # Duration in seconds
    #     t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    #     frequency = 440  # Frequency of the sine wave
    #     sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
        
    #     try:
    #         # Plot data (this won't display a plot in a test, but will check for errors)
    #         plot_data(sine_wave, frequency)
    #     except Exception as e:
    #         self.fail(f"plot_data raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()


'''Execution des tests
    cd BassAccorder
    python -m unittest discover tests
'''

