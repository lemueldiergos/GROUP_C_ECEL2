import pyttsx3
import datetime
from nltk.tokenize import *
from nltk.stem import *
from nltk.corpus import wordnet, stopwords
import requests

tts_engine = pyttsx3.init()

VIRTUAL_VOICE = str(input("What Can I help you? "))

class MAIN:
    def __init__(self, str):
        
        self.voice           = str
        self.ARR_TEXT        = word_tokenize(self.voice.lower())
        self.word_stop       = set(stopwords.words('english'))
    

        tts_engine.say(self.voice)


    # LOCATOR
    def START(self):
        # INPUTTING METHOD
        
        # LOCATOR 
        IDENTIFIER          = ['ako', 'akon', 'my', 'mine', 'me', "i", "where"]
        LOCATION_IDENTIFIER = ['location', 'locate', 'local', 'area', 'place', 'where']
        
        # TIME
        ASK_NOW             = ['now', 'today', 'current', 'instant']
        ASK_DATE_TIME       = ['time', 'date', 'week', 'month']
        
        # ASK DEFINITION    
        DEF_VERIFICATION    = ['meaning', 'mean', 'definition', 'define', 'about', 'know']

        # OTHERS
        NOT_USED_SYMBOL     = ['?', '.', '!', '@', '#', ';', ':']

        # ASK SOMETHING
        REFERRAL_SELF       = 0
        REFERRAL_LOC        = 0

        TOKENIZED_MOB       = []

        for WORDS in self.ARR_TEXT:
            if WORDS not in self.word_stop and WORDS not in NOT_USED_SYMBOL:
                TOKENIZED_MOB.append(WORDS)

        for WORDS in TOKENIZED_MOB:
                try:
                    if WORDS not in DEF_VERIFICATION:
                         
                    


'''     for WORDS in self.ARR_TEXT:
            if (WORDS in IDENTIFIER):
                REFERRAL_SELF += 1
            if (WORDS in LOCATION_IDENTIFIER):
                
                REFERRAL_LOC += 1


        
        if(REFERRAL_SELF >= 1 and REFERRAL_LOC >= 1):
            rjson = requests.get('https://get.geojs.io/v1/ip.json')
            IP = rjson.json()['ip']
            getloc = requests.get('https://get.geojs.io/v1/geo/' + IP + '.json' )

            tts_engine.say("Your Current Location is "+ str(getloc.json()['city']) + ".")
        else:
            self.DEF_GIVER()

    # DEFINITION GIVER
    def DEF_GIVER(self):
        WORDS_TO_SEARCH     = ""
        IDENTIFIER_V1       = ['meaning', 'mean', 'definition', 'define', 'about']
        NOT_USED_SYMBOL     = ['?', '.', '!', '@', '#', ';', ':']
        for WORDS in self.ARR_TEXT:
            try:
                if WORDS not in self.word_stop:
                    if (WORDS not in IDENTIFIER_V1) and (WORDS not in NOT_USED_SYMBOL):
                        def_giver = wordnet.synsets(WORDS)
                        tts_engine.say(def_giver[0].definition())
            except:
                tts_engine.say("I don't understand you!")
                        
        
    # ASK TIME OR DATE
  
'''


init_main = MAIN(VIRTUAL_VOICE)

init_main.START()


tts_engine.runAndWait()
