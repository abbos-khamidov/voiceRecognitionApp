import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio

# get mic audio

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception " + str(e))
    return said

# def 