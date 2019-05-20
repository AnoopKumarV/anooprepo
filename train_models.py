#train_models.py

import _pickle as cPickle
import numpy as np
from scipy.io.wavfile import *
from sklearn.mixture import GaussianMixture as GMM
from speakerfeatures import extract_features
import warnings
import librosa
from pydub import AudioSegment
from pydub.utils import mediainfo
import soundfile as sf
warnings.filterwarnings("ignore")


#path to training data
source   = "development_set/"   

#path where training speakers will be saved
dest = "speaker_models/"

train_file = "development_set_enroll.txt"        


file_paths = open(train_file,'r')

count = 1

# Extracting features for each speaker (5 files per speakers)
features = np.asarray(())
for path in file_paths:    
    path = path.strip()   
    print(path)
    '''audio = AudioSegment.from_wav(source+path)
    frames_per_second = audio.frame_rate
    print(frames_per_second)
    if frames_per_second > 16000:
      newaudio = audio.set_frame_rate(16000)
      newaudio.export("file.wav", format="wav")
      print(newaudio.frame_rate)'''
    #write('newaudio.wav',16000,newaudio)   
   
    # extract 40 dimensional MFCC & delta MFCC features
    #vector   = extract_features(audio,sr)
    #read the audio
    sr,audio = read(source + path)
    #audio = (audio/ 32767).astype(int)
    #print(audio)
    #print(sr)
    # extract 40 dimensional MFCC & delta MFCC features
    vector   = extract_features(audio,sr)
    
    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
   
    # when features of 5 files of speaker are concatenated, then do model training
    if count == 5:    
        print(np.mean(features))
        gmm = GMM(n_components = 16,max_iter = 200, covariance_type='diag',n_init = 3)
        gmm.fit(features)
        
        # dumping the trained gaussian model
        picklefile = path.split("-")[0]+".gmm"
        print(picklefile)
        cPickle.dump(gmm,open(dest + picklefile,'wb'))
        print ('+ modeling completed for speaker:',picklefile," with data point = ",features.shape)    
        features = np.asarray(())
        count = 0
    count = count + 1
    
