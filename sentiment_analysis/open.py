import pysrt
import os
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt


folder_path = '/Users/Pato/PycharmProjects/Drake/starwars/'
files = os.listdir(folder_path)
srt_files = [file for file in files if file.endswith('.srt')]
episodes = [os.path.join(folder_path, file) for file in srt_files]
test = episodes[0]

import chardet

subtitles_data = []



def open_srt(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']

    with open(file_path, 'r', encoding=encoding) as f:
            subs = pysrt.from_string(f.read())
            print(f"file:{file_path}")
            print(subs)

for episode in episodes:
    open_srt(episode)

