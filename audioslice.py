from pydub import AudioSegment
from pydub.utils import mediainfo
import soundfile as sf
import test_speaker as ts
import os
import _pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
from sklearn.mixture import GaussianMixture as GMM
import warnings
warnings.filterwarnings("ignore")
import time
import librosa

def predict(audiofile):
    t1=1
    t2=4
    t1 = t1 * 1000 #Works in milliseconds
    t2 = t2 * 1000
    f1=open("development_set_test.txt","w")
    fname = audiofile
    f = sf.SoundFile(fname)
    print('samples = {}'.format(len(f)))
    print('sample rate = {}'.format(f.samplerate))
    print('seconds = {}'.format(len(f) / f.samplerate))
    seconds = (len(f) // f.samplerate)
    newAudio = AudioSegment.from_wav(audiofile)
    for i in range(1000, seconds*1000, 4000):
        print(i,i+4000)
        newAudio1 = newAudio[i:i+4000]
        frames_per_second = newAudio1.frame_rate
        #print(frames_per_second)
        if frames_per_second > 16000:
          newAudio1 = newAudio1.set_frame_rate(16000)
          newAudio1.export('development_set/test/newSong'+str(i)+'.wav', format="wav")
          #print(newAudio.frame_rate)
        else:
          newAudio1.export('development_set/test/newSong'+str(i)+'.wav', format="wav") 
        #t1 = t1+4000
        #t2 = t2+4000
        #print('development_set/test/newSong'+str(i)+'.wav')
        f1.write('test/newSong'+str(i)+'.wav\n')
    f1.close()
    #newAudio = 0
    #print("hello")
    ts.test()
