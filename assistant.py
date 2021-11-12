import speech_recognition as sr 
import pyttsx3
import datetime
import wikipedia
import webbrowser
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)
def say(audio):
    engine.say(audio)
    engine.runAndWait()
def wish():
    a=int(datetime.datetime.now().hour)
    if (0<=a<12):
        say("Good morning!")
    elif(12<a<=16):
        say("Good Afternoon!")
    else:
        say("Good Evening!")
    say("Hello sir/ma'am, This is Julliete at your service!")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("listening...")
        audio=r.listen(source)    
    try:
        print("Understanding...")
        query= r.recognize_google(audio)
        print(query)
        
    except Exception as e :
        print(e)
        print("say that again...")
        return "none"
    return query
wish()
while True :
    query = take_command().lower()
    if 'wikipedia' in query:
        query = query.replace("Wikipedia","")
        results=wikipedia.summary(query, sentences=3)
        say("According to wikipedia")
        say(results)
        print(results)
        say("Thank you")
    if 'open youtube' in query:
        webbrowser.open("youtube.com")
    if 'open google' in query:
        webbrowser.open("google.com")
    if 'stop' in query:
        say("Thankyou for choosing me")
        break
    



