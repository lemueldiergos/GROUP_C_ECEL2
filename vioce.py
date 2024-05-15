import speech_recognition           # Library for Voice Recoginition
import pyttsx3                      # Text to speech library
import requests                     # used to request the current lcoation online
import nltk                         # NLP library
import datetime                     # date and time library
from tkinter import *               # UI Lib
import psutil                       # System and process utilities


from nltk.tokenize import *         
from nltk.stem     import *
from nltk.corpus   import *

from speech_recognition.recognizers import *

global MAIN_ROOT
MAIN_ROOT = Tk()

labeltxt = StringVar()
labeltxt.set("Waiting...")

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
        DAY_CHECK         = ['date','day', 'today', 'month', 'week']
        BAT_STAT          = ['battery', 'status']

        TOKEN_MOB = []

        for WORDS in self.arr_t:
            if WORDS not in self.w_stop:
                TOKEN_MOB.append(WORDS)
            


        for LOC_WORDS in TOKEN_MOB:
            if LOC_WORDS in ['dictionary', 'mode']:
                tts_engine.say("Ask for any words, and I will provide you with the definition.")
                tts_engine.runAndWait()
                labeltxt.set("Dictionary Mode")
                MAIN_ROOT.update()
                try:
                    DIC_TO_WORD = self.VOICE_REC()
                    DEF_GET = wordnet.synsets(DIC_TO_WORD)
                    labeltxt.set(DEF_GET[0].definition())
                    MAIN_ROOT.update()
                    tts_engine.say(DEF_GET[0].definition())
                    MAIN_ROOT.after(2000, labeltxt.set("Waiting..."))
                except:
                    labeltxt.set("Sorry, the dictionary is only limited to 1 word.")
                    MAIN_ROOT.update()
                    tts_engine.say("Sorry, the dictionary is only limited to 1 word.")
                    MAIN_ROOT.after(2000, labeltxt.set("Waiting..."))
                break
            

            if LOC_WORDS in BAT_STAT:
                BAT_STAT_CMD = psutil.sensors_battery()
                tts_engine.say("The Battery percentage of your device is " + str(int(BAT_STAT_CMD.percent)) + " %")
                labeltxt.set("The Battery percentage of your device is "  + str(int(BAT_STAT_CMD.percent)) + " %")
                MAIN_ROOT.update()
                MAIN_ROOT.after(2000, labeltxt.set("Waiting..."))
                break 

            for LK_WORDS in LOCATION_KEYWORDS:
                try:
                    if str(LOC_WORDS) == str(LK_WORDS):
                        rjson = requests.get('https://get.geojs.io/v1/ip.json')         
                        IP = rjson.json()['ip']
                        GETLOC = requests.get('https://get.geojs.io/v1/geo/' + IP + '.json' )
                        tts_engine.say("Your Current Location is "+ str(GETLOC.json()['city']) + ".")
                        labeltxt.set("Your Current Location is "+ str(GETLOC.json()['city']) + ".")
                        MAIN_ROOT.update()
                        MAIN_ROOT.after(2000, labeltxt.set("Waiting..."))
                except:
                    tts_engine.say("Sorry no Internet Connection to get the location")

      
            for CK_WORDS in TIME_KEYWORDS:
                if str(LOC_WORDS) == str(CK_WORDS):
                    STATIC_TIME = datetime.datetime.now()
                    TIME_TO_SAY = str("the time is " + str(int(STATIC_TIME.strftime("%I"))) + ":" + str(int(STATIC_TIME.strftime("%M"))) + " " + STATIC_TIME.strftime("%p"))
                    print(TIME_TO_SAY)
                    labeltxt.set(TIME_TO_SAY)
                    MAIN_ROOT.update()
                    MAIN_ROOT.after(2000, labeltxt.set("Waiting..."))
                    tts_engine.say(TIME_TO_SAY)
                    

            for DC_WORDS in DAY_CHECK:
                if str(LOC_WORDS) == str(DC_WORDS):
                    STATIC_TIME = datetime.datetime.now()
                    TIME_TO_SAY = str("Today is " + str(STATIC_TIME.strftime("%B")) + " " + str(int(STATIC_TIME.strftime("%d"))) + " " + STATIC_TIME.strftime("%Y"))
                    print(TIME_TO_SAY)
                    labeltxt.set(TIME_TO_SAY)
                    MAIN_ROOT.update()
                    tts_engine.say(TIME_TO_SAY)
                    MAIN_ROOT.after(2000, labeltxt.set("Waiting..."))
                    break
                
                    
        

    def VOICE_REC(self):
        labeltxt.set("Listening...")
        MAIN_ROOT.update()
        recognizer = speech_recognition.Recognizer()
        
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    
                    print("Listening...")
                    recognizer.adjust_for_ambient_noise(mic, duration=0.1)
                    audio = recognizer.listen(mic)
                    text = str(recognizer.recognize_google(audio))
                    text = text.lower()
                    labeltxt.set(text)
                    MAIN_ROOT.update()
                    #print(text)
                    self.voice = text
                    print("END")
                    return self.voice
                    
                    
            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                #print("ERROR WHILE LISTENING")
                continue
            except speech_recognition.RequestError:
                
                print("error!")
                break
     
    def NON_COMMAND_VOICE(self):
        tts_engine.say("Apologies, I couldn't quite catch that. Could you please rephrase or provide more context?")
print("\n--------------------------------------------------------------------------------------------------------")

func = MAIN()

MAIN_ROOT.title("Voice Command")
MAIN_ROOT.geometry("500x500")

#func.VOICE_REC()


def printter():
    
    print("start voice")
    tts_engine.say("Hello! How can I assist you today?")
    tts_engine.runAndWait()
    func.VOICE_REC()
    
    func.START()
    
    tts_engine.runAndWait()
    
    


TRIG_VOICE = Button(MAIN_ROOT, text="Say something?", height=5, width=20, command=printter)
LABEL      = Label(MAIN_ROOT, textvariable=labeltxt, wraplength=200, justify="center")
TRIG_VOICE.pack(pady=100)
LABEL.pack(pady=0.1)

MAIN_ROOT.mainloop()

