from pydub import AudioSegment
from pydub.utils import mediainfo
    
audio = AudioSegment.from_wav("newtest2.wav")
frames_per_second = audio.frame_rate
print(frames_per_second)
if frames_per_second > 16000:
  newaudio = audio.set_frame_rate(16000)
  newaudio.export("file2.wav", format="wav")
  print(newaudio.frame_rate)
