# Data_Projects

Three small Python data projects from June 2024. I made them while learning, and they read that way.

## What's here

**`image_recognition.ipynb`: a CNN on CIFAR-10.**
A small Keras network (three conv layers, two dense) trained on the 50,000 CIFAR-10 training images.
On the 10,000 test images it reaches 72% accuracy.
Cats are the weakest class (recall 0.52). Trucks are the strongest (recall 0.85).
The notebook also tries a second model with data augmentation.
The CIFAR-10 batches are committed in `image_recognition/cifar-10-batches-py/` (about 180 MB).

**`sentiment_analysis/`: sentiment across the six Star Wars films.**
It reads each film's `.srt` subtitles, scores every line with TextBlob, and writes a CSV with a per-line and cumulative score.
It has a bug. `analyze_sentiment` strips every non-alphanumeric character, spaces included, so each line becomes one long word.
Most lines score 0 as a result: only 3 to 36 of the 1,146 to 1,645 lines per film get a non-zero score.
The CSVs in `starwars/` are the output of that buggy version.

**`word_cloud/`: a word cloud from a lyrics file.**
It lower-cases the text, spells out numbers, drops stop words and words under three letters, and draws the top 100 as a word cloud.

## Stack

Python, TensorFlow/Keras, scikit-learn, NumPy, pandas, TextBlob, pysrt, NLTK, wordcloud, Matplotlib.

## How to run

There is no `requirements.txt`. Install what each script imports:

```bash
pip install tensorflow scikit-learn numpy pandas matplotlib textblob pysrt chardet nltk num2words wordcloud
```

- CIFAR-10: open `image_recognition.ipynb` and change `data_dir` to `image_recognition/cifar-10-batches-py`.
- Sentiment: `sentiment_analysis/file.py` has a hard-coded `folder_path` from my machine. Point it at `sentiment_analysis/starwars/`.
- Word cloud: `cd word_cloud && python main.py`.

`image_recognition/image_recognition.py` is empty. The code is all in the notebook.

## Status

Finished and not maintained. Last change June 2024.
