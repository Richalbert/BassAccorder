import unittest
from bass_accorder.audio_capture import get_audio_stream, record_audio
from bass_accorder.frequency_analysis import analyze_frequency

class TestBassAccorder(unittest.TestCase):
    def test_audio_capture(self):
        stream = get_audio_stream()
        data = record_audio(stream)
        self.assertEqual(len(data), 1024)
        stream.stop_stream()
        stream.close()
    
    def test_frequency_analysis(self):
        data = np.sin(2 * np.pi * 440 * np.linspace(0, 1, 44100))  # Generate a 440 Hz sine wave
        freq = analyze_frequency(data, 44100)
        self.assertAlmostEqual(freq, 440, delta=1)
        
if __name__ == "__main__":
    unittest.main()
