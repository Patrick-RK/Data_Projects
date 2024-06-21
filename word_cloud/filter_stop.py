import nltk

from nltk.corpus import stopwords
from num2words import num2words
import ssl

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()
# custom_data_location = "/Users/Pato/nltk_data"
# nltk.download('stopwords')
# nltk.data.path.insert(0, custom_data_location)


def filter_stop_words(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)

    # Get English stop words from NLTK
    stop_words = set(stopwords.words('english'))

    # Filter out stop words and punctuation
    filtered_words = [word.lower() for word in words if word.lower() not in stop_words]

    return filtered_words

def convert_numbers(text):
    ftext = []

    for line in text:
        words = []
        if line != "":
                for word in line.split():
                    if word.isdigit():
                        words.append(num2words(int(word)))
                    else:
                        words.append(word)
                ftext.append(' '.join(words))

    return(ftext)



