import nltk
#tokenizers
from nltk import sent_tokenize, word_tokenize
#stopwords
from nltk.corpus import stopwords

def tokenize(txt):
    sentence = sent_tokenize(txt)
    words = word_tokenize(txt)
    return [words, sentence]

def filter(txt):
    words = tokenize(txt)[0]
    filtered_words = [w for w in words if not w in stopwords]
    
    filtered_sentences = []

    for w in sentences:
        if w not in stop_words:
            filtered_sentences.append(w)

    return [filtered_words, filtered_sentences]