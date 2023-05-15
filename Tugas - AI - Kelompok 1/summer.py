import pyttsx3 #pip install di terminal
import speech_recognition as sr #install ini speechRecognition
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("initializing summer")

MASTER = ""

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
print (rate) 
engine.setProperty('rate', 130)


#speak
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
#function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
        speak("")
        
#microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        audio = r.listen(source)
        
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-us")
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("Say that again please")
        query = None
        
    return query
        
        
        
        
# main start here
speak("Hello my name is summer, i can help you!")
wishMe()
query = takeCommand()

# system logic for tasks as per query
if "wikipedia" in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
    
elif "open youtube" in query.lower():
    url = "youtube.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    
elif "open google" in query.lower():
    url = "google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    
elif "the time" in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M")
    speak(f"{MASTER} the time is {strTime}")
    
elif "open music" in query.lower():
    url = "open.spotify.com/intl-id"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    
elif "open whatsapp" in query.lower():
    url = "web.whatsapp.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    
elif "open gmail" in query.lower():
    url = "mail.google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    
