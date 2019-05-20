import os
import sys
import glob
import numpy as np
import librosa
from scipy.io import wavfile

def main(pathAudio):
	#print(pathAudio)
	for filename in os.listdir(pathAudio):
		#print(filename)
		y, sr = librosa.load(pathAudio+filename, sr = 16000, mono=True)
		y = y * 32767 / max(0.01, np.max(np.abs(y)))
		wavfile.write('trumpnew/'+filename, sr, y.astype(np.int16))

if __name__ == '__main__':
	main('/home/anoop/anoopvenv/GMM/trump/')


