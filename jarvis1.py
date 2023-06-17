import os
import datetime
import pyttsx3 #pip intall pyttsx3
import speech_recognition as sr #pip intall speechRecognition
import wikipedia #pip install wikipedia
import webbrowser
import smtplib
import pywhatkit as kit #pip install pywhatkit
import python_weather #pip install python_weather

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#File handling, It saves the execution to a new text file 
with open ("C:\Users\admin\Desktop\file1",'a') as myobject:
    content = myobject.write()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Happy Morning!")

    elif hour>=12 and hour<18:
        speak("Happy Afternoon!")

    else:
        speak("Happy Evening!")

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
    server.login('sender mail id', 'password')
    server.sendmail('recever email id', to, content)
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
        codePath = "file directory"
        os.startfile(codePath)

    elif 'email to asha' in query:
        try:
            speak("what should I say?")
            content = takecommand()
            to = "sender email"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry my friend. I am not able to send this email")

    elif 'open instagram' in query:
        webbrowser.open("instagram.com")
             
    elif 'open flipkart'in query:
        webbrowser.open("flipkart.com")

    elif 'open amazon' in query:
        webbrowser.open("amazon.com")

    elif 'open spotify' in query:
        webbrowser.open("spotify.com")
         
    elif 'open Netflix' in query:
        webbrowser.open("Netflix.com")

    elif 'open Swiggy' in query:
        webbrowser.open("Swiggy.com")

    elif 'open zomato' in query:
        webbrowser.open("Zomato.com")     

    elif 'open Google Map' in query:
        webbrowser.open("maps.google.com")

    elif 'open Facebook' in query:
        webbrowser.open("Facebook.com")

    elif 'open Hotstar' in query:
        webbrowser.open("hotstar.com")

    elif 'open Prime video' in query:
        webbrowser.open("primevideo.com")

    elif 'open Twitter' in query:
        webbrowser.open("twitter.com")

    elif 'open Discord' in query:
        webbrowser.open("discord.com")

    elif 'weather' in query:
        weather = get(inda)
        python_weather.weather(c)
        print("todays weather is{weather}")
#it send msg directly to the sender
try:
     number = ''
     kit.sendwhatmsg(number,'text',24,0)
 
     print("Message Sent!")
 
except: 
     print("Error in sending the message")