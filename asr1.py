import pyttsx3
engine = pyttsx3.init()

def speak(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #changing index changes voices but ony 0 and 1 are working here
    engine.say(text)
    engine.runAndWait()
