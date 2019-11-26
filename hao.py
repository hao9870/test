import collections
import contextlib
import sys
import wave
import os
import webrtcvad


import librosa
import shutil
import librosa
import soundfile as sf
wav_path = '/Users/momo/Desktop/3/'
#wav_path = the directory of wavs to be handled
wav_file = os.listdir(wav_path)
for i, wav in enumerate(wav_file):

    if wav == ".DS_Store":
        continue
    else:

        f = open("Label.txt", 'a')
        f.write(os.getcwd()+'/'+os.path.basename(wav))
        f.write('\n')
