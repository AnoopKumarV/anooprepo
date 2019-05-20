import pygame
from tkinter import *  # not advisable to import everything with *
from tkinter import filedialog
import audioslice as slice1
import test_speaker as ts
from pydub import AudioSegment
from pydub.playback import play
pygame.mixer.init() # initializing the mixer
root = Tk()
audio_file_name = ''
lb1 = Label(root,text="The speakers in this audio file are")
lb1.pack(side=LEFT)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )
mylist = Listbox(root, width=15, height=15, yscrollcommand = scrollbar.set )
root.title("Speaker Recognition")
def open_masker():
    global audio_file_name
    audio_file_name = filedialog.askopenfilename(filetypes=(("Audio Files", ".wav .ogg"),   ("All Files", "*.*")))
    
    #m_label = Label(root, text = audio_file_name)
    #m_label.pack(anchor = CENTER)
def predict_masker():
    slice1.predict(audio_file_name)
    lb = Label(root,text=len(ts.val))
    lb.pack(side=RIGHT)
    
    for i in  range (0,len(ts.val)):
        mylist.insert(END, ts.val[i].split('/')[1])
def playsong():
    song = AudioSegment.from_wav(audio_file_name)
    play(song)    
mylist.pack( side = LEFT)
scrollbar.config( command = mylist.yview )
root.resizable(0, 0)
b1 = Button(root, text = 'open file',command = open_masker)
b2 = Button(root, text = 'predict',command = predict_masker)
b3 = Button(root, text = 'Playvoice',command=playsong)
b1.pack(anchor=CENTER)
b2.pack(anchor=CENTER)
b3.pack(anchor=CENTER)
root.mainloop()







