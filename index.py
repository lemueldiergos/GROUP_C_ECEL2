import nltk

# nltk.download('vader_lexicon')


import matplotlib.pyplot as plot



from nltk.tokenize import *
from nltk.probability import *
from nltk.corpus import *
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer

text = """Hello world!, Welcome to nice change changing chager coding coder cool coolest cooler programmer programming my world, WOOOORLD, happen happenning hapiness happy   worldworld world world in your dream, tangina mo, testing lang man ni ah"""

ARR_WORDS    = word_tokenize(text)
ARR_SENT     = sent_tokenize(text)

FREQ_D       = FreqDist(ARR_WORDS)

MOST_C       = FREQ_D.most_common()

STOPW        = set(stopwords.words('english'))

STEEMING    = PorterStemmer()
Lematize    = WordNetLemmatizer()

analyzer = SentimentIntensityAnalyzer()

# for word in ARR_WORDS:
#     print(word, STEEMING.stem(word), Lematize.lemmatize(word))

# print(analyzer.polarity_scores(text))

# syn = wordnet.synsets("figurine")
# print(syn[0].definition())

for syn in wordnet.synsets('my'):
    for list in syn.lemmas():
        #print(list.name())
        if list.antonyms():
            print(list.antonyms()[0].name())



