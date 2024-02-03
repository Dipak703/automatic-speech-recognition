import speech_recognition as sr
import asr1 as x
from turtle import *
color("black")
title("ASR")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        nt = 284
        setposition(-360, nt)
        nt -= 16
        pendown()
        write("listening...", font=["airal", 14, "normal"]) 
        penup()
        r.energy_threshold = 1000
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        setposition(-360, nt)
        nt -= 16
        pendown()
        write("recognizing...", font=["airal", 14, "normal"])
        penup()

        query = r.recognize_google(audio, language="en-IN")
        setposition(-360, nt)
        nt -= 16
        pendown()
        write(f"user said : {query}", font=["airal", 14, "normal"])
        penup()
        return query
    except Exception as e:
        setposition(-360, nt)
        nt -= 16
        pendown()
        write("please say it again...", font=["airal", 14, "normal"])
        penup()


def select_language():
    try:
        penup()
        nt = 300
        setposition(-360, nt)
        nt -= 16
        pendown()
        write("Please tell in which language you want to script:\nby default is english", font=[
              "airal", 14, "normal"])
        penup()
        x.speak('select your language, tell hindi to use hindi')
        D = {"English": "en-IN", "Hindi": "hi-IN"}
        return (D[listen()])
    except Exception as e:
        x.speak("language not recognised")


sc = str(select_language())


def asrlisten():
    nt = 201
    r = sr.Recognizer()
    with sr.Microphone() as source:
        setposition(-360, nt)

        nt -= 17
        pendown()
        write("listening...", font=["airal", 14, "normal"])
        penup()
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)
    try:
        setposition(-360, nt)
        nt -= 17
        pendown()
        write("recognizing...", font=["airal", 14, "normal"])
        penup()
        query = r.recognize_google(audio, language=sc)
        # x.speak(f"{query}")
        if sc == "en-IN":
            with open("asr.txt", "a") as f:
                f.write(f"{query}\n")
        return query
    except Exception as e:
        pass

x.speak("I am asr system ")
# x.speak("welcome to automated voice recognition system")
nt = 220
setposition(-360, nt)
nt -= 19
pendown()
write("To stop the program say 010", font=["airal", 14, "normal"])
penup()
x.speak("To stop the program say 010")
nt = 163
while True:
    ab = str(asrlisten())
    if len(ab)<50:
        setposition(-360, nt)
        nt -= 19
        pendown()
        write(f" user said : {ab}", font=["airal", 14, "normal"])
        penup() 
    if len(ab)>50:
        setposition(-360, nt)
        nt -= 19
        pendown()
        write(f" user said : {ab[0:50]}", font=["airal", 14, "normal"])
        penup() 
        bc = ab[50:100]
        cd = ab[100:]
        setposition(-360, nt)
        nt -= 19
        pendown()
        write(f" \t  {bc}", font=["airal", 14, "normal"])
        penup()
        setposition(-360, nt)
        nt -= 19
        pendown()
        write(f" \t  {cd}", font=["airal", 14, "normal"])
        penup()
    if ab == "010":
        setposition(-360, nt)
        write("Thank you for using ASR", font=["airal", 14, "normal"])
        x.speak("thank you for using ASR")
        pendown()
        done()
        break
