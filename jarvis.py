import pyttsx3 #pip intall pyttsx3
import datetime
import speech_recognition as sr #pip intall speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def takecommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='em-in')
        print(f"user said: {query}\n")    
        
    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"  
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')
    server.sendmail('', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

    # logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackpoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'C:\\Windows\\music'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strtime}")

    elif 'open visual studio code' in query:
        codePath = ""
        os.startfile(codePath)

    elif 'email to ' in query:
        try:
            speak("what should I say?")
            content = takecommand()
            to = ""
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry my friend. I am not able to send this email")       
