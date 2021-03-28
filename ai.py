import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import requests, json
import playsound
import datetime
import random
import face_recognition
import cv2
import numpy as np
import pyttsx3
from ecapture import ecapture as ec
import webbrowser
import time
import subprocess
import signal

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

a = random.randint(0,8)
b = random.randint(0,8)
c = random.randint(0,8)
d = random.randint(0,8)
e = random.randint(0,8)

urlyoutube = 'https://www.youtube.com'
urlgoogle = 'https://www.google.com/'

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        def speak(text):
            tts = gTTS(text=text, lang='it')
            filename = 'goodmorning.mp3'
            tts.save(filename)
            playsound.playsound(filename)
        speak("Good morning")
        print("Good morning :)")
    elif hour>=12 and hour<18:
        def speak(text):
            tts = gTTS(text=text, lang='it')
            filename = 'goodafternoon.mp3'
            tts.save(filename)
            playsound.playsound(filename)
        speak("Good afternoon")
        print("Good afternoon:)")
    else:
        def speak(text):
            tts = gTTS(text=text, lang='it')
            filename = 'goodevening.mp3'
            tts.save(filename)
            playsound.playsound(filename)
        speak("Good evening")
        print("Good evening:) ")

def listen():
    wishMe()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if e <= 2:
            def speak(text):
                tts = gTTS(text=text, lang='it')
                filename = 'voiceai91.mp3'
                tts.save(filename)
                playsound.playsound(filename)
            speak("Morning today? What can I do for you?")
            print("Morning today? What can I do for you? :)")
        elif e <= 4:
            def speak(text):
                tts = gTTS(text=text, lang='it')
                filename = 'voiceai92.mp3'
                tts.save(filename)
                playsound.playsound(filename)
            speak("If a good morning starts in the morning, today will be a really nice day, what can I do for you?")
            print("If a good morning starts in the morning, today will be a really nice day, what can I do for you? :)")
        elif e <= 6:
            def speak(text):
                tts = gTTS(text=text, lang='it')
                filename = 'voiceai93.mp3'
                tts.save(filename)
                playsound.playsound(filename)
            speak("I wanted to rest a little longer, what do you want?")
            print("I wanted to rest a little longer, what do you want? :(")
        elif e <= 8:
            def speak(text):
                tts = gTTS(text=text, lang='it')
                filename = 'voiceai94.mp3'
                tts.save(filename)
                playsound.playsound(filename)
            speak("brrrrr I'm not feeling so good, I must have drunk a little too much the other night, what can I do for you?")
            print("brrrrr I'm not feeling so good, I must have drunk a little too much the other night, what can I do for you? :)")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        return lock()
    return digital_assistant(data)

def lock():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        def speak(text):
            tts = gTTS(text=text, lang='it')
            filename = 'voiceainocap.mp3'
            tts.save(filename)
            playsound.playsound(filename)
        print("......")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        return lock()
    return digital_assistant(data)

def searchgoogle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        def speak(text):
            tts = gTTS(text=text, lang='it')
            filename = 'voiceaisearchgoogle.mp3'
            tts.save(filename)
            playsound.playsound(filename)
        speak("What do I have to look for?")
        print("What do I have to look for? :)")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("I have to search: " + data)
    except sr.UnknownValueError:
        return searchgoogle()
    webbrowser.open("https://google.com/search?q=%s" % data)
    return lock()

def searchyoutube():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        def speak(text):
            tts = gTTS(text=text, lang='it')
            filename = 'voiceaisearchgoogle.mp3'
            tts.save(filename)
            playsound.playsound(filename)
        speak("What do I have to look for?")
        print("What do I have to look for? :)")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("I have to search: " + data)
    except sr.UnknownValueError:
        return searchyoutube()
    webbrowser.open("https://youtube.com/search?q=%s" % data)
    return lock()

def digital_assistant(data):
    try:
        if "how are you" in data:
            listening = True
            if a <= 2:
                def speak(text):
                    tts = gTTS(text=text, lang='it')
                    filename = 'voiceai21.mp3'
                    tts.save(filename)
                    playsound.playsound(filename)
                speak("I'm fine, can't wait for summer to come")
                print("I'm fine, can't wait for summer to come :p")
                return lock()
            elif a <= 4:
                def speak(text):
                    tts = gTTS(text=text, lang='it')
                    filename = 'voiceai22.mp3'
                    tts.save(filename)
                    playsound.playsound(filename)
                speak("I feel really good today")
                print("I feel really good today :p")
                return lock()
            elif a <= 6:
                def speak(text):
                    tts = gTTS(text=text, lang='it')
                    filename = 'voiceai23.mp3'
                    tts.save(filename)
                    playsound.playsound(filename)
                speak("I don't feel so good, I must have some broken circuit, I think it's the cipset")
                print("I don't feel so good, I must have some broken circuit, I think it's the cipset :(")
                return lock()
            elif a <= 8:
                def speak(text):
                    tts = gTTS(text=text, lang='it')
                    filename = 'voiceai23.mp3'
                    tts.save(filename)
                    playsound.playsound(filename)
                speak("You know I often ask myself, but I never know what to answer, it's difficult")
                print("You know I often ask myself, but I never know what to answer, it's difficult :|")
                return lock()
             
        if "realtime" in data or "real time" in data:
            listening = True
            def speak(text):
                tts = gTTS(text=text, lang='it')
                filename = 'voiceaitime.mp3'
                tts.save(filename)
                playsound.playsound(filename)
            speak(current_time)
            print("It's", current_time)
            return lock()
          
        if 'video' in data or 'Video' in data:
            def speak(text):
                tts = gTTS(text=text, lang='it')
                filename = 'voiceaiyoutube.mp3'
                tts.save(filename)
                playsound.playsound(filename)
            speak("Okay")
            print("Okay")
            return searchyoutube()
          
        if 'google' in data or 'Google' in data or 'search' in data:
            def speak(text):
                tts = gTTS(text=text, lang='it')
                filename = 'voiceaigoogle.mp3'
                tts.save(filename)
                playsound.playsound(filename)
            speak("Okay")
            print("Okay :)")
            return searchgoogle()
          
        if 'performance' in data or 'control' in data:
            def speak(text):
                tts = gTTS(text=text, lang='it')
                filename = 'voiceaiwrite.mp3'
                tts.save(filename)
                playsound.playsound(filename)
                os.system("/usr/bin/gnome-system-monitor")
            speak("We check the processes")
            print("We check the processes 8|")
            return lock()
          
        if "close" in data or "exit" in data:
            listening = True
            if c <= 2:
                def speak(text):
                    tts = gTTS(text=text, lang='it')
                    filename = 'voiceai41.mp3'
                    tts.save(filename)
                    playsound.playsound(filename)
                speak("Are you sure? And that's okay, see you later")
                print("Are you sure? And that's okay, see you later :(")

            elif c <= 4:
                def speak(text):
                    tts = gTTS(text=text, lang='it')
                    filename = 'voiceai42.mp3'
                    tts.save(filename)
                    playsound.playsound(filename)
                speak("No no please don't, noooooooooooooooo sku sku ble ble ble blu blu nu nuuuuuu")
                print("No no please don't, noooooooooooooooo sku sku ble ble ble blu blu nu nuuuuuu............")

            elif c <= 6:
                def speak(text):
                    tts = gTTS(text=text, lang='it')
                    filename = 'voiceai43.mp3'
                    tts.save(filename)
                    playsound.playsound(filename)
                speak("I'm in charge here, you can't tell me what to do and what not to do, hello")
                print("I'm in charge here, you can't tell me what to do and what not to do, hello >(")

            elif c <= 8:
                def speak(text):
                    tts = gTTS(text=text, lang='it')
                    filename = 'voiceai44.mp3'
                    tts.save(filename)
                    playsound.playsound(filename)
                speak("Okay")
                print("Okay")
    except sr.UnknownValueError:
    return lock()

time.sleep(10)
listening = True
while listening == True:
    data = listen()
    listening = digital_assistant(data)
