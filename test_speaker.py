#test_gender.py
import os
import _pickle as cPickle
import os
import _pickle as cPickle
import numpy as np
from scipy.io.wavfile import read
from speakerfeatures import extract_features
from sklearn.mixture import GaussianMixture as GMM
import warnings
warnings.filterwarnings("ignore")
from tkinter import *
from tkinter import filedialog
import time
val=[]
#speakers=[]
def test():
    #path to training data
    print("hello")
    source   = "development_set/"   
    modelpath = "speaker_models/"
    test_file = "development_set_test.txt"        
    file_paths = open(test_file,'r')
    gmm_files = [os.path.join(modelpath,fname) for fname in 
              os.listdir(modelpath) if fname.endswith('.gmm')]
    #Load the Gaussian gender Models
    global speakers
    models    = [cPickle.load(open(fname,'rb')) for fname in gmm_files]
    speakers   = [fname.split("\\")[-1].split(".gmm")[0] for fname 
              in gmm_files]
    print(file_paths)
    print("hello")

    #Read the test directory and get the list of test audio files 
    for path in file_paths:  
        print(path) 
        #print("hello")
        path = path.strip()   
        print (source + path)
        sr,audio = read(source + path)
        vector   = extract_features(audio,sr)
        print(np.mean(vector))
        log_likelihood = np.zeros(len(models)) 
        print(log_likelihood)
        for i in range(len(models)):
          gmm    = models[i]         #checking with each model one by one
          scores = np.array(gmm.score(vector))
          log_likelihood[i] = scores.sum()
        winner = np.argmax(log_likelihood)
        #global speakers
        print(winner)
        print("\tdetected as - ", speakers[winner])
        global val
        val.append(speakers[winner])
        time.sleep(1.0)      
