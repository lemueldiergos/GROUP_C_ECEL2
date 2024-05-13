import pyttsx3
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import *
from nltk.corpus import wordnet

tts_engine = pyttsx3.init()

SAMPLE_VOICE = """please locate my area"""

VIRTUAL_VOICE = str(input("What Can I help you? "))

print(VIRTUAL_VOICE)

# IDENTIFIER 

# LOCATOR 
IDENTIFIER          = ['ako', 'akon', 'my', 'mine', 'me', "i"]
LOCATION_IDENTIFIER = ['location', 'locate', 'local', 'area', 'place', 'where']

# ASK SOMETHING
IDENTIFIER_V1       = ['what']



ARR_TEXT        = word_tokenize(VIRTUAL_VOICE.lower())

# GET LOCATION COMMAND
REFERRAL_SELF = 0
REFERRAL_LOC  = 0

for WORDS in ARR_TEXT:
    if (WORDS in IDENTIFIER):
        REFERRAL_SELF += 1

for WORDS in ARR_TEXT:
    if (WORDS in LOCATION_IDENTIFIER):
        REFERRAL_LOC += 1

if(REFERRAL_SELF >= 1 and REFERRAL_LOC >= 1):
    tts_engine.say("Words DETECTED: " + str(REFERRAL_SELF) +  " -- Getting the location...")
    



tts_engine.runAndWait()