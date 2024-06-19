import pysrt
import os
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import chardet


folder_path = '/Users/Pato/PycharmProjects/Drake/starwars/'
files = os.listdir(folder_path)
srt_files = [file for file in files if file.endswith('.srt')]
episodes = [os.path.join(folder_path, file) for file in srt_files]
test = episodes[0]




def generate_sentiment(f_path):
    subtitles_data = []

    def analyze_sentiment(text):
        import re
        text = re.sub(r'[^a-zA-Z0-9]', '', text)
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        return sentiment_score

    def open_srt(f_path):
        with open(f_path, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']

        with open(f_path, 'r', encoding=encoding) as f:
            subs = pysrt.from_string(f.read())
            print(f"file:{f_path}")
            print(subs)

        return subs

    subs = open_srt(f_path)

    for sub in subs:

        index = sub.index
        start = sub.start.to_time()
        end = sub.end.to_time()
        text = sub.text

        subtitles_data.append({
                'index': index,
                'start_time': start,
                'end_time': end,
                'text': text
            })

        subtitles_df = pd.DataFrame(subtitles_data)
        subtitles_df['sentiment_score'] = subtitles_df['text'].apply(analyze_sentiment)
        subtitles_df['cumulative_sentiment'] = subtitles_df['sentiment_score'].cumsum()

    return subtitles_df



for i, episode in enumerate(episodes):

    row = i // 3
    col = i % 3
    df = generate_sentiment(episode)

    file_path = f"{episode}_data.csv"
    file_path = file_path.replace(".srt", "")

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

plt.tight_layout()
plt.show()
