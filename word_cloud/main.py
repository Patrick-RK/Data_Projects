import csv
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
from filter_stop import *
from wordcloud import WordCloud


def plot_word_frequency_from_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        text = text.lower()

    text_alpha = re.sub(r'[^a-z\s]', '', text)
    text_split_by_newline = text_alpha.split('\n')

    f_text = convert_numbers(text_split_by_newline)

    s_text = filter_stop_words(' '.join(f_text))
    word_freq = Counter(s_text)
    word_dict = dict(word_freq)
    df = pd.DataFrame(list(word_dict.items()), columns=['word', 'freq'])
    df_filtered = df[df['word'].apply(len) >= 3]
    sorted_df = df_filtered.sort_values(by='freq', ascending=False)

    top_words = sorted_df.head(100)

    def plot_freq(words):
        # Plot the word frequency distribution
        plt.figure(1, figsize=(10, 6))  # Specify figure number as 1
        plt.bar(words["word"], words["freq"], color='skyblue')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.title('Word Frequency Distribution')
        plt.xticks(rotation=90, ha='right')
        plt.tight_layout()
        plt.show()
    # plot_freq(top_words)

    def plot_word_cloud(words):
        word_freq_dict = dict(zip(words["word"], words["freq"]))
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq_dict)
        plt.figure(2, figsize=(10, 5))  # Specify figure number as 2
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.show()

    plot_word_cloud(top_words)


txt_file = 'drake-lyrics.txt'
plot_word_frequency_from_text(txt_file)

