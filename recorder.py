import sounddevice as sd 
import soundfile as sf 
import matplotlib.pyplot as plt
import numpy as np
import wave
from pyglet.resource import media
from time import sleep 
# from pygame import mixer

def importSignal (name):
	spf = wave.open(name,'r')
	signal = spf.readframes(-1)
	signal = np.fromstring(signal, 'Int16')
	if spf.getnchannels() == 2:
		raise ValueError ('Mone wave supported')
	return signal

def plot (name):
	signal = importSignal (name)
	print (signal)
	plt.figure(1)
	plt.title(name)
	plt.plot(signal)
	plt.show()
def play (name):

	med = media (name)
	med.play ()
	sleep (med.duration-0.212)
	return med

def record (prompt, time=1):
	print (prompt)
	sd.default.channels = 1
	data = sd.rec (int (time*44100))
	sd.wait ()
	return data

def save (data,name):
	sf.write (name, data, 44100)	

def init ():
	mixer.init ()

def main ():
	play ('nghiệp.mp3')
	pass

# init ()
if __name__ == '__main__':
	main ()

