import speech_recognition           # Library for Voice Recoginition
import pyttsx3                      # Text to speech library
import requests                     # used to request the current lcoation online
import nltk                         # NLP library
import datetime                     # date and time library

from nltk.tokenize import *         
from nltk.stem     import *
from nltk.corpus   import *

from speech_recognition.recognizers import *

tts_engine = pyttsx3.init()         # initialize the text to speech library


                                    # main function of the entire system
class MAIN:

                                    # contructor 
    def __init__(self):
        self.voice      = ""
        self.arr_t      = []
        self.w_stop     = set(stopwords.words('english'))

                                    # start function
    def START(self):
                                    # tokenize the words or text recieve
                                    
        self.arr_t      = word_tokenize(self.voice.lower())
        LOCATION_KEYWORDS = ['location', 'locate', 'local', 'city', 'town', 'area']
        TIME_KEYWORDS     = ['time', 'clock']

        TOKEN_MOB = []

        for WORDS in self.arr_t:
            if WORDS not in self.w_stop:
                TOKEN_MOB.append(WORDS)


        for LOC_WORDS in TOKEN_MOB:
            if LOC_WORDS in ['dictionary', 'mode']:
                DIC_TO_WORD = self.VOICE_REC()
                DEF_GET = wordnet.synsets(DIC_TO_WORD)
                tts_engine.say(DEF_GET[0].definition())
                break 

        for LOC_WORDS in TOKEN_MOB:
            for LK_WORDS in LOCATION_KEYWORDS:
                if str(LOC_WORDS) == str(LK_WORDS):
                    rjson = requests.get('https://get.geojs.io/v1/ip.json')         
                    IP = rjson.json()['ip']
                    GETLOC = requests.get('https://get.geojs.io/v1/geo/' + IP + '.json' )
                    tts_engine.say("Your Current Location is "+ str(GETLOC.json()['city']) + ".")

        for LOC_WORDS in TOKEN_MOB:
            for CK_WORDS in TIME_KEYWORDS:
                if str(LOC_WORDS) == str(CK_WORDS):
                    STATIC_TIME = datetime.datetime.now()
                    TIME_TO_SAY = str("the time is " + str(int(STATIC_TIME.strftime("%I"))) + " " + str(int(STATIC_TIME.strftime("%M"))) + " " + STATIC_TIME.strftime("%p"))
                    print(TIME_TO_SAY)
                    tts_engine.say(TIME_TO_SAY)

    def VOICE_REC(self):
        recognizer = speech_recognition.Recognizer()
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(mic, duration=0.1)
                    audio = recognizer.listen(mic)

                    text = str(recognizer.recognize_google(audio))
                    text = text.lower()
                    print(text)
                    self.voice = text
                    print("END")
                    return self.voice
                    
            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                print("ERROR WHILE LISTENING")
                continue
            except speech_recognition.RequestError:
                print("error!")
                break

print("\n\n-------------------------------------")

func = MAIN()
func.VOICE_REC()
func.START()


tts_engine.runAndWait()