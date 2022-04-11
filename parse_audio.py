import sys, re, librosa
import matplotlib.pyplot as plt
import numpy as np
import IPython.display as ipd

# Helper code used to set-up the rest of the code
class Bird:
    def __init__(self, scientific_name = 'AVES', common_name = 'BIRD', colour = 'UNKOWN'):
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.colour = colour


def plot_sound(labeldict, filedir, filename):
    audio, _ = librosa.load(filedir+filename)
    plt.plot(np.abs(audio))
    plt.ylabel('Amplitude')
    plt.show()

#def get_soundfile(filedir, filename):
#    audio, sr = librosa.load(filedir+filename)
#    return ipd.Audio(audio, rate=sr)
    
# Code with logic and calls to other functions
if len(sys.argv) < 2:
    sys.exit('No argument input. Enter a valid audio file.')

m = re.search(f'(.*)', sys.argv[1])
if m == None:
    sys.exit('No valid file input. Enter a valid audio file.')

print(m.groups())

